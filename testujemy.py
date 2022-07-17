import csv
import unidecode

def instantiate_from_csv():
    #vcs_file = str(input('Please enter path to vcs_file: '))
    vcs_file = 'example.csv'
    with open(vcs_file, 'r') as f:
        reader = csv.reader(f)
        items = list(reader)
        return items
def frequency_validation():
    items = instantiate_from_csv()
    frequency_list = []
    for x in range(4, len(items)-1):
        frequency = str(items[x][1])
        frequency = unidecode.unidecode(frequency)
        frequency = frequency.replace(' ', '.')
        frequency = frequency.strip('.')
        frequency_list.append(frequency)
    return frequency_list


def mass_share_X_axe():
    items = instantiate_from_csv()
    mass_x_list = []
    for x in range(4, len(items) - 1):
        mass_x = str(items[x][2])
        mass_x = unidecode.unidecode(mass_x)
        mass_x = mass_x.replace(' ', '.')
        mass_x = mass_x.strip('.')
        mass_x_list.append(float(mass_x))

    return mass_x_list

def mass_share_Y_axe():
    items = instantiate_from_csv()
    mass_y_list = []
    for y in range(4, len(items) - 1):
        mass_y = str(items[y][3])
        mass_y = unidecode.unidecode(mass_y)
        mass_y = mass_y.replace(' ', '.')
        mass_y = mass_y.strip('.')
        mass_y_list.append(float(mass_y))

    return mass_y_list

def mass_share_Z_axe():
    items = instantiate_from_csv()
    mass_z_list = []
    for z in range(4, len(items) - 1):
        mass_z = str(items[z][4])
        mass_z = unidecode.unidecode(mass_z)
        mass_z = mass_z.replace(' ', '.')
        mass_z = mass_z.strip('.')
        mass_z_list.append(float(mass_z))

    return mass_z_list

def filtration_significant_masses():
     # input('Please enter the minimum percentage mass share of the mod, or type "skip" to pass filtration: ')
     # if input == 'skip':
     #     frequency = frequency_validation()
     #     x = mass_share_X_axe()
     #     y = mass_share_Y_axe()
     #     z = mass_share_Z_axe()
     #     zas = [frequency, x, y, z]
     #     return zas
     # else:
    frequency = frequency_validation()
    x = mass_share_X_axe()
    y = mass_share_Y_axe()
    z = mass_share_Z_axe()
    zas_1 = [frequency, x, y, z]
    zas = [[], [], [], []]
    for i in range(len(zas_1[0])):
        if zas_1[1][i] or zas_1[2][i] or zas_1[3][i] > 0.05:
            zas[0].append(zas_1[0][i])
            zas[1].append(zas_1[1][i])
            zas[2].append(zas_1[2][i])
            zas[3].append(zas_1[3][i])
        else:
            continue
    print(zas_1)

def visualization_of_variables():
    zas = filtration_significant_masses()
    # frequency = frequency_validation()
    # x = mass_share_X_axe()
    # y = mass_share_Y_axe()
    # z = mass_share_Z_axe()
    #
    # zas = [frequency,x,y,z]
    string_rep = ''
    # get max column widths for printing
    width = []
    for i in range(len(zas)):
        columns = zas[i]
        width.append(len(max(columns, key=len)))

    # print the csv strings
    indices = ["Frequency [Hz]", "Mass X axe [%]", "Mass Y axe [%]", "Mass Z axe [%]"]
    for i in range(1, 4):
        indices[i] = indices[i] + ' '* (len(indices[0]) - len(indices[i]))


    indices_row = '    '
    cells_column = []
    for idx, col in enumerate(indices):
        format = '%-' + str(width[idx]) + "s"
        cells_column.append(format % col)
    indices_row += '  '.join(cells_column)
    indices_row += '  \n'
    for i in range(len(zas[0])):

        string_rep += f'{i}' + ' '* (3 - len(str(i)))+ '|'
        cells = []


        for a in range(len(zas)):
            format = str(zas[a][i] + ' ' * (len(indices[0]) - len(zas[a][i])))
            cells.append(format)

        string_rep += ' |'.join(cells)
        string_rep += ' |\n'

    str_len = int(len(string_rep) / 41)
    string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

    print(string_rep)

filtration_significant_masses()

