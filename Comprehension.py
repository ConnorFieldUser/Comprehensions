# Opening files
with open("dataset.txt") as open_dataset:
    dataset = open_dataset.readlines()

# print(dataset)
# print(dataset.replace("\n", " "))
# string = ""
# for letter in string:
#     if letter not in vow
#     string += letter


def vwl_rmvr(string):
    vow = 'aeiou'
    n_vwl_str = [letter for letter in string if letter not in vow]
    return ''.join(n_vwl_str)
# Removes vowels

print(vwl_rmvr("Comprehensions are the greatest!\n"))


# Dataset formating =
def file_format(file):
    data_format = [item.split(',') for item in dataset]
    return data_format

ff_ds = (file_format(dataset))

# print(ff_ds)

# Fifth collumn grab
watertemp = [row[4] for row in ff_ds]


watertemp.pop(0)


def string_to_float(temp_data):
    water_float_lol = [float(string) for string in temp_data]
    return water_float_lol

new_temp = string_to_float(watertemp)

print("Tempature list:")
print(new_temp)

print("")


def cels_to_fahr(templist):
    fahr_temp = [float(celtemp) * 9 // 5 + 32 for celtemp in templist]
    return fahr_temp

fin_temp = cels_to_fahr(watertemp)

print(fin_temp)


# Create a dictionary with Date as the key and Wave Height as the value
w_hight_day = {row[5].replace('\n', ''): row[1]
               for row in ff_ds}

print(w_hight_day)

dayta_set = [row[5].replace('\n', '')[-2:] for row in ff_ds]

print(dayta_set)
# wave_day_average = {for day in dayta_set}


homework_grades = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                   'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 'River': {'Homework 1': 85, 'Homework 2': 91}}
