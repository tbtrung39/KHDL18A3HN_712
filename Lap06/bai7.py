import random
 List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
 print("Cac phan tu trong List_: ")
 for item in List_:
     print(item)
 phan_tu_2 = List_[2][1]
 print("Phan tu thu 2 cua sublist 3: ", phan_tu_2)
 
 do_dai = len(List_)
 print("Do dai cua List_ la: ", do_dai)
 ngay_nn = "day" + str(random.randint(1,100))
 so_nn = random.randint(1,200)
 sub_nn = [ngay_nn, so_nn]
 List_.append(sub_nn)
 print("List_ sau khi them sublist ngau nhien:", List_)
 
 ngay_can_tinh = ["mon", "tue", "sat", "sun"]
 tong_sale = 0
 for sublist in List_:
     ngay = sublist[0]  
     sale = sublist[1]  
     if ngay in ngay_can_tinh:
         tong_sale += sale
 
 
 print("Danh sach List_:", List_)
 print("Tong sale value cua thu 2, thu 3, thu 7 va chu nhat:", tong_sale)