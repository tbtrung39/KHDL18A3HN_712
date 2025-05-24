NGAY_THANG = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def nam_nhuan(n): return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
def so_ngay(t, n): return 29 if t == 2 and nam_nhuan(n) else NGAY_THANG[t - 1]

def tinh_khoang_cach(d1, d2):
    try:
        d1, t1, n1 = map(int, d1.split('-'))
        d2, t2, n2 = map(int, d2.split('-'))
        if not (1 <= t1 <= 12 and 1 <= t2 <= 12): raise ValueError("Tháng sai.")
        if not (1 <= d1 <= so_ngay(t1, n1) and 1 <= d2 <= so_ngay(t2, n2)): raise ValueError("Ngày sai.")
        if (n1, t1, d1) > (n2, t2, d2): d1, t1, n1, d2, t2, n2 = d2, t2, n2, d1, t1, n1
        ngay = d2 - d1 if d2 >= d1 else d2 + so_ngay(t1, n1) - d1; t2 -= d2 < d1
        thang = t2 - t1 if t2 >= t1 else t2 + 12 - t1; n2 -= t2 < t1
        return f"{n2 - n1} năm, {thang} tháng, {ngay} ngày."
    except ValueError as e: return f"Lỗi: {e}"
    except: return "Lỗi không xác định."
    finally: print("Hoàn tất.")

ngay1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
ngay2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
print(tinh_khoang_cach(ngay1, ngay2))