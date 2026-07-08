# Vendor Table Schema

The table may be CSV, XLSX, Numbers export, or pasted markdown. CSV is easiest for the helper script.

## Minimum useful columns

- `vendor_name`: vendor, company, studio, or brand name.
- `service_area`: city, district, province, nearby cities, remote service, or showroom coverage.
- `scope`: project types supported, such as whole-home customization, kitchen cabinets, wardrobes, storage planning, woodwork, interior design, or installation.
- `budget_positioning`: low, mid, mid-high, high-end, luxury, or typical price range.
- `strengths`: why this vendor was included.
- `caveats`: known fit limits, such as slower schedule, high design fee, limited areas, or not ideal for ultra-low budgets.
- `source_notes`: source, inspection notes, creator notes, or recommendation evidence.

## Recommended columns

- `city`
- `districts`
- `showroom_address`
- `contact_channel`
- `verification_date`
- `verified_by`
- `design_style`
- `materials`
- `environmental_standard`
- `delivery_capacity`
- `installation_capacity`
- `after_sales`
- `typical_timeline`
- `minimum_budget`
- `maximum_budget`
- `ideal_customer`
- `not_ideal_for`
- `recent_public_risk`
- `case_links`
- `notes_private`

## Common Chinese aliases

- Vendor name: `商家`, `商家名称`, `公司`, `公司名称`, `品牌`, `工作室`
- Service area: `城市`, `地区`, `覆盖区域`, `服务城市`, `服务区域`, `门店城市`
- Scope: `业务范围`, `品类`, `服务内容`, `主营`, `适合项目`
- Budget positioning: `预算`, `价格`, `价格定位`, `预算档位`, `客单价`
- Strengths: `优势`, `特点`, `推荐理由`, `适合人群`, `亮点`
- Caveats: `短板`, `注意事项`, `不适合`, `风险点`, `备注`
- Materials: `板材`, `材料`, `环保`, `五金`, `供应链`
- Style: `风格`, `设计风格`, `审美`, `设计能力`
- Timeline: `工期`, `交付`, `排期`, `安装周期`

## Data hygiene

Keep private notes separate from public recommendation text. If a row includes personal phone numbers, WeChat IDs, internal prices, or unpublished inspection notes, ask whether those details can be shared before including them in an answer.

Track `verification_date` whenever possible. Rows older than 6-12 months should still be usable, but should receive a stronger recent web check.

