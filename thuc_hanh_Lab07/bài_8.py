A=set(input('nhập các tập hợp của A:').split(","))
tap_hop_moi=set()
for phan_tu in A:
    phan_tu=phan_tu.strip()
    if phan_tu.replace(".","",1).isdigit():
        phan_tu=float(phan_tu) if"." in phan_tu else int(phan_tu)
    tap_hop_moi.add(phan_tu)
so_nguyen={x for x in tap_hop_moi if type(x) == int}
so_thuc={x for x in tap_hop_moi if type(x) == float }
chuoi_ky_tu={x for x in tap_hop_moi if type(x) == str}
print("Số nguyên:",len(so_nguyen))
print("Số thực:",len(so_thuc))
print("Chuỗi ký tự:",len(chuoi_ky_tu))      