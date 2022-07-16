def string():
    zas = [["*" for i in range(41)], ["." for i in range(41)], ["g" for i in range(41)], ["-" for i in range(41)]]
    string_rep = ''
    # get max column widths for printing
    width = []
    for i in range(len(zas)):
        columns = zas[i]
        width.append(len(max(columns, key = len)))

    # print the csv strings
    indices = ["*", ".", "g", "-"]
    indices_row = '   '
    cells_column = []
    for idx, col in enumerate(indices):
        format = '%-' + str(width[idx]) + "s"
        cells_column.append(format % col)
    indices_row += '  '.join(cells_column)
    indices_row += '  \n'
    for i in range(len(zas[0])):
        row = zas[0][i]
        string_rep += f'{i+1} |'
        cells = []
        c = 0

        for x in range(len(zas)):
            format = str(zas[x][c])
            cells.append(format)
            c += 1
        string_rep += ' |'.join(cells)
        string_rep += ' |\n'

    str_len = int(len(string_rep) / 4)
    string_rep = indices_row + '-' * 30 + '\n' + string_rep + '-' * 30

    print(string_rep)
string()