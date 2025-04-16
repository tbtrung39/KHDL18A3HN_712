#Bai17
import functools
def tong_so_chan(lst):
    so_chan = filter(lambda m: m % 2 == 0, lst)
    tong = functools.reduce(lambda m, n: m + n, so_chan)
    return tong
a = int(input("Nhap so nguyen: "))
lst = []
for i in range(1, a + 1):
    lst.append(i)
tong_chan = tong_so_chan(lst)
print("Tong cua cac so chan tu 1 den", a, "la:", tong_chan)