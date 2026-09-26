# NTE 数据来源记录 / Sources

生成时间：2026-09-27

## 来源总览

| 来源 | URL | 类型 | 可信度 | 状态 |
| --- | --- | --- | --- | --- |
| 官方中文网站 | https://nte.perfectworld.com | Official | High | 需手动核验 |
| Google Play | https://play.google.com/store/apps/details?id=com.hottagames.nte | Official | High | 需手动核验 |
| NTE-ASIA/NTE-Internal | https://github.com/NTE-ASIA/NTE-Internal | Game Data | Medium | 需判断内容类型 |
| SolicenTEAM/UEExtractor | https://github.com/SolicenTEAM/UEExtractor | Tool | N/A | 工具仓库 |
| interactivemap.app NTE DB | https://interactivemap.app/neverness-to-everness/database/en/ | Third-party DB | Medium | 需手动核验 |
| thegameswiki NTE | https://thegameswiki.com/nte/wiki/localization | Wiki | Medium | 需手动核验 |
| 游戏客户端 .pak/.locres | N/A | Game Data | Highest | 需本地提取 |

## 游戏客户端本地化路径（Unreal Engine）

```
HT/Content/Localization/
  Game/Game.locres
  UI/UI.locres
```

提取工具：UEExtractor（SolicenTEAM）、repak、UnrealPak

## 当前已确认术语

| source | target | tgt_lng | 来源 | 可信度 |
| --- | --- | --- | --- | --- |
| Neverness to Everness | 异环 | zh-CN | Official | High |
| NTE | 异环 | zh-CN | Official | High |
| Hethereau | 海特洛市 | zh-CN | Official | High |
| Eibon | 伊波恩 | zh-CN | Official | High |
| Anomaly Hunter | 异象猎人 | zh-CN | Official | High |
| Anomaly | 异象 | zh-CN | Official (derived) | High |

## 语言支持确认状态

| 语言代码 | 确认状态 | 备注 |
| --- | --- | --- |
| zh-CN | 已确认 | 游戏开发语言 |
| en-US | 已确认 | 英文名 Neverness to Everness |
| zh-TW | 待确认 | 需游戏客户端或官方商店验证 |
| ja-JP | 待确认 | 需游戏客户端或官方商店验证 |
| ko-KR | 待确认 | 需游戏客户端或官方商店验证 |
| de-DE | 待确认 | 需游戏客户端或官方商店验证 |
| fr-FR | 待确认 | 需游戏客户端或官方商店验证 |
| es-ES | 待确认 | 需游戏客户端或官方商店验证 |
| ru-RU | 待确认 | 需游戏客户端或官方商店验证 |
