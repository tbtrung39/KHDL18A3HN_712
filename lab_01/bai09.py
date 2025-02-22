x, y, z = map(float, input("Nhập tọa độ điểm (x y z): ").split())

# Nhập mặt phẳng để tính điểm đối xứng
mat_phang = (input("Nhập mặt phẳng (Oxy, Oxz, Oyz): ").strip())

# Tính tọa độ điểm đối xứng
if mat_phang == "Oxy":
    doi_xung = (x, y, -z)
elif mat_phang == "Oxz":
    doi_xung = (x, -y ,z)
elif mat_phang == "Oyz":
    doi_xung = (-x, y, z)
else:
    doi_xung = None
    print("Mặt phẳng không hợp lệ. Vui lòng nhập Oxy, Oxz hoặc Oyz.")

if doi_xung:
    print(f"Tọa độ điểm đối xứng qua mặt phẳng {mat_phang} là: {doi_xung}")