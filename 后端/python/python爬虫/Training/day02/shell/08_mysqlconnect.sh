#!/bin/bash

user="root"
password="123456"

while :
do
    count=`mysqladmin -u$user -p$password status | awk '{print $4}'`
    echo "连接数:$count"
    sleep 2
done










