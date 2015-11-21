#!/bin/bash

dur=65
sleep_time=$dur
alive=/tmp/sexbot2

sudo rm $alive

sleep $sleep_time

while true
    do

        if [ ! -f $alive ]; then
            echo "File not found! - Talk.py has not checked in and must be hung"
            sudo kill $1
            exit 0
        else

            sudo rm $alive
        fi

        sleep $sleep_time
        sleep_time=$(( $dur * 2 ))
        # the first trip through the loop is fast to catch start-up errors

done
