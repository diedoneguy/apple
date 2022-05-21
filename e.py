#psevdocod
# f  = 10
# r = 10.5
# j = 13.7
# def game(f,r,j):
#     if r > j:
#         print('r > j')
#     elif r < j:
#         print('r < j')
#     else:
#         print('r == j')
# print(game(r,f,j))

# A = 4
# B = 7
# def love(A,B):
#     if A % 2 == 0:
#         print('Число четное')
#     elif A % 2 != 0 and A > 4:
#         print('Число простое')
# print(love(A,B))

#secondteam
# a = [1,2,2,1,6,4,7,8,6,5]
# b=[2,6,7,8]
# a.sort()
# print(a)
# b.sort()
# print(b)



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
op = []
def pre(a):
    for i in a:
        if i > 5:
            op.append(i)
    return op
print(pre(a))

# i = 0
# while i < 300:
#     i +=2
#     print(i)
#     if i == 254:
#         break

