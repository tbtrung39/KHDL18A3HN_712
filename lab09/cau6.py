import random
def hoan_vi_ngau_nhien(n):
  if not isinstance(n, int) or n <= 0:
    return "Vui lòng nhập một số tự nhiên dương."
  lst = list(range(1, n + 1))
  ket_qua = []
  while lst:
    chi_so_ngau_nhien = random.randint(0, len(lst) - 1)
    phan_tu_ngau_nhien = lst.pop(chi_so_ngau_nhien)
    ket_qua.append(phan_tu_ngau_nhien)

  return ket_qua
try:
  n = int(input("Nhập một số tự nhiên n: "))
  hoan_vi = hoan_vi_ngau_nhien(n)
  print(f"Hoán vị ngẫu nhiên của các số từ 1 đến {n} là: {hoan_vi}")
except ValueError:
  print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")