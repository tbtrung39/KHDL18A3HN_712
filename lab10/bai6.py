import doicoso2

def main():
    chuoi_nhap = input("Nhap chuoi ky tu: ")
    
    chuoi_loc = doicoso2.loc_ky_tu_hop_le(chuoi_nhap)
    print("Chuoi hop le sau khi loc:", chuoi_loc)

    he_co_so = doicoso2.xac_dinh_he_co_so(chuoi_loc)
    if he_co_so == -1:
        print("Khong xac dinh duoc he co so.")
    else:
        print(f"Chuoi bieu dien theo he co so {he_co_so}")
        gia_tri_thap_phan = doicoso2.chuyen_sang_thap_phan(chuoi_loc, he_co_so)
        print(f"Gia tri thap phan tuong ung: {gia_tri_thap_phan}")

if __name__ == "__main__":
    main()