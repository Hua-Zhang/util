#!/bin/sh
# numpy默认开启多核，影响并行性能
# 添加环境变量即可解决
#

date "+%Y-%m-%d %H:%M:%S"
echo 'starting server'
export OMP_NUM_THREADS=1
# 这里指定numpy开启核数
python=/home/appops/bin/python3
nohup $python extract_server.py -p 9201 -f server.conf 2>&1 > app.log &
nohup $python extract_server.py -p 9202 -f server.conf 2>&1 > app.log &
nohup $python extract_server.py -p 9203 -f server.conf 2>&1 > app.log &
nohup $python extract_server.py -p 9204 -f server.conf 2>&1 > app.log &
