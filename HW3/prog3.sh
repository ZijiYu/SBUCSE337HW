#!/bin/bash

if [ ! -f "$1" ]; then 
    echo "Usage: $0 <data file> <int> <int> <int> ... "
    echo "Missing File"
    exit 1
fi 

data_file="$1"
shift

total_sum=0
row=0
N=0
while IFS=',' read -r -a lines || [[ -n $lines ]]; do
    if [ $row -eq 0 ];then # 第一行
        # 记录数组长度
        N=$((${#lines[@]}-1))
        #echo "Weight Numbers : $N"
        
        # 读取文件第一行，确定有几个分数
        declare -a weights=()

        weight_sum=0
        for (( i=1; i<=$N; i++ )); do
            if [ -n "${!i}" ]; then
                weights[i-1]=${!i}
                ((weight_sum+=${!i}))
            else
                weights[i-1]=1
                ((weight_sum+=1))
            fi
        done
        # echo "weight_sum: $weight_sum"
    else
        sum=0
        id=${lines[0]}
        for ((i=1; i<=$N; i++)); do
            weight=${weights[$((i-1))]:-1}  # 使用默认权重1，如果未设置 语法：${variable:-default}
            ((sum+=${lines[$i]}*$weight))
        done
        total_sum=$(echo "$total_sum + $sum / $weight_sum" | bc -l)
        #echo "Score $(echo "$sum / $weight_sum" | bc -l)"
    fi
    ((row++))
done < "$data_file"

round() {
    # $1 是要四舍五入的数字，$2 是除数
    echo "scale=0; $1 / $2" | bc
}
rounded_result=$(round $total_sum $((row-1)))
# echo "Length of scores:  $((row-1))"
echo "$rounded_result"

