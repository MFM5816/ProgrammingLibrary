#!/bin/bash

for filename in `ls /etc/*.conf`
do
    md5sum $filename >> /home/tarena/shell/md5_2.txt
done
