# myConnectSQL
a very lightweight and easy mysql client.

## Introduce
基于Python + MySQLdb 库显示的非常简单的mysql客户端。可以使用其连接上mysql server并执行对应的sql。

## Example
``` bash
python myConnectSQL.py 127.0.0.1 63751 root root wsms "SELECT * FROM test LIMIT 10"
```

## What For
线上有些机器没有安装mysql客户端,导致程序经常由于白名单的问题没办法正常连接。使用该脚本可以用于测试mysql连接。
python 以及 mySQLdb 在我们的服务器都是预装好的。
