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
