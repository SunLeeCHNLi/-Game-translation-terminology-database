# NTE 多语言术语库（nte-glossary/）

按**目标语言**拆分为独立文件夹，每个文件夹内按**类目**分文件存放。共 9 种语言、21 个类目。

## 数据来源

- 种子数据：官方推广资料
- 待合并：UE5 客户端 `HT/Content/Localization/` 下的 `.locres` 文件

## 文件格式

所有 CSV 均为 **UTF-8（含 BOM）** 编码、**CRLF** 换行、RFC 4180 转义。

| source | target | tgt_lng |
| --- | --- | --- |
| Hethereau | 海特洛市 | zh-CN |
| 海特洛市 | Hethereau | en-US |

## 重新生成

```bash
python ../tools/build_nte_glossary.py
```

- 游戏版本：`UNKNOWN - requires extraction from game client`
- 生成时间：`2026-09-27`
