n=input("nhap chuoi: ")
s=""
for i in n:
    if "a"<=i<="f" or "A"<=i<="F" or "0"<=i<="9":
        s+=i
bin=int(s,2)
print(bin)