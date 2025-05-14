def nhap_so():
    n = int(input("Nhap so nguyen: "))
    return n
def doi_nhi_phan(n):
    return bin(n)[2:]  
def doi_bat_phan(n):
    return oct(n)[2:]  
def doi_thap_luc_phan(n):
    return hex(n)[2:].upper()  
