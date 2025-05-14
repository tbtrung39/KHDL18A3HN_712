def loc_ky_tu_hop_le(s):
    """Loại bỏ ký tự không thuộc tập 0-9, A-F"""
    tap_hop_le = "0123456789ABCDEF"
    s = s.upper()
    return ''.join(c for c in s if c in tap_hop_le)
def xac_dinh_co_so(s):
    """Tìm cơ số nhỏ nhất mà chuỗi có thể biểu diễn được"""
    s = s.upper()
    tap = set(s)
    max_ky_tu = max(tap)
    if max_ky_tu.isdigit():
        co_so = int(max_ky_tu) + 1
    else:
        co_so = ord(max_ky_tu) - ord('A') + 11  
    return max(co_so, 2)  
def chuyen_sang_thap_phan(s, base):
    """Chuyển chuỗi từ hệ bất kỳ (2, 8, 16) sang hệ 10"""
    try:
        return int(s, base)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số {}".format(base)
