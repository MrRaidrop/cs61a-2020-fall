def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2) 20
    >>> f(lambda x: x - 7) 13
    >>> f(lambda x: x > 5) True
    """
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f


def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for i in s:
        key = fn(i)
        if key  not in grouped:
            grouped[key]=[i]
        else:
            grouped[key] = grouped[key]+[i]
    return grouped


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    flag=0
    for i in s :
        if i==x:
            flag+=1
    for i in range(flag):
        s.append(el)
    return



def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for i in iterable:
        if fn(i):
            yield i


def sequence(start, step):
    while True:
        yield start
        start += step
a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...


def merge(a, b):
    """
    >>> def sequence(start, step):
            while True: yield start
                start += step
        a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
        b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>>
    >>>
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    #error occur when the num reach to about 1000
    #this is really stupid
    def remove_same(t):
        flag=0
        for i in range(1,len(t)):
            if t[i-1]==t[i]:
                t.insert(0,t.pop(i-1))
                flag+=1
        t[0:flag]=[]
        return t
    c=20 
    def helper(a,b,c):
        cache=[next(a) for _ in range(c*20)]+[next(b) for _ in range(c*20)]
        cache.sort()
        result=remove_same(cache)
        return result
    cache=helper(a,b,c)
    while c>10:
        yield from cache
        cache=helper(a,b,c)







    


        
