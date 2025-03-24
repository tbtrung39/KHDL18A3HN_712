# cau 13
A = "111"
B = "120"
dang_thuc_dung = False
do_dai_A = len(A)
do_dai_B = len(B)
for vi_tri_1 in range(1, do_dai_A):  
    for vi_tri_2 in range(vi_tri_1 + 1, do_dai_A):  
        so_A1 = A[:vi_tri_1]
        so_A2 = A[vi_tri_1:vi_tri_2]
        for vi_tri_3 in range(1, do_dai_B):  
            for vi_tri_4 in range(vi_tri_3 + 1, do_dai_B):  
                so_B1 = B[:vi_tri_3]
                so_B2 = B[vi_tri_3:vi_tri_4]
                if (so_A1[0] != '0' or so_A1 == "0") and \
                   (so_A2[0] != '0' or so_A2 == "0") and \
                   (so_B1[0] != '0' or so_B1 == "0") and \
                   (so_B2[0] != '0' or so_B2 == "0"):
                    if int(so_A1) + int(so_A2) == int(so_B1) + int(so_B2):
                        print(so_A1, "+", so_A2, "=", so_B1, "+", so_B2)
                        dang_thuc_dung = True
if not dang_thuc_dung:  
    print("Không tồn tại !")
