class KyTuLoi(Exception):
    pass
class LoiNhapLieu(Exception):
    pass
class LoiLapLai(Exception):
    pass
class LoiTrungLap(Exception):
    pass
while True:
    try:
        s = input("Nhập chuỗi ký tự: ")
        for ch in s:
            if not ch.isalpha():
                raise KyTuLoi("Lỗi ký tự !!!")
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                raise LoiNhapLieu("Lỗi nhập liều !!!")
        for i in range(len(s) - 3):
            if s[i] == s[i+1] == s[i+2] == s[i+3]:
                raise LoiLapLai("Lỗi nhập lặp lại !!!")
        for i in range(len(s) - 4):
            if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
                raise LoiTrungLap("Lỗi nhập trùng lặp!!!")
        print("Chuỗi hợp lệ:", s)
    except KyTuLoi as e:
        print(e)
    except LoiNhapLieu as e:
        print(e)
    except LoiLapLai as e:
        print(e)
    except LoiTrungLap as e:
        print(e)
