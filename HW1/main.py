from Q1 import  is_chaotic
from Q2 import is_balanced

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



if __name__=='__main__':
    main()