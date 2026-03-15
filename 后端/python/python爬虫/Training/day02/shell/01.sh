#!/bin/bash

# echo `expr $1 + $2`

# 方式一:let命令
i=1
let i++ 
echo $i
# 方式二: `expr `
echo `expr $i + 3`
# 方式三: $[]
echo $[i+8]
