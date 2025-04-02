import random
A=list(map(int,input("nhap sanh sach cac so nguyen: ").split()))
B=[x for x in A if x%3==0 and x%5!=0]
print(f"danh sach B: {B}")
C=[x**2 for x in A]
print(f"danh sach C{C}")
D=[]
list=[x for x in A if x%3==0]
while len(D)<len(list):
    index=random.randint(0, len(list)-1)
    i=list[index]
    if i not in D:
        D.append(i)
print(f"danh sach D: {D}")