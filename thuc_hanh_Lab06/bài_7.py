import random
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:", List_)
if len(List_) >= 3:
    phan_tu_thu_hai_cua_phan_tu_thu_ba = List_[2][1]
    print("Phần tử thứ hai của phần tử thứ ba:", phan_tu_thu_hai_cua_phan_tu_thu_ba)
else:
    print("Danh sách List_ không đủ 3 phần tử.")
do_dai_list_test = len(List_)
print("Độ dài của danh sách List_:", do_dai_list_test)
ngay_ngau_nhien = random.choice(["aaa", "bbb", "ccc"])
gia_tri_ngau_nhien = random.randint(50, 150)
phan_tu_ngau_nhien = [ngay_ngau_nhien, gia_tri_ngau_nhien]
List_.append(phan_tu_ngau_nhien)
print("Danh sách List_ sau khi thêm phần tử ngẫu nhiên:", List_)
tong_sale = sum(phan_tu[1] for phan_tu in List_ if phan_tu[0] in ["tue", "wed", "sat", "sun"])
print("Tổng sale value các ngày thứ hai, thứ ba, thứ bảy, chủ nhật:", tong_sale)