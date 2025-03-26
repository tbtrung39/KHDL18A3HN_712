#Cach 1:
chuoi = """Trăm năm trong cõi người ta
            Chữ tài chữ mệnh khéo là ghét nhau
            Trải qua một cuộc bể dâu, ta
            Những điều trông thấy mà đau đớn lòng."""
danh_sach = chuoi.split()
tu_don = input("Nhap tu don muon tim: ")
dem = 0
for kt in danh_sach:
    if kt == tu_don:
        dem += 1
print(f"Tu {tu_don} xuat hien {dem} lan trong chuoi") 

#Cach 2:
tk = """Đầu lòng hai ả tố nga,
        Thúy Kiều là chị, em là Thúy Vân.
        Mai cốt cách, tuyết tinh thần,
        Một người một vẻ, mười phân vẹn mười."""
ds = tk.split()
tu_can_tim = input("Nhap tu can tim: ")
count = ds.count(tu_can_tim)
print(f" Tư {tu_can_tim} xuat hien {count} lan trong chuoi")