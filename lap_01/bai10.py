start_hour = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
end_hour = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))
if start_hour < 5 or start_hour > 22 or end_hour < 5 or end_hour > 22:
    print("Giờ không hợp lệ. Vui lòng nhập lại.")
else:
    total_hours = end_hour - start_hour
    if total_hours <= 0:
        print("Giờ kết thúc phải lớn hơn giờ bắt đầu.")
    else:
        price_per_hour = 100000
        total_cost = 0
        if total_hours <= 3:
            total_cost = total_hours * price_per_hour
        else:
            total_cost = 3 * price_per_hour
            remaining_hours = total_hours - 3
            discounted_price = price_per_hour * 0.75
            total_cost += remaining_hours * discounted_price
        if 11 <= start_hour <= 15 or 11 <= end_hour <= 15:
            total_cost *= 0.9
            print(f"Số tiền khách phải trả là: {total_cost:.2f} đồng.")