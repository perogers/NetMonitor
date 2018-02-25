#!/bin/bash

APP_NAME="monitor.py"
# Host, Ping timeout, Delay between pings
APP="$APP_NAME $1 $2 $3"
LOG="./monitor_runner.log"

active=`ps -ef |grep ${APP_NAME} |grep -v grep`

#echo "active: \"${active}\""

if [[ -z "${active// }" ]]
	then
	START=`date`
	echo "${START} - Not active starting\n" >>$LOG
	nohup python2 ${APP}  1>>${LOG} 2>>&1 &
fi
