#cau12:
import math
a = float(input("Nhap van toc cua o to luc ban dau:"))
t = a**4 / math.log(5,4)
lam_tron = round(t,2)
print("Thời gian để ô tô đi với vận tốc",a,"dừng lại là:",lam_tron,"giây")