while True:
    n=input("nhập ký tự: ")
    if len(n)!=1:
        print("chỉ được nhập 1 ký tự")
    else:
        print(ord(n))
        break