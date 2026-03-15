#!/bin/bash

while :
do
	echo "++++++++++++++++++++++++++++++"
	echo "   Welcome(q to quit)         "
	echo "++++++++++++++++++++++++++++++"

	read -p "请输入一个字符:" char
	if [ ${#char} -ne 1 ];then
		echo "${char}不是一个字符"
	elif [ $char == 'q' ];then
		echo "程序退出"
		exit
	fi

	case $char in
	[a-z]|[A-Z])
		echo "字母"
		;;
	[0-9])
		echo "数字"
		;;
	*)
		echo "其他字符"
		;;
	esac
done
