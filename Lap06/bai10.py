import random
 valid_numbers = [num for num in range(0, 201) if num % 5 == 0 and num % 7 == 0]
 random_number = random.choice(valid_numbers)
 print("So ngau nhien chia het cho 5 va 7:", random_number)