
def special_pairs(n: int) -> [[int]]: # type: ignore
    
    # find prime numbers 
    res = []
    for i in range(n):
        if i > 1:
            for j in range(2, i):
                if (i%j) == 0:
                    break
            else:
                res.append(i)

    # find special pairs
    pair = []
    while res:
        num = res.pop()
        diff = n - num
        if diff in res:
            pair.append((diff, num))

    pair.reverse()
    return pair

print(special_pairs(18))



    if diff in res:
        pair.append((diff, num))

# pair.reverse()
print(pair)
