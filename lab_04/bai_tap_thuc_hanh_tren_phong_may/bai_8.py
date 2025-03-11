while True:
    n = input("Nhập một ký tự: ")
    if len(n) == 1:  
        print("Mã ASCII của", n, "là:", ord(n))
        break
