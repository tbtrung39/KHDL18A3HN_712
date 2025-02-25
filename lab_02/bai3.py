thu = int(input("Nhap thu trong tuan(1-7): "))
if thu < 1 or thu > 7:
    if thu == 1:
        print("1. Sunday")
    elif thu == 2:
        print("2. Monday")
    elif thu == 3:
        print("3. Tuesday")
    elif thu == 4:
        print("4. Wednesday")
    elif thu == 5:
        print("5. Thursday")
    elif thu == 6:
        print("6. Friday")
    else:
        print("7. Saturday")
else:
    print("Vui long nhap tu 1 den 7")