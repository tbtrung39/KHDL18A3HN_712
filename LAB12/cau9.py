N=[31,28,31,30,31,30,31,31,30,31,30,31]
def ln(n):return n%4==0 and (n%100!=0 or n%400==0)
def snt(m,y):return 29 if m==2 and ln(y) else N[m-1]
def tt(ng,t,y):
  try:
    if not(1<=t<=12 and 1<=ng<=snt(t,y)):raise ValueError("Ngày hoặc tháng sai")
    d=sum(snt(i,y)for i in range(1,t))+ng
    return f"Tuần thứ {(d+6)//7}"
  except Exception as e:return f"Lỗi:{e}"
  finally:print("Xong")

ng=int(input("Ngày:"))
th=int(input("Tháng:"))
nm=int(input("Năm:"))
print(tt(ng,th,nm))