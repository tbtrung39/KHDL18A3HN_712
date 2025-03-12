bang_doi= {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18,
    'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27,
    'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36,
    'Y': 37, 'Z': 38  }


container = input("Nhap ma container (10 ky tu): ").upper()

tong_trong_so = 0
for i in range(10):
    if i < 4:  
        gia_tri = bang_doi[container[i]]
    else:  
        gia_tri = int(container[i])
    
    trong_so = gia_tri * (2 ** i)
    print(f"w{i} = {gia_tri} x 2^{i} = {trong_so}")
    tong_trong_so += trong_so

so_kiem_tra = tong_trong_so % 11

print(f"Tong trong so: {tong_trong_so}")
print(f"So kiem tra = {tong_trong_so} : 11 du {so_kiem_tra}")
print(f"Vay so kiem tra cua ma container {container} la {so_kiem_tra}")