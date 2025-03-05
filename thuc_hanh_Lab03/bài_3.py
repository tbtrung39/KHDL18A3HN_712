
n = int(input("Nhập số n: "))
if n < 2:
    nguyen_to = 0
else:
    i = 2 
    while i * i <= n: 
        if n % i == 0:
            nguyen_to = 0
            i = n  
        i += 1  
if nguyen_to == 1:
    print(n, "là số nguyên tố.")
else:
    nho_hon = n - 1
    lon_hon = n + 1
    tim_thay_nho = 0
    while tim_thay_nho == 0:  
        nguyen_to_nho = 1
        i = 2
        while i * i <= nho_hon:
            if nho_hon % i == 0:
                nguyen_to_nho = 0
                i = nho_hon  
            i += 1
        if nguyen_to_nho == 1:
            tim_thay_nho = 1  
        else:
            nho_hon -= 1  
    tim_thay_lon = 0
    while tim_thay_lon == 0:  
        nguyen_to_lon = 1
        i = 2
        while i * i <= lon_hon:
            if lon_hon % i == 0:
                nguyen_to_lon = 0
                i = lon_hon 
            i += 1
        if nguyen_to_lon == 1:
            tim_thay_lon = 1  
        else:
            lon_hon += 1  
    if (n - nho_hon) <= (lon_hon - n):
        gan_nhat = nho_hon
    else:
        gan_nhat = lon_hon
    print(n, "không phải số nguyên tố. Số nguyên tố gần nhất là", gan_nhat)

