import collections
def is_chaotic(str):
    dic = collections.defaultdict(int)
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


