a =[2,-4,1,9,-3,6,3,-2,6,8]
'''#1
S = 0
for i in a:
    S = S+i
print(S)
#2
list =[]
for j in range(len(a)):
    if a[j]>0:
        list.append(a[j])
print(list)
print(list.count(list))'''
#4
print(max(a))
