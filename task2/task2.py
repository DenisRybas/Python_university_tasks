def transpose(arr):
    if arr == []:
        return arr
    rows = len(arr)
    cols = len(arr[0])
    return [[arr[i][j] for i in range(rows)] for j in range(cols)]

def remove_equal_columns(arr):
    a = transpose(arr)
    out = []
    for i in a:
        if not i in out: out.append(i)
    return transpose(out)

if __name__ == '__main__':
    print(remove_equal_columns([[11, 12, 15, 11, 53, 11, 14, 14],
                            [13, 12, 14, 13, 15, 13, 15, 15],
                            [13, 12, 14, 13, 15, 13, 14, 14],
                            [13, 12, 14, 13, 15, 13, 14, 14],
                            [13, 12, 14, 11, 15, 13, 14, 14]]))