#!/usr/bin/env python3
"""Rank vetted whole-home customization vendors from a CSV table.

Usage:
  rank_vendors.py vendors.csv answers.json --top 5

The script is intentionally simple: it helps sort candidates, but the agent
should still read notes, perform a recent web check, and write the final advice.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


ALIASES = {
    "vendor_name": ["vendor_name", "name", "商家", "商家名称", "公司", "公司名称", "品牌", "工作室"],
    "service_area": ["service_area", "city", "城市", "地区", "覆盖区域", "服务城市", "服务区域", "门店城市"],
    "scope": ["scope", "services", "业务范围", "品类", "服务内容", "主营", "适合项目"],
    "budget": ["budget", "budget_positioning", "价格定位", "预算档位", "预算", "价格", "客单价"],
    "style": ["style", "design_style", "风格", "设计风格", "审美", "设计能力"],
    "materials": ["materials", "板材", "材料", "环保", "五金", "供应链"],
    "timeline": ["timeline", "typical_timeline", "工期", "交付", "排期", "安装周期"],
    "strengths": ["strengths", "优势", "特点", "推荐理由", "适合人群", "亮点"],
    "caveats": ["caveats", "短板", "注意事项", "不适合", "风险点", "备注"],
    "source_notes": ["source_notes", "来源", "考察记录", "大V备注", "备注", "notes"],
}

REMOTE_TERMS = ["全国", "线上", "远程", "周边", "跨城"]


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def pick(row: dict[str, str], field: str) -> str:
    for key in ALIASES[field]:
        if key in row and normalize_text(row[key]):
            return normalize_text(row[key])
    return ""


def tokens(text: str) -> list[str]:
    text = normalize_text(text).lower()
    parts = re.split(r"[\s,，、/;；|｜]+", text)
    return [part for part in parts if part]


def contains_any(haystack: str, needles: list[str]) -> bool:
    haystack = normalize_text(haystack).lower()
    return any(needle.lower() in haystack for needle in needles if needle)


def overlap_score(text: str, wanted: list[str], points: int) -> tuple[int, list[str]]:
    matched = [term for term in wanted if term and term.lower() in normalize_text(text).lower()]
    if not matched:
        return 0, []
    return min(points, max(1, len(matched)) * max(1, points // 3)), matched


def answer_terms(answers: dict[str, Any], *keys: str) -> list[str]:
    out: list[str] = []
    for key in keys:
        value = answers.get(key)
        if isinstance(value, list):
            for item in value:
                out.extend(tokens(str(item)))
        elif value:
            out.extend(tokens(str(value)))
    return list(dict.fromkeys(out))


def score_row(row: dict[str, str], answers: dict[str, Any]) -> dict[str, Any]:
    score = 0
    reasons: list[str] = []
    warnings: list[str] = []

    city_terms = answer_terms(answers, "city", "district", "nearby_city")
    area = pick(row, "service_area")
    if city_terms:
        if contains_any(area, city_terms):
            score += 25
            reasons.append("service area matches")
        elif contains_any(area, REMOTE_TERMS):
            score += 12
            reasons.append("remote or nearby service may work")
        else:
            score -= 80
            warnings.append("service area may not match")

    scope_terms = answer_terms(answers, "scope", "project_scope", "services")
    gained, matched = overlap_score(pick(row, "scope") + " " + pick(row, "strengths"), scope_terms, 15)
    score += gained
    if matched:
        reasons.append("scope matches: " + ", ".join(matched[:4]))

    budget_terms = answer_terms(answers, "budget", "budget_level", "price_preference")
    gained, matched = overlap_score(pick(row, "budget") + " " + pick(row, "strengths"), budget_terms, 15)
    score += gained
    if matched:
        reasons.append("budget language matches: " + ", ".join(matched[:4]))

    style_terms = answer_terms(answers, "style", "design_style", "aesthetic")
    gained, matched = overlap_score(pick(row, "style") + " " + pick(row, "strengths"), style_terms, 10)
    score += gained
    if matched:
        reasons.append("style matches: " + ", ".join(matched[:4]))

    material_terms = answer_terms(answers, "materials", "environment", "environmental_priority")
    gained, matched = overlap_score(pick(row, "materials") + " " + pick(row, "strengths"), material_terms, 10)
    score += gained
    if matched:
        reasons.append("materials/environment matches: " + ", ".join(matched[:4]))

    timeline_terms = answer_terms(answers, "timeline", "deadline", "move_in")
    gained, matched = overlap_score(pick(row, "timeline") + " " + pick(row, "strengths"), timeline_terms, 10)
    score += gained
    if matched:
        reasons.append("timeline language matches: " + ", ".join(matched[:4]))

    priority_terms = answer_terms(answers, "priorities", "service_preference")
    gained, matched = overlap_score(
        " ".join([pick(row, "strengths"), pick(row, "style"), pick(row, "materials"), pick(row, "source_notes")]),
        priority_terms,
        20,
    )
    score += gained
    if matched:
        reasons.append("priority matches: " + ", ".join(matched[:5]))

    dealbreakers = answer_terms(answers, "dealbreakers")
    caveats = pick(row, "caveats")
    if dealbreakers and contains_any(caveats, dealbreakers):
        score -= 30
        warnings.append("caveats may touch dealbreakers")

    return {
        "vendor_name": pick(row, "vendor_name") or "(unnamed)",
        "score": score,
        "reasons": reasons,
        "warnings": warnings,
        "fields": {
            "service_area": area,
            "scope": pick(row, "scope"),
            "budget": pick(row, "budget"),
            "strengths": pick(row, "strengths"),
            "caveats": caveats,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("answers_json", type=Path)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()

    answers = json.loads(args.answers_json.read_text(encoding="utf-8"))
    with args.csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    ranked = [score_row(row, answers) for row in rows]
    ranked.sort(key=lambda item: item["score"], reverse=True)
    print(json.dumps(ranked[: args.top], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
