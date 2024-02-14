from functools import wraps
def _counterTure(func):
    @wraps(func)
    def wrapper(nums):
        count = 0
        for num in nums:
            if func(num) == True:
                count +=1
        return count
    return wrapper

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