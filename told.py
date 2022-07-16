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
        mass_x_list.append(mass_x)

    return mass_x_list

def mass_share_Y_axe():
    items = instantiate_from_csv()
    mass_y_list = []
    for y in range(4, len(items) - 1):
        mass_y = str(items[y][3])
        mass_y = unidecode.unidecode(mass_y)
        mass_y = mass_y.replace(' ', '.')
        mass_y = mass_y.strip('.')
        mass_y_list.append(mass_y)

    return mass_y_list

def mass_share_Z_axe():
    items = instantiate_from_csv()
    mass_z_list = []
    for z in range(4, len(items) - 1):
        mass_z = str(items[z][4])
        mass_z = unidecode.unidecode(mass_z)
        mass_z = mass_z.replace(' ', '.')
        mass_z = mass_z.strip('.')
        mass_z_list.append(mass_z)

    return mass_z_list
def visualization_of_variables():
    frequency = frequency_validation()
    x = mass_share_X_axe()
    y = mass_share_Y_axe()
    z = mass_share_Z_axe()

    for i in range(len(frequency_validation())):
        # print(items[x][1])
        print(frequency[i], '|', x[i], '|', y[i], '|', z[i])


visualization_of_variables()