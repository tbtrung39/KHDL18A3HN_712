so=list(map(int,input("nhap cac so cach nhau boi dau cach: ").split()))
for i in so:
    assert i%2==0, "tat ca cac so khong phai so chan"
print("tat ca cac so deu la so chan")