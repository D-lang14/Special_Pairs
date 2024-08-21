
# def special_pairs(n: int) -> [[int]]: # type: ignore
    
#     # finding prime numbers 
#     res = []
#     for i in range(n):
#         if i > 1:
#             for j in range(2, i):
#                 if (i%j) == 0:
#                     break
#             else:
#                 res.append(i)

#     # finding special pairs
#     pair = []
#     while res:
#         num = res.pop()
#         diff = n - num
#         if diff in res:
#             pair.append((diff, num))

#     pair.reverse()
#     return pair

# print(special_pairs(18))


n = 100
res = []
for i in range(n):
    if i > 1:
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            res.append(i)
            
print(res)
            
# finding special pairs
pair = []
while res:
    # getting the last element from the list
    num = res.pop()
    diff = n - num
    # check if the difference is in the list
    if diff in res:
        pair.append((diff, num))

# pair.reverse()
print(pair)