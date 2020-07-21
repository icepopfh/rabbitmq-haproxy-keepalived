#!/bin/bash
count = `ps -aux | grep -v grep | grep haproxy | wc -l`
if [ $count > 0 ]; then
    exit 0
else
    killall keepalived
fi