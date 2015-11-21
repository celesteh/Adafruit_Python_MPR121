#!/bin/bash

# get the dir of this script
pushd `dirname $0` > /dev/null
program_dir=`pwd`
popd > /dev/null

cd $program_dir

sleep 20


while true
    do

        #touch /tmp/sexbot2

        sleep 5

        git pull
        sleep 5
        echo "starting script"
        sudo /usr/bin/python Talk.py &
        pid=$!

        ./keepAlive.sh $pid &
        alive_pid=$!

        wait $pid
        kill $alive_pid
        
        sleep 1

done
