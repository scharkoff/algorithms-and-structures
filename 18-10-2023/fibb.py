def fun(n):
    res = [0, 0, 1]
    for i in range(3, n):
        res.append((res[i-2] + res[i-1]))
    return res

print(fun(10))
        

