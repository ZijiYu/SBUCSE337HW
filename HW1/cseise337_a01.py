# Student Name: Ziji.Yu
# Student ID: 115405914
from functools import wraps
from collections import defaultdict

# Question 1: Chaotic Strings
def is_chaotic(str):
    dic = defaultdict(int)
    for char in str:
        dic[char]+=1
    # if all value of dict is different so the string is chaotic
    res = set()
    for item in dic:
        if dic[item] not in res:
            res.add(dic[item])
        else:
            return "ELMA"
    return "TOHRU"

# Question 2: Balanced Brackets
def is_balanced(s):
    dic = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for item in s:
        if item in dic:
            stack.append(item)
        elif stack and dic[stack[-1]] == item:
            stack.pop()
        else:
            return False
    return len(stack) == 0

# Question 3: Functional Programming
# Given Functions:
def _counterTure(func):
    @wraps(func) # to keep the inner function of the even and odd
    def wrapper(nums):# _counterTure will change the even and odd to wrapper's inner function
        count = 0
        for num in nums:
            if func(num) == True:
                count +=1
        return count
    return wrapper # that will return the output of function wrapper

@_counterTure
def even(x):
    return x % 2 == 0

@_counterTure
def odd(x):
    return x % 2 == 1

def winning_function(nums,func1,func2):
    true_in_func1 = func1(nums)
    true_in_func2 = func2(nums)
    if true_in_func2>true_in_func1:
        return func2.__name__
    elif true_in_func2<true_in_func1:
        return func1.__name__
    else:
        return "TIE"

# Question 4: Representing Filesystems
class FS_Item:
    def __init__(self, name):
        self.name = name

class Folder(FS_Item):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class File(FS_Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

def load_fs(ls_output):
    with open(ls_output, 'r') as f:
        lines = f.readlines()

    root = None
    current_path = []
    folders = defaultdict(Folder)

    for line in lines:
        line = line.strip()
        if line.endswith(':'):  # New directory
            dir_path = line[:-1]  # Remove ‘:’
            folder_name = dir_path.split('/')[-1]  # Get the last part as folder name
            folder = Folder(folder_name)
            folders[dir_path] = folder

            if not root:  # First directory is the root
                root = folder
            else:  # Add to parent folder
                parent_path = '/'.join(dir_path.split('/')[:-1])
                if parent_path in folders:
                    folders[parent_path].add_item(folder)

            current_path = dir_path
        elif 'total' in line or not line:
            continue  # Skip total line and empty lines
        else:  # Files
            parts = line.split()
            file_name = parts[-1]
            file_size = int(parts[-5])
            file = File(file_name, file_size)
            folders[current_path].add_item(file)

    return root
# Question 5:  Decoding
def encode(ct):

    plaintext = ""
    presum = 0
    for i,char in enumerate(ct):
        if char.isalpha():
            if i == 0:
                first = ord(char) + 59
                presum += ord(char)
                temp = first%26+97
                plaintext+= chr(temp)
            else:
                presum += ord(char)
                original_ord = presum%26+97
                plaintext+=chr(original_ord)
        else:
            plaintext += char
    return plaintext

def find_original(final,begin,end):
    for index in range(begin,end):
        if index%26== final:
            return index
    return final

def decode(ct):
    plaintext = ""
    presum = 0
    begin,end= ord('a'),ord('z')
    for i,char in enumerate(ct):
        if char.isalpha():
            ord_val = ord(char)-97
            # for the first letter
            if i == 0:
                original_ord = find_original(ord_val,begin+59,end+59)-59
                presum = find_original(ord_val,begin,end)+97
            else:
                original_ord = find_original(ord_val,begin+presum,end+presum)-presum
                presum += original_ord
            plaintext+=(chr (original_ord))
        else:
            plaintext += char
    return plaintext

# Test Cases:

def print_fs(item, level=0):
    indent = '    ' * level  # use four space as indent
    if isinstance(item, Folder):
        print(f"{indent}Folder: {item.name}")
        for child_item in item.items:
            print_fs(child_item, level + 1)  # use recursion for each child
    elif isinstance(item, File):
        print(f"{indent}File: {item.name} | Size: {item.size} bytes")


def main():
    print("----Q1: is_chaotic()----")
    print(is_chaotic("abbccc"))
    print(is_chaotic('abcc'))
    print(is_chaotic('azz'))


    print("----Q2: is_balanced()----")
    print(is_balanced("{[()]}"))
    print(is_balanced("{[(])}"))
    print(is_balanced("{{[[(())]]}}"))

    print("----Q3: is_balanced()----")
    arr = [2,3,4,5,6,8]
    print(winning_function(arr,even,odd))
    arr1 = [0,1]
    print(winning_function(arr1, even, odd))



    print("----Q4: load_fs()----")
    print_fs(load_fs("lsoutput.txt"))

    
    print("----Q5: decode()----")
    test1 = encode("i am here now")
    test2 = encode("this is a test")
    test3 = encode("secret")
    print(test1)
    print(test2)
    print(test3)
    print("decode",decode(test1))
    print("decode", decode(test2))
    print("decode", decode(test3))




if __name__=='__main__':
    main()



