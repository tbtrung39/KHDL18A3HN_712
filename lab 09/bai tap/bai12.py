def tim_ga_va_cho(ga=0):
    cho = 36 - ga
    if cho < 0:
        return
    if ga * 2 + cho * 4 == 100:
        print(f"Gà: {ga}, Chó: {cho}")
        return
    tim_ga_va_cho(ga + 1)

tim_ga_va_cho()