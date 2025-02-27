# onebot_transport_shit
全自动搬屎！
<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.10.14%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

</div>
让 AI 学会搬史, 搬史进入新时代! 全自动搬史!

## 📢 公告: 注意 当前项目正在重构中

由于意料之外的热度, 本项目已经不适合直接使用(让bot转发未经筛选的, 不可信任来源的消息过于危险, 这不仅会导致您的bot被封禁, 也可能导致群聊被封禁, 面对传播谣言等风险)

本项目正在重构中, 每完成一个目标将会更新:

- [ ] 建立评价机制, 只有满足一定评价条件的消息才会被转发(在此之前, 不建议使用, 除非来源可以信任)
- [ ] 史的保存, 由于史的来源的不确定性, 需要保存并去重, 对于少量消息本地缓存是不错的策略, 对于大量消息, 就应当使用数据库或服务器中心化保存
- [ ] 史的自动评价, 我们会训练一个模型来自动评价史的类别与等级, 将来会开放给大家免费使用

本项目为公益项目, 不接受任何赞助, 所有服务均为免费提供, 所有付费服务与广告都是骗人的, 请不要相信并向作者报告
## ✨ 功能

- 🚫 自动从指定的群聊(推荐加入 1032915502, 共建搬史中心), 转发聊天记录(史)到其他指定的群聊(详见设置)

## 🛠️ 使用方法

1. 加入天天发史的群聊
2. 通过PYTHON运行shit.py，修改生成的id.json,set.json和bot的有关设置
3. 再次通过PYTHON运行shit.py
4. bot 开始全自动搬史!

## 👥 贡献指南

欢迎通过以下方式参与项目：

- 🐛 提交 Issue 报告问题
- 💡 提出新功能建议
- 🔧 提交 Pull Request 改进代码

思路来自[Astrbot Sowing_discord 模块 - 搬史插件](https://github.com/anka-afk/astrbot_sowing_discord)
