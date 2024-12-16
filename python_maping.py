# s = [1,2,3,4]
# res =map(int,s)
# print(list(res))
# print(set(res))

# program 2

'''
a = [1,2,3,4,5]

def duble(val):
    return val*2

res = list(map(duble,a))
print(res)
def cup(val):
    return val*3
res = list(map(cup,a))
print(res)
'''
# program 3

'''
a = [1,2,3,4]
res = list(map(lambda x:x*2,a))
print(res)
'''

#program4
'''
a = [1,2,3,4]
res = list(map(lambda x:x*3,a))
print(res)
'''

# fruits = ['apple','banana','cherry']
# res = map(str.upper,fruits)
# print(list(res))

values = list(map(int, input("Enter multiple values: ").split()))
print("List of integers:", values)

li = list(map(int,input().split()))
print(li)

for i in li:
    print(i)











