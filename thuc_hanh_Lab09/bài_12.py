def tim_ga_cho(ga=0, cho=0):
    if ga + cho > 36:
        return
    if ga + cho == 36 and ga * 2 + cho * 4 == 100:
        print(f"Số con gà: {ga}, Số con chó: {cho}")
        return
    tim_ga_cho(ga + 1, cho)
    tim_ga_cho(ga, cho + 1)
tim_ga_cho()
