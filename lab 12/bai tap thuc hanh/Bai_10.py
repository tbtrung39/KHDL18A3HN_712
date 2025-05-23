from datetime import datetime

date_str1=input("Nhập ngày thứ nhất(dd-mm-yyyy):")
date_str2=input("Nhập ngày thứ hai(dd-mm-yyyy):")
date1=datetime.strptime(date_str1,"%d-%m-%Y")
date2=datetime.strptime(date_str2,"%d-%m-%Y")

so_ngay_cach_nhau=abs((date2-date1).days)

nam=so_ngay_cach_nhau // 365
ngay_con_lai=so_ngay_cach_nhau % 365
thang=ngay_con_lai // 30
ngay=ngay_con_lai % 30
print(f"Hai ngày cách nhau khoảng:{nam} năm,{thang} tháng,{ngay} ngày.")