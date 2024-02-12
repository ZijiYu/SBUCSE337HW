def even(x):
    return x % 2 == 0


def odd(x):
    return x % 2 == 1

def winning_function(nums):
    true_in_func1 = 0
    true_in_func2 = 0
    for num in nums:
        if even(num) == True:
            true_in_func1+=1
        elif odd(num) == True:
            true_in_func2+=1
    if true_in_func2>true_in_func1:
        return "Odd"
    elif true_in_func2<true_in_func1:
        return "Even"
    else:
        return "TIE"
