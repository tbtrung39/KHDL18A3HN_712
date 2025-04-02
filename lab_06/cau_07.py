import random
list_ = [['mon', 73], ['tue',89], ['wed',95], ['thu', 103],['fri', 115], ['sat', 128], ['sun', 120]]
print('danh sách list:')
for item in list_:
    print(item)
print('phân tử thứ 2 của sublist vi trí 3:',list_[2][1])
random.choice = random.choice(list_).append(random.randint(50,150))
print('danh sách list sau khi thêm phần tử ngẫu nhiên:',list_)
tong_gia_tri = sum(list_[i][1] for i in [1,2,5,6])
print('tổng giá trị của thứ hai, ba, bảy, chủ nhật:', tong_gia_tri)

