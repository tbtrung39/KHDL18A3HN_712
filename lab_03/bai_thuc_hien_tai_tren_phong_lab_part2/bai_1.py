chuoi_container = input("Nhập số container (10 ký tự): ").upper()
chu_cai = "ABCDEFGHJKLMNPQRSTUVWXYZ"
so_tuong_ung = [
    10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 
    28, 29, 30, 31, 32, 34, 35, 36, 37, 38
]
tong_trong_so = 0
vi_tri = 0
for ky_tu in chuoi_container:
    if ky_tu in chu_cai:  
        vi_tri_chu = 0
        while chu_cai[vi_tri_chu] != ky_tu:
            vi_tri_chu += 1
        so_tuong_ung_chu = so_tuong_ung[vi_tri_chu]
    else:  
        so_tuong_ung_chu = int(ky_tu)
    
    trong_so = so_tuong_ung_chu * (2 ** vi_tri)
    tong_trong_so += trong_so
    vi_tri += 1
so_kiem_tra = tong_trong_so % 11
print("Số kiểm tra của container là:", so_kiem_tra)

