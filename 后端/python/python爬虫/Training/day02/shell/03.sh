#!/bin/sh

c=$[RANDOM%2]

while :
do
	read -p "请猜数字:" y

	if [ $c -eq $y ];then
	    echo "恭喜,猜对了,数字为:$c"
	    exit
	elif [ $c -lt $y ];then
	    echo "猜大了"
	else
	    echo "猜小了"
	fi
done
