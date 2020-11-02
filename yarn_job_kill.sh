#!/bin/bash

source ~/cluster/.bashrc

#current_time=`date +'%Y-%m-%d %H:%M:%S'`
current_time_temp=`date +'%s%N'`
current_time=$[$current_time_temp/1000000]
outfile='./logs/moniter_app_on_yarn.log'

echo "==current time:"$current_time >> $outfile
app_list=`yarn application -list -appStates RUNNING | grep job_name_prefix_`
for app in ${app_list[@]}
do
    # the next sent is check the rela contain
    if  [[ $app =~ "application_"  ]];then
        echo "====active application: "${app} >> $outfile
        app_status=`yarn application -status ${app} | grep Start-Time`
        #echo "========out========"${app_status}
        # regex string
        start_time=$( expr "$app_status" : '.*\([0-9]\{13\}\).*' )

        # other method
        #if [[ $app_status=~ Start-Time\ :\ ([0-9]*)\ Finish-Time ]] ;  then echo ${BASH_REMATCH[1]};  echo ${BASH_REMATCH[2]};  fi
        echo "======application start time: "$start_time >> $outfile
        ((diff_time=$current_time-$start_time))
        threshold=12000000  #200min -> ms
        echo "======application have run time: "$diff_time >> $outfile
        if [ $diff_time -gt $threshold ];then
            result=`yarn application -kill ${app}`
            echo '============yarn application -kill '$app>> $outfile
            #break
        fi
    fi
done
