import doicoso2

def main():
    chuoi_nhap = input("Nhập chuỗi ký tự: ")
    
    chuoi_loc = doicoso2.loc_ky_tu_hop_le(chuoi_nhap)
    print("Chuỗi hợp lệ sau khi lọc:", chuoi_loc)

    he_co_so = doicoso2.xac_dinh_he_co_so(chuoi_loc)
    if he_co_so == -1:
        print("Không xác định được hệ cơ số.")
    else:
        print(f"Chuỗi biểu diễn theo hệ cơ số {he_co_so}")
        gia_tri_thap_phan = doicoso2.chuyen_sang_thap_phan(chuoi_loc, he_co_so)
        print(f"Giá trị thập phân tương ứng: {gia_tri_thap_phan}")

if __name__ == "__main__":
    main()