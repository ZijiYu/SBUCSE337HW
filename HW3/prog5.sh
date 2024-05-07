#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "[Error] Missing File" 
    echo "<Usage> $0 <Input.txt> <Directory.txt>"
    exit 1
fi

input=$1
directory=$2

if [ ! -f "$input" ]; then 
    echo "[Error] $input is not a file"
    exit 1
fi

if [ ! -f "$directory" ]; then
    echo "[Error] $directory is not a file"
    exit 1
fi

check() {
    local word=$1
    while IFS= read -r line || [[ -n "$line" ]]; do
        modified_word=$(echo "$word" | tr '[:upper:]' '[:lower:]')
        modified_line=$(echo "$line" | tr '[:upper:]' '[:lower:]')
        if [[ "$modified_word" == $modified_line ]]; then
            return 0
            exit  # Found the word
        fi
    done < "$directory"  # Ensure data is read from directory file
    return 1  # Word not found
}

while IFS=' ,.' read -r -a lines || [[ -n ${lines} ]]; do
    for ((i=0; i<${#lines[@]}; i++)); do

        if [[ "${lines[$i]}" == https://* ]]; then
            while [[ "${lines[$i]}" != */ && $i -lt ${#lines[@]} ]]; do
            # 增加索引，直到找到以 / 结尾的元素或达到数组末尾
                ((i++))
            done
            ((i++))
        else
            if [[ ${#lines[i]} -eq 4 ]]; then
                check "${lines[i],,}"
                res=$?
                if [[ $res -eq 1 ]]; then
                    echo "${lines[i]}"
                fi
            fi
        fi
        # printf " ${lines[$i]},"
    done
done < "$input"  # Ensure data is read from input file