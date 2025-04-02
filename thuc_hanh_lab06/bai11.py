import random
A=list(map(int,input("nhập danh sách các số nguyên: ").split()))
B=[x for x in A if x%3==0 and x%5!=0]
print(f"danh sách B: {B}")
C=[x**2 for x in A]
print(f"danh sách C{C}")
D=[]
list=[x for x in A if x%3==0]
while len(D)<len(list):
    index=random.randint(0, len(list)-1)
    i=list[index]
    if i not in D:
        D.append(i)
print(f"danh sách D: {D}")