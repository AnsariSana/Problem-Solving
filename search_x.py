def search(matrix,length,x):
    row, col = 0,length - 1
    if matrix[length-1][length-1] < x:
        return "Not Found"
    while row <= length-1 and col >= 0:

        if matrix[row][col] < x:
            row += 1
        elif matrix[row][col] > x:
            col -= 1
        elif matrix[row][col] == x:
            return row,col

    else:
        return "Not Found"
matrix = [[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
x = int(input())
res = search(matrix,len(matrix),x)
print(res)