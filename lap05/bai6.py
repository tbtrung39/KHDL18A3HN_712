chuoi_hex = input("Nhập chuỗi hệ 16: ")
 chu_so_hex = "0123456789ABCDEFabcdef"
 hop_le = True 
 for ky_tu in chuoi_hex:
     if ky_tu not in chu_so_hex:
         hop_le = False
         break 
 if hop_le:
     thap_phan = 0
     luy_thua = 0
     for i in range(len(chuoi_hex) - 1, -1, -1):
         ky_tu = chuoi_hex[i]
         if '0' <= ky_tu <= '9':
             gia_tri = ord(ky_tu) - ord('0')
         else:
             gia_tri = ord(ky_tu.upper()) - ord('A') + 10
         thap_phan += gia_tri * (16 ** luy_thua)
         luy_thua += 1
     print("Giá trị thập phân tương ứng là:", thap_phan)
 else:
     print("Chuỗi nhập vào không phải số hệ 16 hợp lệ.")