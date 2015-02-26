#!/bin/bash

date >/tmp/msg
echo "Status message from cronaudcoll" >>/tmp/msg
uname -a >>/tmp/msg
ifconfig eth0 >>/tmp/msg
df -h >>/tmp/msg
who >>/tmp/msg

cat /tmp/msg | mail kmw7339@gmail.com

