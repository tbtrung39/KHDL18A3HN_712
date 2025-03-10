# In menu với hình minh họa đẹp mắt
print("🎉"*20)
print("🍹 Chào mừng bạn đến với Quán Đồ Uống 🍹")
print("🎉"*20)
print("="*60)
print("1. Cafe  ☕")
print("2. Cam vắt  🍊")
print("3. Nước ép cà rốt  🥕")
print("4. Nước lọc  💧")
print("5. Nước dừa  🥥")
print("="*60)
mon_da_chon = ""
while True:
    lua_chon=input("\n🎯 Vui lòng chọn đồ uống (nhập số từ 1 đến 5): ")
    if lua_chon=='1':
        mon_da_chon+="Cafe ☕\n"
        print("\nBạn đã chọn: Cafe ☕.")
    elif lua_chon=='2':
        mon_da_chon+="Cam vắt 🍊\n"
        print("\nBạn đã chọn: Cam vắt 🍊.")
    elif lua_chon=='3':
        mon_da_chon+="Nước ép cà rốt 🥕\n"
        print("\nBạn đã chọn: Nước ép cà rốt 🥕.")
    elif lua_chon=='4':
        mon_da_chon+="Nước lọc 💧\n"
        print("\nBạn đã chọn: Nước lọc 💧.")
    elif lua_chon=='5':
        mon_da_chon+="Nước dừa 🥥\n"
        print("\nBạn đã chọn: Nước dừa 🥥.")
    else:
        print("\n❌ Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")
        continue  
    tiep_tuc=input("\n📝 Bạn có muốn chọn thêm đồ uống không? (y/n): ")
    if tiep_tuc=='n':
        print("\n🎯 Bạn đã chọn những đồ uống sau:")
        print(mon_da_chon)
        confirm = input("\n🔄 Bạn có chắc chắn muốn hoàn tất không? (y/n): ")
        if confirm == 'y':
            print("\n🎉 Cảm ơn bạn đã sử dụng dịch vụ! Hẹn gặp lại! 🎉")
            break
        else:
            print("\n🔄 Quay lại chọn thêm đồ uống!")
            continue 
    elif tiep_tuc != 'y':
        print("\n❌ Lựa chọn không hợp lệ. Vui lòng nhập y hoặc n.")
