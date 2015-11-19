#!/bin/bash

# get the dir of this script
pushd `dirname $0` > /dev/null
program_dir=`pwd`
popd > /dev/null

cd $program_dir

sleep 20


while true
    do

        touch /tmp/sexbot2

        sleep 10

        echo "starting script"
        sudo /usr/bin/python Talk.py

        sleep 1

done
