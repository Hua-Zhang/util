#!/bin/bash

port=44407

if [ $# == 1 ]
then
  port=$1
fi

ifconfig | grep "Bcast" | awk '{split($2, a, ":"); print a[2]":""'$port'"}'
python -m SimpleHTTPServer $port
