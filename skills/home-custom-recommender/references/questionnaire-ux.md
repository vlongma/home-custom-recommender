# Questionnaire UX

Use this reference when interviewing an end user. The goal is to feel like a guided product flow, not a homework form.

## Core rules

- Ask one topic per turn.
- After asking one question, stop. Do not confirm the answer, ask the next question, or summarize progress in the same assistant turn.
- Prefer 2-4 choices plus `其他/我补充` and `跳过`.
- If the runtime provides a native choice/picker UI, use it.
- If no native choice UI is available, render numbered choices in text.
- Accept numbers, option labels, and natural-language replies.
- Confirm important inferred details only at the beginning of the next assistant turn, then ask exactly one next question.
- Do not force the user to answer every detail before making progress.

## Single-question stop rule

This rule is strict:

1. If you render a native choice/picker UI, do not also render a text fallback for that same question.
2. If you render a native choice/picker UI, do not ask the next question in plain text below it.
3. If the user just answered a choice, acknowledge briefly and ask exactly one next question, then stop.
4. Never show "Question 2" and "Question 3" in the same assistant message.
5. Never combine a visible choice card with the next numbered question in the same assistant message.

Good:

```text
好，新房毛坯。

你的新房大概多大？

1. 90㎡以下
2. 90-130㎡
3. 130-180㎡
4. 180㎡以上
5. 其他，我补充
```

Bad:

```text
好，新房毛坯，130-180㎡，3-4室。

第三问：你打算做哪些定制内容？
...
```

## Text fallback format

Use this pattern when native choice UI is unavailable:

```text
这套房子在哪个范围？

1. 杭州主城区
2. 杭州周边
3. 不在杭州
4. 其他，我补充

你可以直接回数字。
```

Avoid asking more than one numbered question in the same turn. Do this even if the user seems comfortable. Only switch to a compact form when the user explicitly asks to speed up.

## Recommended question flow

### 1. City scope

Ask:

```text
这套房子在哪个范围？

1. 杭州主城区
2. 杭州周边
3. 上海
4. 其他城市，我补充
```

Then ask district if the city has matching data.

### 2. Renovation type

```text
你这次更像哪种情况？

1. 新房毛坯装修
2. 二手房翻新
3. 精装房局部改造
4. 只补柜子/局部收纳
```

### 3. Project scope

Allow multi-select by saying the user can pick multiple numbers:

```text
这次主要想做哪些部分？可以多选。

1. 全屋柜体
2. 客厅/电视柜/收纳
3. 厨房/橱柜
4. 衣柜/衣帽间
5. 需要设计统筹
6. 其他，我补充
```

### 4. Budget

Adjust options by city and project scope when possible:

```text
定制部分预算大概在哪个区间？

1. 10 万以内
2. 10-20 万
3. 20-30 万
4. 30 万以上
5. 还没概念
```

### 5. Priorities

Ask for top three, not everything:

```text
这几个里你最看重哪 3 个？可以回数字。

1. 设计好看
2. 环保材料
3. 收纳规划
4. 安装细节
5. 沟通省心
6. 性价比
7. 交付速度
8. 售后稳定
```

If the user chooses too many, ask them to narrow to three.

### 6. Style

```text
风格更接近哪种？

1. 现代简约
2. 原木/奶油
3. 中古
4. 轻奢/高定感
5. 实用收纳优先
6. 其他，我补充
```

### 7. Timeline

```text
时间上急不急？

1. 1-2 个月内要安装
2. 3 个月内安装
3. 半年内入住
4. 不急，可以慢慢做
```

### 8. Dealbreakers

```text
这些里面哪些你不能接受？可以多选。

1. 定金不退
2. 付款太靠前
3. 工期太长
4. 沟通慢
5. 设计弱
6. 没有本地门店
7. 其他，我补充
```

## When enough information is collected

Once city, district, renovation type, scope, budget, top priorities, style, timeline, and dealbreakers are clear enough, stop interviewing and start filtering. Do not keep asking just because more details could be useful.
