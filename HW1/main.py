from Q1 import  is_chaotic
from Q2 import is_balanced
from Q3 import winning_function,odd,even
from Q4 import load_fs
from Q4 import File,Folder
from Q5 import encode,decode

def print_fs(item, level=0):
    indent = '    ' * level  # 使用四个空格作为缩进单位
    if isinstance(item, Folder):
        print(f"{indent}Folder: {item.name}")
        for child_item in item.items:
            print_fs(child_item, level + 1)  # 对于每个子项递归调用print_fs
    elif isinstance(item, File):
        print(f"{indent}File: {item.name}, Size: {item.size} bytes")


def main():
    print("----Q1: is_chaotic()----")
    print(is_chaotic("aabbcd"))
    print(is_chaotic('aaaabbbccd'))
    print(is_chaotic('abaacccdee'))


    print("----Q2: is_balanced()----")
    print(is_balanced("{[()]}"))
    print(is_balanced("{[(])}"))
    print(is_balanced("{{[[(())]]}}"))


    print("----Q3: is_balanced()----")
    arr = [2,3,4,5,6,8]
    print(winning_function(arr))


    print("----Q4: load_fs()----")
    print_fs(load_fs("lsoutput.txt"))
    print("----Q5: decode()----")
    test1 = encode("i am here now")
    test2 = encode("this is a test")
    test3 = encode("secret")
    print("decode",decode(test1))
    print("decode", decode(test2))
    print("decode", decode(test3))




if __name__=='__main__':
    main()