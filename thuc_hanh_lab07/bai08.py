A = [34, 22, 63, "T1", "Max", "Uneti", -10]
songuyen = 0
sothuc = 0
chuoikytu = 0
for i in A:
    if isinstance(i,int):
        songuyen+=1
    elif isinstance(i,float):
        sothuc+=1
    elif isinstance(i,str):
        chuoikytu+=1
print("So nguyen la: ",songuyen)
print("So thuc la: ",sothuc)
print("Chuoi ky tu la: ",chuoikytu)