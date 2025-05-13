import random
def hoan_vi_ngau_nhien(n):
  if not isinstance(n, int) or n <= 0:
    return "Vui long nhap mot so tu nhien duong."
  lst = list(range(1, n + 1))
  ket_qua = []
  while lst:
    chi_so_ngau_nhien = random.randint(0, len(lst) - 1)
    phan_tu_ngau_nhien = lst.pop(chi_so_ngau_nhien)
    ket_qua.append(phan_tu_ngau_nhien)

  return ket_qua
try:
  n = int(input("Nhap mot so tu nhien n: "))
  hoan_vi = hoan_vi_ngau_nhien(n)
  print(f"Hoan vi ngau nhien cua cac so tu 1 den  {n} la: {hoan_vi}")
except ValueError:
  print("Đau vao khong hop le. Vui long nhap mot so nguyen.")