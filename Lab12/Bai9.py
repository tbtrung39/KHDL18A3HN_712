from datetime import datetime
thu_trong_tuan={
    0: "Thu Hai",
    1: "Thu Ba",
    2: "Thu Tu",
    3: "Thu Nam",
    4: "Thu Sau",
    5: "Thu Bay",
    6: "Chu Nhat"
}
ngay_str=input("Nhap (dd-mm-yyyy):")
try:
    ngay=datetime.strptime(ngay_str, "%d-%m-%Y")
    print("Ngay do la:", thu_trong_tuan[ngay.weekday()])
except ValueError:
    print("Khong hop le!")