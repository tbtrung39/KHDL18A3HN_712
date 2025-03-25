s1 = input("Nhap chuoi thu nhat: ")
s2 = input("Nhap chuoi thu hai: ")

chuoi_con = ""  

for i in range(len(s1)):  
    for j in range(i, len(s1)):  
        sub = s1[i:j + 1]  
        if sub in s2 and len(sub) > len(chuoi_con):  
            chuoi_con = sub  

print(f"Chuoi con chung dai nhat: '{chuoi_con}'")
