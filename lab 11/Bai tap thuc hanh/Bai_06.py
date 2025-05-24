def xu_ly_ma_tran(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    matrix = [list(map(int, line.strip().split())) for line in lines[1:]]

    print("a. Dòng đầu tiên:", matrix[0])
    if len(matrix) >= 3:
        print("a. Dòng thứ 3:", matrix[2])
    else:
        print("Dòng thứ 3 không tồn tại.")

    print("\nb. Toàn bộ ma trận:")
    for row in matrix:
        print(row)

    odd_matrix = []
    for row in matrix:
        odd_row = [x if x % 2 == 1 else 0 for x in row]
        odd_matrix.append(odd_row)

    with open('ODD.txt', 'w') as out_file:
        for row in odd_matrix:
            out_file.write(' '.join(map(str, row)) + '\n')

    with open('ODD.txt', 'r') as odd_file:
        lines = odd_file.readlines()
        if lines:
            print("\nd. Dòng cuối của file ODD.txt:")
            print(lines[-1].strip())
        else:
            print("File ODD.txt rỗng.")

xu_ly_ma_tran("input_ma_tran.txt")
