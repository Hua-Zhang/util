#!/bin/bash

port=44407

#如果ifconfig没有预支持
#ifconfig='/sbin/ifconfig'

if [ $# == 1 ]
then
  port=$1
fi

ifconfig | grep "Bcast" | awk '{split($2, a, ":"); print a[2]":""'$port'"}'
#如果ifconfig没有预支持
#$ifconfig | grep "Bcast" | awk '{split($2, a, ":"); print a[2]":""'$port'"}'

python -m SimpleHTTPServer $port
#Python3
#python -m http.server $port
