#Bai12
def tinh_slg_ga_cho():
    for ga in range(37):
        cho = 36 - ga
        if ga * 2 + cho * 4 == 100:
            return ga, cho
ga, cho = tinh_slg_ga_cho()
print("Số con gà là:",ga,"Số con chó là:",cho)