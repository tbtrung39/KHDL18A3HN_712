# Xác suất không lần nào cả 3 xúc xắc đều ra 6 trong 3 lần tung
xac_suat_hut = (215/216) ** 3
#Xác suất ít nhất 1 lần cả 3 xúc xắc đều ra 6
xac_suat_it_nhat_mot_lan = 1 - xac_suat_hut
xac_suat_it_nhat_mot_lan = round(xac_suat_it_nhat_mot_lan, 2)
print(f"Xác suất ít nhất 1 lần cả 3 xúc xắc đều ra 6:{xac_suat_it_nhat_mot_lan}")