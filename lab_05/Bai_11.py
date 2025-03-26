chuoi = input("Nhập chuỗi nhị phân (chỉ gồm 0 và 1): ")  
hop_le = True  

for ky_tu in chuoi:
    if ky_tu != '0' and ky_tu != '1':  
        hop_le = False  
        break  

if hop_le:
    gia_tri_thap_phan = int(chuoi, 2)  
    print(f"Giá trị thập phân của {chuoi} là: {gia_tri_thap_phan}")  
else:
    print("Chuỗi không hợp lệ, vui lòng nhập lại.")  