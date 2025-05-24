import csv
from libs.xu_ly_thong_tin_nhanvien import nhap_danh_sach, tinh_toan_thong_tin, in_bang, sap_xep

def tai_file():
    """Tải dữ liệu từ file CSV."""
    duong_dan = input("Nhập đường dẫn file để tải dữ liệu (bỏ trống nếu không có): ").strip()
    if not duong_dan:
        return []
    try:
        with open(duong_dan, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            ds = []
            for row in reader:
                # Chuyển kiểu dữ liệu về số nếu cần
                row['hsl'] = float(row['hsl'])
                row['luong'] = float(row['luong'])
                row['phu_cap'] = float(row['phu_cap'])
                row['thuc_linh'] = float(row['thuc_linh'])
                ds.append(row)
            return ds
    except FileNotFoundError:
        print(f"Không tìm thấy file tại {duong_dan}. Bắt đầu với danh sách rỗng.")
    except Exception as e:
        print(f"Lỗi khi tải file: {e}")
    return []


def luu_file(ds):
    """Lưu danh sách vào file CSV."""
    duong_dan = input("Nhập đường dẫn file để lưu (ví dụ: files/ds_nhanvien.csv): ").strip()
    try:
        with open(duong_dan, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["ma_nv", "ten_nv", "chuc_vu", "hsl", "luong", "phu_cap", "thuc_linh"])
            writer.writeheader()
            for nv in ds:
                writer.writerow(nv)
        print(f"Danh sách đã được lưu vào {duong_dan}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def main():
    ds = tai_file()  # Tải dữ liệu khi khởi động chương trình
    while True:
        print("\nQuản lý nhân viên:")
        print("1. Nhập danh sách nhân viên")
        print("2. Tính toán Lương, Phụ cấp, Thực lĩnh")
        print("3. In danh sách nhân viên")
        print("4. Sắp xếp theo Thực lĩnh và in danh sách")
        print("5. Lưu danh sách vào file")
        print("0. Thoát")
        chon = input("Chọn chức năng: ").strip()
        
        if chon == "1":
            ds += nhap_danh_sach()
        elif chon == "2":
            tinh_toan_thong_tin(ds)
        elif chon == "3":
            in_bang(ds)
        elif chon == "4":
            ds = sap_xep(ds)
            in_bang(ds)
        elif chon == "5":
            luu_file(ds)
        elif chon == "0":
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()