import csv

def instantiate_from_csv():
    #vcs_file = str(input('Please enter path to vcs_file: '))
    vcs_file = 'example.csv'
    with open(vcs_file, 'r') as f:
        reader = csv.reader(f)
        items = list(reader)
        return items
def visualization_of_variables():
    items = instantiate_from_csv()
    for x in range(3, len(items)):
        # print(items[x][1])
        print(items[x][1], '|', items[x][2], '|', items[x][3], '|', items[x][4])

def frequency_validation():
    items = instantiate_from_csv()
    frequency_list = []
    for x in range(4, len(items)):
        frequency = str(items[x][1])
        frequency = frequency.replace(' ', '.')

        frequency = frequency.strip('.')
        # frequency = frequency.translate({ord(" "): ""})
        # x = float(frequency)
        # print(f'{x:.30f}')
        # print(frequency)
        frequency_list.append(frequency)

    # z = float(frequency_list[14])
    # z += 1
    # print(z)

    z = frequency_list
    # z += 1
    print(z)






frequency_validation()