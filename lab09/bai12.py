def tim_ga_va_cho(x=0):
    y = 36 - x
    if 2 * x + 4 * y == 100:
        return x, y
    elif x > 36:
        return None
    return tim_ga_va_cho(x + 1)

result = tim_ga_va_cho()
if result:
    ga, cho = result
    print(f"So con ga: {ga}, so con cho: {cho}")
else:
    print("Khong tim thay ket qua hop le!")