ds=[]
def nhap():
  while 1:
    try:
      u=input("User:")
      if not u or any(not(c.isalnum())for c in u):raise ValueError("Sai")
      ds.append(u+"@companyname.com")
      print("Lưu:",ds[-1])
      break
    except Exception as e:
      print("Lỗi:",e)

nhap()
print(ds)