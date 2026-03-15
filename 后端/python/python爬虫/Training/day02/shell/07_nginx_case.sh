#!/bin/bash

read -p 'nginx(start|stop|restart)' choice

case $choice in
"start")
    sudo /etc/init.d/nginx restart
    ;;
"stop")
    sudo /etc/init.d/nginx stop
    ;;
*)
    echo "Useage(start|stop)"
    ;;
esac









