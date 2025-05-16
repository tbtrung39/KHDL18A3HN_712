def nhap_so_nguyen():
    so = int(input("Nhập một số nguyên: "))
    return so

def doi_nhi_phan(so):
    return bin(so)[2:]

def doi_bat_phan(so):
    return oct(so)[2:]

def doi_thap_luc_phan(so):
    return hex(so)[2:].upper()
