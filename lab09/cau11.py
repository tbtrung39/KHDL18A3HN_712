def giai_thua_kep(n):
  if n == 0 or n == 1:
    return 1
  elif n < 0:
    raise ValueError("Giai thừa kép không xác định cho số âm.")
  else:
    result = 1
    if n % 2 == 0:  
      for i in range(n, 0, -2):
        result *= i
    else:  
      for i in range(n, 0, -2):
        result *= i
    return result
print(f"0!! = {giai_thua_kep(0)}")
print(f"1!! = {giai_thua_kep(1)}")
print(f"2!! = {giai_thua_kep(2)}")
print(f"3!! = {giai_thua_kep(3)}")
print(f"4!! = {giai_thua_kep(4)}")
print(f"5!! = {giai_thua_kep(5)}")