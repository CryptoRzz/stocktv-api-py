# StockTV API Python Client

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)

一个用于对接 **StockTV全球股票、外汇、期货、加密货币API** 的Python客户端库，支持实时行情、历史数据、市场新闻等功能。

## 📦 安装

### 依赖要求

- Python 3.8+
- 通过Telegram联系 [StockTV客服](https://t.me/CryptoRzz) 获取API密钥

### 安装步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/CryptoRzz/stocktv-api-python.git
   cd stocktv-api-python
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 快速开始

### 初始化客户端

```python
from stocktv.stock import StockAPI

# 替换为你的API密钥
API_KEY = "联系客服获取测试key"

# 初始化股票API客户端
stock_client = StockAPI(API_KEY)
```

### 获取印度股票市场列表

```python
response = stock_client.get_stock_list(country_id=14, page_size=10)
print("印度股票市场列表:", response["data"]["records"])
```

### 订阅实时行情（WebSocket）

```python
ws = stock_client.connect_websocket()

# 发送心跳（示例）
ws.send("ping")

# 接收实时数据
while True:
    data = ws.recv()
    print("实时行情:", data)
```

---

## 📚 功能列表

| 模块         | 功能描述                       | 示例方法                       |
| ------------ | ------------------------------ | ------------------------------ |
| **股票**     | 市场列表、指数、K线、IPO日历等 | `get_indices()`, `get_kline()` |
| **外汇**     | 实时汇率、交叉汇率、K线图表    | `get_real_time_rates()`        |
| **期货**     | 期货列表、实时行情、历史数据   | `get_futures_market()`         |
| **加密货币** | 交易对信息、最新价格、K线数据  | `get_klines()`, `get_trades()` |

---

## ⚙️ 配置说明

### 设置API密钥

推荐通过环境变量配置密钥以提升安全性：

```bash
export STOCKTV_API_KEY="联系客服获取测试key"
```

代码中读取环境变量：

```python
import os
api_key = os.getenv("联系客服获取测试key")
```

---

## 🧪 运行测试

```bash
python tests/test_stock.py
```

测试用例覆盖：

- 股票接口基础功能
- 外汇数据解析
- 加密货币实时价格

---

## 🤝 贡献指南

欢迎提交Issue或PR！请遵循以下步骤：

1. Fork项目并创建分支：`git checkout -b feature/your-feature`
2. 提交代码并描述变更
3. 运行测试确保无报错
4. 提交Pull Request至`main`分支

---

## 📜 许可证

本项目采用 [MIT License](LICENSE)。

---

## 📞 联系支持

- 获取API密钥: [联系StockTV客服](https://t.me/CryptoRzz)
- 报告问题: [GitHub Issues](https://github.com/CryptoRzz/stocktv-api-python/issues)