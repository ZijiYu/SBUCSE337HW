#!/bin/bash

# 对文件夹中的所有内容进行操作
# 并且得到一个返回值

if [ "$#" -ne 1 ]; then
    echo "score directory missing"
    exit 1
fi

scores_directory="$1"

if [ ! -d "$scores_directory" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

assign_grade() {
    local score=$1
    if [ "$score" -ge 93 ]; then
        echo "A"
    elif [ "$score" -ge 80 ]; then
        echo "B"
    elif [ "$score" -ge 65 ]; then
        echo "C"
    else
        echo "D"
    fi
}

sum=0

for file in "$scores_directory"/*; do
    sum=0
    id=""
    while IFS=, read -r -a lines || [[ -n ${lines} ]]; do
        if [ ${lines[0]} == "ID" ]; then
            continue
        fi
        id=${lines[0]}
        for((i=1; i<${#lines[@]}; i++)); do
            ((sum+=${lines[$i]}))
        done
    done < "$file"

    percentage=$((sum * 100 / 50))

    grade=$(assign_grade $percentage)
    echo "$id:$grade"

done
        
    
