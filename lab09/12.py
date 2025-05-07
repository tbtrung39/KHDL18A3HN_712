def tim_ga_cho(tong_con, tong_chan, ga=0, cho=0):
    if ga + cho == tong_con and ga * 2 + cho * 4 == tong_chan:
        return ga, cho
    if ga > tong_con:
        return None
    return tim_ga_cho(tong_con, tong_chan, ga + 1, tong_con - (ga + 1))
ket_qua = tim_ga_cho(36, 100)
if ket_qua:
    print("Số con gà:", ket_qua[0], "Số con chó:", ket_qua[1])
else:
    print("Không tìm được kết quả")
