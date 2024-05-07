#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <data file> <output file>"
    echo "data file or output file not found"
    exit 1
fi

data_file="$1"
output_file="$2"

# 检查数据文件是否存在
if [ ! -f "$data_file" ]; then
    echo "$data_file not found"
    exit 1
fi

# 初始化一个空的关联数组来存储每列的总和
declare -A col_sums

# 读取数据文件
while IFS=';:,' read -r -a cols || [[ -n "$cols" ]]; do
    for i in "${!cols[@]}"; do
        # 累加每列的值
        ((col_sums[$i]+=${cols[$i]}))
    done
done < "$data_file"

# 写入输出文件
> "$output_file"  # 清空输出文件（如果存在）
for i in "${!col_sums[@]}"; do
    echo "Col $((i + 1)) : ${col_sums[$i]}" >> "$output_file"
done

echo "Output written to $output_file"







