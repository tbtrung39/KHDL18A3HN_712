def nhap_so():
    so = int(input("Nhap mot so nguyen:"))
    return so

def nhi_phan(so):
    return bin(so)[2:]

def bat_phan(so):
    return oct(so)[2:]

def thap_luc_phan(so):
    return hex(so)[2:].upper()