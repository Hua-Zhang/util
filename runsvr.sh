#!/bin/bash
while [ 1 ]
do
    for i in $(seq 9001 9001)
    do
        pid=$(pgrep -f "./bin/topic_analysis_svr $i")
        if [ "$pid" = "" ]
        then
            timestamp=`date +%F-%T`
            echo -n $timestamp" Restarting topicAnalysis Server $i..."
            # logging method info
            ./bin/topic_analysis_svr $i ../model/ ../data/stop_words_all.txt ../data/tag_tree_2.0/ &
            echo  " new pid: "`pgrep -f "./bin/topic_analysis_svr $i"`
        fi
    done
    sleep 60
done
