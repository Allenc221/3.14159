# 3.14159
Do it good

## 股票数据分享

该仓库提供 `stock_share.py` 脚本，可从 Yahoo Finance 下载指定股票的历史数据并保存为 CSV 文件。

### 安装依赖
```bash
pip install yfinance
```

### 使用示例
```bash
python stock_share.py AAPL MSFT --start 2023-01-01 --end 2023-06-01 --output data.csv
```
运行后将在当前目录生成 `data.csv` 文件。
