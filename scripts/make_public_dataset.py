#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

from openpyxl import Workbook


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "whole-home-customization-vendors.csv"
OUT_DIR = ROOT / "data"

PUBLIC_FIELDS = [
    "record_id",
    "record_type",
    "city",
    "service_area",
    "scope",
    "budget_positioning",
    "design_style",
    "materials",
    "environmental_standard",
    "typical_timeline",
    "verification_date",
    "verified_by",
    "vendor_label",
    "vendor_name",
    "contact_person",
    "address",
    "district",
    "store_type",
    "authorization",
    "customer_segments",
    "board_materials",
    "recommended_boards",
    "hardware",
    "starting_price_projection",
    "edge_band_material",
    "edge_banding_process",
    "edge_banding_equipment",
    "cabinet_structure",
    "cabinet_connectors_feet",
    "measurement_design_fee",
    "deposit_refund_policy",
    "designer_team",
    "rendering_cycle",
    "outsourced_design",
    "installation_team",
    "damage_handling",
    "floor_protection",
    "aftersales_staff",
    "warranty_policy",
    "customization_cycle",
    "retain_final_payment",
    "payment_terms",
    "creator_comment",
    "strengths",
    "caveats",
    "source_name",
    "source_type",
    "source_author",
    "source_date",
    "source_page_or_rows",
    "source_confidence",
]


FIELD_NOTES = {
    "record_id": "Stable row id.",
    "record_type": "vendor or external_note.",
    "source_confidence": "high/medium/low confidence in structured extraction completeness.",
    "vendor_name": "Formal vendor name when known; blank means the source only gave a label/contact.",
    "creator_comment": "Summarized creator/source comment; verify before publishing as final advice.",
    "caveats": "Known fit limits or verification reminders.",
}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    public_rows = [
        {field: row.get(field, "") for field in PUBLIC_FIELDS}
        for row in rows
    ]

    csv_path = OUT_DIR / "whole-home-customization-vendors.public.csv"
    json_path = OUT_DIR / "whole-home-customization-vendors.public.json"
    xlsx_path = OUT_DIR / "whole-home-customization-vendors.public.xlsx"

    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PUBLIC_FIELDS)
        writer.writeheader()
        writer.writerows(public_rows)

    json_path.write_text(json.dumps(public_rows, ensure_ascii=False, indent=2), encoding="utf-8")

    wb = Workbook()
    ws = wb.active
    ws.title = "vendors"
    ws.append(PUBLIC_FIELDS)
    for row in public_rows:
        ws.append([row.get(field, "") for field in PUBLIC_FIELDS])
    notes = wb.create_sheet("field_notes")
    notes.append(["field", "note"])
    for field in PUBLIC_FIELDS:
        notes.append([field, FIELD_NOTES.get(field, "")])
    wb.save(xlsx_path)

    print(f"Wrote {len(public_rows)} rows to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
