# this question need to use presum
def encode(ct):
    # res [1:]
    # presum = 0
    # strs = []
    # for char in ct:
    #     presum += ord(char)
    #     temp = presum%26+97
    #     strs.append(chr(temp))
    # # first value
    # first = ord(ct[0])+59
    # temp = first%26+97
    # strs[0] = chr(temp)
    #
    # return ''.join(strs)
    plaintext = ""
    res = []
    presum = 0
    for i,char in enumerate(ct):
        if char.isalpha():
            ord_val = ord(char)-97
            if i == 0:
                first = ord(char) + 59
                temp = first%26+97
                plaintext+= chr(temp)
            else:
                original_ord = ((ord_val-presum) % 26)
            presum += original_ord
            plaintext+=(chr (original_ord+97))
        else:
            plaintext += char
    return plaintext
def decode(ct):
    plaintext = ""
    res = []
    presum = 0
    for i,char in enumerate(ct):
        if char.isalpha():
            ord_val = ord(char)-97
            if i == 0:
                original_ord = (ord_val - 59) % 26
            else:
                original_ord = ((ord_val-presum) % 26)
            presum += original_ord
            plaintext+=(chr (original_ord+97))
        else:
            plaintext += char
    return plaintext
# def decode(ct):
#     # 初始化用于存储解密字符的列表和前序字符的累积序数值和
#     decoded_chars = []
#     presum = 0
#
#     # 处理第一个字符
#     first_char = ct[0]
#     first_ord = (ord(first_char) - 97 - 59) % 26 + 97  # 逆转第一个字符的加密过程
#     decoded_chars.append(chr(first_ord))
#     presum += ord(chr(first_ord))  # 更新累积序数值和
#
#     # 处理后续字符
#     for char in ct[1:]:
#         # 逆转加密过程以恢复原始字符
#         temp_ord = (ord(char) - 97 - presum % 26) % 26 + 97
#         decoded_chars.append(chr(temp_ord))
#         presum += ord(chr(temp_ord))  # 使用解密后的字符更新累积序数值和
#
#     # 将解密后的字符列表转换为字符串
#     return ''.join(decoded_chars)