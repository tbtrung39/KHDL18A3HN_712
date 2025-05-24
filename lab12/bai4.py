try:
    ten_tep_doc = input("Nhap ten file doc: ")
    ten_tep_ghi = input("Nhap ten file ghi: ")
    
    with open(ten_tep_doc, 'r', encoding='utf-8') as file_in:
        noi_dung = file_in.read()

    with open(ten_tep_ghi, 'w', encoding='utf-8') as file_out:
        file_out.write(noi_dung)

    print("Ghi du lieu thanh cong.")
except FileNotFoundError:
    print("Khong tim thay tap tin nguon.")
except IOError:
    print("Loi doc/ghi tap tin.")
except Exception as e:
    print("Loi khac:", e)
finally:
    print("Ket thuc chuong trinh va dong tep.")