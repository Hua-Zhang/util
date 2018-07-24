#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime, timedelta
import numpy as np

HADOOP = '/home/user/hadoop-current/bin/hadoop'

def dir_exist(path):
    '''
    判断hadoop路径是否存在

    @return:
    ------------
    存在    True
    不存在  False
    '''
    for item in path.strip().split(" "):
        res = os.system(HADOOP + ' fs -test -e ' + item)
        if res == 0:
            return True
        else:
            return False
            
def main():
    print ("Start map-reduce task")

    input_path = '/path/to/input_data/*'
    print (input_path)
    output_path = '/path/to/output_data/'

    rm_cmd = '/home/user/hadoop-current/bin/hadoop fs -rm -r %s' %(output_path)
    print (rm_cmd)
    os.system(rm_cmd)

    hadoop = '/home/user/hadoop-current/bin/hadoop'
    streaming = "jar /home/user/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.5.2.jar"

    cmd = '%s %s ' \
    ' -D mapred.job.priority=VERY_HIGH' \
    ' -D mapred.reduce.tasks=1' \
    ' -D mapred.map.tasks=500' \
    ' -D mapreduce.job.queuename=root.data_analysis.default' \
    ' -file mapper.py' \
    ' -file reducer.py' \
    ' -input %s' \
    ' -output %s' \
    ' -mapper "python mapper.py"' \
    ' -reducer "python reducer.py" '%(hadoop, streaming, input_path, output_path)

    os.system(cmd)
    
    output_flag = dir_exist(output_path)
    if output_flag == False:
        print ("Hadoop output_path doesn't exist!")
        return

    print ("Finish map-reduce task")

    try:
        cmd = HADOOP + " fs -get " + output_path + " ./output_data/"
        print (cmd)
        os.system(cmd)
    except:
        print ("Exception occurs when get output result!")

if __name__ == "__main__":
    main()
