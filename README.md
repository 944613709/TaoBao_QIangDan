# 淘宝自动抢单工具 | Taobao Flash Buy

[English](README_EN.md) | 简体中文

一个基于 Python 的淘宝商品自动抢单工具，使用 PyQt5 构建图形界面，支持定时自动抢购购物车中的商品。

## 功能特点

- 图形化操作界面，使用简单直观
- 支持定时自动抢购功能
- 自动选择购物车中的所有商品
- 语音提示功能，操作过程更清晰
- 自动完成登录、结算、提交订单等流程

## 技术栈

- Python 3.x
- PyQt5 + Qt Designer
- Selenium WebDriver
- pyttsx3 语音合成

## 环境要求

- Python 3.x
- Chrome 浏览器
- ChromeDriver（需要与 Chrome 浏览器版本匹配）
- 必要的 Python 包：
  - PyQt5
  - selenium
  - pyttsx3

## 安装说明

1. 克隆或下载本项目到本地
2. 安装所需的 Python 包：

```bash
pip install PyQt5 selenium pyttsx3
```

3. 下载与您的 Chrome 浏览器版本匹配的 ChromeDriver
4. 将 ChromeDriver 放置在正确的目录下（默认为 D:\python）

## 使用方法

1. 运行 `GuiMain.py` 启动程序
2. 在界面上设置抢购时间

   ![image-20230515232236257](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202305152322361.png)
3. 程序会自动打开淘宝网站并提示登录

   ![image-20230515225439295](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202305152254991.png)
4. 在 15 秒内完成淘宝账号登录
5. 程序会自动跳转到购物车页面
6. 到达设定时间后，程序会自动执行抢购流程

## 注意事项

- 使用前请确保已经将要抢购的商品加入购物车
- 请提前测试 ChromeDriver 是否正常工作
- 登录时需要在规定时间内完成
- 本工具仅供学习研究使用，请勿用于商业用途
- 抢购时请遵守淘宝平台的规则和条款

## 项目结构

```
├── GuiMain.py        # 主程序入口
├── gui.py           # GUI 界面实现
├── gui.ui          # Qt Designer 界面文件
├── chromedriver.exe # Chrome 浏览器驱动
└── README.md       # 项目说明文档
```

## 开源许可

本项目采用 MIT 许可证，详情请见 [LICENSE](LICENSE) 文件。

## 贡献指南

欢迎提交问题反馈和功能建议。如果您想贡献代码：

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 推送到您的分支
5. 创建 Pull Request

## 免责声明

本工具仅供学习和研究使用，使用本工具产生的任何后果由使用者自行承担。请确保您的使用符合淘宝平台的规则和条款。
