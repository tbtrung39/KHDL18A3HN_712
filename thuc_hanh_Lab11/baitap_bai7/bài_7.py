import os
def doc_file_so_nguyen(ten_file):
    with open(ten_file, 'r') as f:
        noi_dung = f.read()
        return list(map(int, noi_dung.split()))
def ghi_file(ten_file, danh_sach):
    with open(ten_file, 'w') as f:
        for so in danh_sach:
            f.write(f"{so} ")
ds_m = os.path.join("baitap_bai7", "m_nums.txt")
ds_n = os.path.join("baitap_bai7", "n_num.txt")
m_list = doc_file_so_nguyen(ds_m)
n_list = doc_file_so_nguyen(ds_n)
so_chung = sorted(set(m_list) & set(n_list))
duong_dan = os.path.join("baitap_bai7", "so_chung.txt")
ghi_file(duong_dan, so_chung)
with open(duong_dan, 'r') as f:
    print("Các số có mặt ở cả 2 file là:")
    print(f.read())
