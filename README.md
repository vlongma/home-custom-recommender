# Home Custom Recommender

一个用于“全屋定制/柜体定制/设计统筹”推荐的 Codex skill，内置一份官方维护的商家数据源。适合搜索和使用场景包括：杭州全屋定制推荐、全屋定制避坑、装修避坑、精装房改造、二手房翻新、开放式厨房改造、橱柜定制、衣柜定制、全屋柜体、设计工作室推荐、靠谱商家白名单、装修顾问、装修博主工具。

它适合博主、装修顾问或社群运营者发布一份自己维护的官方商家名单，然后通过问询用户的城市、预算、风格、材料、工期和雷点，给出更合适的商家推荐。下载者不需要替换表格。

交互方式默认是选择题引导：每轮只问一个主题，优先给 2-4 个选项，并允许用户选择“其他/跳过”。如果 Codex/宿主环境支持可点击选择框，skill 会优先使用原生选择控件；如果当前环境不支持可点击选择框，会退回为编号选项。用户可以点选、回编号、回选项文字，或者直接用自然语言回答。

## What is included

- `skills/home-custom-recommender/`: Codex skill。
- `skills/home-custom-recommender/assets/default-vendors.csv`: skill 内置官方数据源，安装后默认使用。
- `skills/home-custom-recommender/assets/default-vendors.json`: 同一内置数据源的 JSON 版本。
- `skills/home-custom-recommender/assets/default-vendors.xlsx`: 同一内置数据源的 Excel 版本。
- `data/whole-home-customization-vendors.public.csv`: 公开版数据源副本，方便在 GitHub 上预览。
- `data/whole-home-customization-vendors.public.json`: 公开版 JSON 副本。
- `data/whole-home-customization-vendors.public.xlsx`: 公开版 Excel 副本。
- `examples/hangzhou-gongshu-request.json`: 示例用户需求。
- `install.sh`: 一键安装 skill 到本机 Codex skills 目录。
- `update.sh`: 拉取最新版并重装本机 skill。

## Keywords

中文关键词：

- 全屋定制推荐
- 杭州全屋定制
- 杭州全屋定制哪家靠谱
- 全屋定制避坑
- 装修避坑
- 装修商家推荐
- 靠谱全屋定制
- 全屋定制白名单
- 柜体定制
- 橱柜定制
- 衣柜定制
- 全屋柜体
- 精装房改造
- 二手房翻新
- 开放式厨房改造
- 中古风装修
- 设计统筹
- 装修顾问
- 装修博主工具
- Codex skill

English keywords:

- whole home customization
- custom cabinets
- cabinet vendor recommendation
- renovation advisor
- interior design vendor
- home renovation assistant
- vetted vendor database
- Codex skill

Suggested GitHub topics:

```text
codex-skill
home-renovation
interior-design
custom-cabinets
whole-home-customization
vendor-recommendation
renovation-advisor
装修
全屋定制
杭州全屋定制
装修避坑
```

## Install

Clone or download this repository, then run:

```bash
./install.sh
```

Restart Codex after installation.

If you prefer manual install:

```bash
cp -R skills/home-custom-recommender "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Update

Installed skills do not update automatically. When this repository publishes new vendor data or skill behavior, update from your local clone:

```bash
cd home-custom-recommender
./update.sh
```

`update.sh` will run `git pull --ff-only` when the folder is a Git clone, remove the old installed skill, copy the latest bundled skill and official vendor table into Codex, and ask you to restart Codex.

If you prefer manual update:

```bash
cd home-custom-recommender
git pull
rm -rf "${CODEX_HOME:-$HOME/.codex}/skills/home-custom-recommender"
cp -R skills/home-custom-recommender "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after updating.

## Use

After restarting Codex, invoke the skill with:

```text
Use $home-custom-recommender to recommend suitable whole-home customization vendors from its bundled official vendor table.
```

Chinese prompt example:

```text
用 $home-custom-recommender 根据内置官方商家表，帮我给一个杭州拱墅区、精装局改、预算 10-20 万的用户推荐全屋定制商家。
```

For a guided interview, start naturally:

```text
用 $home-custom-recommender，我想装修。
```

The skill should ask choice-first questions instead of giving the user a long open-ended form.

## Data model

Core fields:

- `record_type`: `vendor` for recommendable merchants, `external_note` for source notes or search leads.
- `city`, `service_area`, `district`: where the vendor can serve.
- `scope`: whole-home customization, cabinet customization, design service, soft furnishing, hard furnishing, etc.
- `budget_positioning`: rough budget fit.
- `materials`, `environmental_standard`: board/material/environment keywords.
- `typical_timeline`: delivery or production timeline.
- `strengths`: why this vendor may fit.
- `caveats`: what to verify before recommending.
- `source_confidence`: how complete/reliable the extracted row is.

Rows can be incomplete. If a blogger clearly listed a vendor but details are missing, keep it as `record_type=vendor`, leave unknown fields blank, and set `source_confidence=low`.

## Ranking helper

The skill includes a helper script:

```bash
python3 skills/home-custom-recommender/scripts/rank_vendors.py \
  skills/home-custom-recommender/assets/default-vendors.csv \
  examples/hangzhou-gongshu-request.json \
  --top 5
```

The script is only a sorting aid. The final recommendation should still consider the user's answers, source confidence, caveats, and recent public information.

## Official data note

This repository includes a public-friendly official dataset. It removes local file paths and large raw extraction text.

Before publishing official data publicly:

- Confirm you have permission to share third-party lists or creator notes.
- Remove private contacts, phone numbers, WeChat IDs, private prices, and unpublished internal comments.
- Keep `source_confidence` honest.
- Avoid promising "zero risk" or "safe to choose blindly"; recommend based on fit and current verification.

## Data updates

Ordinary users do not need to replace the table. The skill is meant to use the bundled official dataset.

Maintainers can update the official dataset, regenerate the public copies, copy the generated files into `skills/home-custom-recommender/assets/`, and publish a new GitHub release:

```bash
python3 scripts/make_public_dataset.py
cp data/whole-home-customization-vendors.public.csv skills/home-custom-recommender/assets/default-vendors.csv
cp data/whole-home-customization-vendors.public.json skills/home-custom-recommender/assets/default-vendors.json
cp data/whole-home-customization-vendors.public.xlsx skills/home-custom-recommender/assets/default-vendors.xlsx
```

Users should update by pulling or downloading the latest release, not by editing their local table.
