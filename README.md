# Token服务单位经济的消耗口径与毛利分解

本项目整理智能消费与数字服务分析所需的合成业务记录。示例用于检查输入结构和内容身份，不代表新闻中的平台数据或企业事实。`analytics.py`提供JSON输入读取及分区概览；`economics.py`读取订单与调用修订并保留其来源分区身份；通用输入层会返回该分区记录摘要。字段边界见[分析契约](docs/contracts.md)。

使用Python 3.11及标准库。

```sh
python -m unittest discover -s tests -v
python -m compileall -q analytics.py tests
python analytics_cli.py
```

在Linux容器中可通过Dockerfile执行同一套基线检查。
