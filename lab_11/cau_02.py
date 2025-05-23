def sap_xep_tang_dan(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        dong = file.readline()
        cac_chuoi_so = dong.strip().split()
        danh_sach_so = [int(so) for so in cac_chuoi_so]
        danh_sach_so.sort()

    with open(output_file, 'w', encoding='utf-8') as file:
        cac_so_da_sap = ' '.join(str(so) for so in danh_sach_so)
        file.write(cac_so_da_sap)

sap_xep_tang_dan('Inp.txt', 'out.dat')

