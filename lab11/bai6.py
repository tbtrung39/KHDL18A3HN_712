def tao_bang_so(filename='bangso.txt'):
    bang = [
        [4],
        [211, 133, 180],
        [5],
        [192, 168, 1, 254],
        [11],
        [1],
        [11],
        [233]
    ]
    with open(filename, 'w') as f:
        for dong in bang:
            f.write(' '.join(map(str, dong)) + '\n')
def xu_ly_bang_so(filename='bangso.txt', oddfile='ODD.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    print("Dòng đầu tiên:", lines[0].strip())
    print("Dòng thứ 3:", lines[2].strip())
    print("Toàn bộ file:")
    for line in lines:
        print(line.strip())
    
    numbers = []
    for line in lines:
        numbers.extend(map(int, line.strip().split()))
    
    odd_matrix = []
    index = 0
    for _ in range(4):
        row = []
        for _ in range(4):
            while index < len(numbers) and numbers[index] % 2 == 0:
                index += 1
            if index < len(numbers):
                row.append(str(numbers[index]))
                index += 1
            else:
                row.append('0')
        odd_matrix.append(row)

    with open(oddfile, 'w') as f:
        for row in odd_matrix:
            f.write(' '.join(row) + '\n')

    with open(oddfile, 'r') as f:
        lines = f.readlines()
        print("Dòng cuối ODD.txt:", lines[-1].strip())
