N=[31,28,31,30,31,30,31,31,30,31,30,31]
ln=lambda y:y%4==0 and(y%100!=0 or y%400==0)
snt=lambda m,y:29 if m==2 and ln(y) else N[m-1]

def truoc(d,m,y):
  try:
    if not(1<=m<=12 and 1<=d<=snt(m,y)):raise ValueError("Ngày sai")
    d-=1
    if d==0:
      m-=1
      if m==0:m=12;y-=1
      d=snt(m,y)
    return f"{d}-{m}-{y}"
  except Exception as e:return f"Lỗi:{e}"
  finally:print("Xong")

d=int(input("Ngày:"))
m=int(input("Tháng:"))
y=int(input("Năm:"))
print(truoc(d,m,y))