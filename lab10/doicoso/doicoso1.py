def nhap_so():
    so = int(input("Nhap so nguyen tu ban phim: "))
    print("so da nhap la: " + str(so))
    return so

def chuyen_sang_nhi_phan(so):
    print("so " + str(so) + " o he nhi phan la: " + bin(so)[2:])

def chuyen_sang_bat_phan(so):
    print("so " + str(so) + " o he bat phan la: " + oct(so)[2:])

def chuyen_sang_thap_luc_phan(so):
    print("so " + str(so) + " o he thap luc phan la: " + hex(so)[2:].upper())