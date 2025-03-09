so = input("Nhập số: ")
i = 0
while so[i:i+1]:
    if so[i] == "0":
        print("không", end=" ")
    elif so[i] == "1": 
        print("một", end=" ")
    elif so[i] == "2": 
        print("hai", end=" ")
    elif so[i] == "3": 
        print("ba", end=" ")
    elif so[i] == "4": 
        print("bốn", end=" ")
    elif so[i] == "5": 
        print("năm", end=" ")
    elif so[i] == "6": 
        print("sáu", end=" ")
    elif so[i] == "7": 
        print("bảy", end=" ")
    elif so[i] == "8": 
        print("tám", end=" ")
    elif so[i] == "9": 
        print("chín", end=" ")
    elif so[i] == '-' or so[i] == '.':
        print('phay', end=' ')
    i += 1