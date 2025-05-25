class KyTuKhongHopLe(Exception):
    pass
class LoiKyTuLienKe(Exception):
    pass
class LoiNhapLapLai(Exception):
    pass
class LoiNhapTrungLap(Exception):
    pass
def kiem_tra_chuoi(s):
    if len(s) != 5:
        raise KyTuKhongHopLe("Chuoi phai gom dung 5 ky tu")
    if not all(char.isalpha() for char in s):
        raise KyTuKhongHopLe("loi ky tu")
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            raise LoiKyTuLienKe("loi nhap lieu")
    for i in range(len(s)-1):
        if s[i]==s[i+1]==s[i+2]== s[i+3]:
            raise LoiNhapLapLai("loi nhap lai")
    from collections import Counter
    dem=Counter(s)
    for char, count in dem.items():
        if count==5:
            raise LoiNhapTrungLap("loi nhap trung lap")
while True:
    try:
        chuoi=input("nhap chuoi gom 5 ky tu chu cai")
        kiem_tra_chuoi(chuoi)
        print("chuoi hop lai")
        break
    except Exception as e:
        print(f"loi:{e}")
