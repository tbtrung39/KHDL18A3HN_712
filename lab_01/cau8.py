a=list(map(float,input("nhập tọa độ điểm A: ").split())) 
b=list(map(float,input("nhập tọa độ điểm B: ").split())) 
c=list(map(float,input("nhập tọa độ điểm C: ").split()))
x=round((a[0]+b[0]+c[0])/3,2) 
y=round((a[0]+b[0]+c[0])/3,2) 
g=(x,y)
print("trọng tâm của tam giác có 3 đỉnh A,B,C là",g)