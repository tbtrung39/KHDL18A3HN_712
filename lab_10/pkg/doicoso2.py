def loc_ky_tu(s):
    return ''.join(c for c in s if c.upper() in "0123456789ABCDEF")

def co_so_nao(s):
    s = s.upper()
    if all(c in "01" for c in s):
        return 2
    elif all(c in "01234567" for c in s):
        return 8
    elif all(c in "0123456789ABCDEF" for c in s):
        return 16
    return "Không xác định"

def bin_to_dec(s):
    return int(s, 2)

def oct_to_dec(s):
    return int(s, 8)

def hex_to_dec(s):
    return int(s, 16)