#!/bin/bash
# 创建当前文件夹与目标文件夹
SRC_DIR="project"
DEST_DIR="project_backup"

if [ ! -d "$SRC_DIR" ]; then
    echo "$SRC_DIR not found"
    exit 0
fi

# 创建目标目录（如果不存在）
mkdir -p "$DEST_DIR"

# 使用 while 循环和 read 命令读取 find 的输出到数组中
dirs=()
while IFS= read -r dir; do
    dirs+=("$dir")
done < <(find "$SRC_DIR" -type d)

# 遍历目录数组
for dir in "${dirs[@]}"; do
    
    SUB_DIR=${dir/$SRC_DIR/$DEST_DIR}
    mkdir -p "$SUB_DIR"

    # 查找当前目录下的 .c 文件，并保存到数组
    C_FILES=()
    while IFS= read -r file; do
        C_FILES+=("$file")
    done < <(find "$dir" -maxdepth 1 -name "*.c")
    NUM_C_FILES=${#C_FILES[@]}

    echo "Directory: [$dir] has [$NUM_C_FILES] .c files."
    for file in "${C_FILES[@]}"; do
        echo " - $file"
    done

    # 如果 .c 文件数量大于3，则提示用户是否移动这些文件
    if [ $NUM_C_FILES -gt 3 ]; then=
        read -p "Do you want to move these files?(Y/N) " response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            for file in "${C_FILES[@]}"; do
                mv "$file" "${file/$SRC_DIR/$DEST_DIR}" # 使用参数化来修改文件名替换路径并移动文件
            done
        fi
    else
        # 如果 .c 文件数量不大于3，直接移动这些文件
        for file in "${C_FILES[@]}"; do
            mv "$file" "${file/$SRC_DIR/$DEST_DIR}"
        done
    fi
done

echo "Files moved successfully"
