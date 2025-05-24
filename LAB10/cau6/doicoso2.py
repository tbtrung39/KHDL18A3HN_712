def loc_ky_tu(s):
    allowed="0123456789ABCDEF"
    kq="".join(c for c in s.upper() if c in allowed)
    print(kq)
    return kq

def co_so(s):
    allowed="0123456789ABCDEF"
    cs=max((allowed.index(c) for c in s.upper()))+1
    print("Cơ số:",cs)
    return cs

def hop_le(s,cs):
    allowed_sets = {
        2:"01",
        8:"01234567",
        16:"0123456789ABCDEF"
    }
    allowed = allowed_sets.get(cs)
    return all(c in allowed for c in s.upper())

def sang_thap_phan(s,cs):
    if not hop_le(s,cs):
        return f"Lỗi: chuỗi không hợp lệ với cơ số {cs}"
    return int(s,cs)

def tu_co_so_2(s): return sang_thap_phan(s,2)
def tu_co_so_8(s): return sang_thap_phan(s,8)
def tu_co_so_16(s): return sang_thap_phan(s,16)
