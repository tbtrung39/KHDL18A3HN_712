from datetime import datetime,timedelta
try:
    ngay_str=input("Nhập ngày(định dạng dd-mm-yyyy):")
    ngay_nhap=datetime.strptime(ngay_str,"%d-%m-%Y")
    ngay_ke_tiep=ngay_nhap+timedelta(days=1)
    print("Ngày kế tiếp la:",ngay_ke_tiep.strftime("%d-%m-%Y"))

except ValueError :
    print("Lỗi: Ngày không hợp lệ hoặc sai định dạng(dd-mm-yyyy).")