import csv


def get_median(lis, pos):
    if len(lis) % 2 == 0:
        return (float(lis[len(lis) // 2 - 1][pos]) + float(lis[len(lis) // 2][pos])) / 2
    else:
        return float(lis[(len(lis) + 1) / 2][pos])


def printer(lis):
    print("{:<30}{:<30}{:<30}".format("China", "Brazil", "USA"))
    for i in range(len(lis)):
        print("{:<30}".format(lis[i]), end="")
    print(end='\n\n')


with open('income_growth.csv') as csv_file:
    growth = list(csv.reader(csv_file, delimiter=','))
    mean_values = [0, 0, 0]
    median_values = [0, 0, 0]
    standard_deviation = [0, 0, 0]

    for i in growth:
        if growth.index(i) != 0:
            for j in range(1, len(i)):
                mean_values[j - 1] += float(i[j]) / (len(growth) - 1)

    for i in growth:
        if growth.index(i) != 0:
            for j in range(1, len(i)):
                standard_deviation[j - 1] += (float(i[j]) - mean_values[j - 1])**2 / (len(growth) - 2)

    standard_deviation[0] = standard_deviation[0] ** 0.5
    standard_deviation[1] = standard_deviation[1] ** 0.5
    standard_deviation[2] = standard_deviation[2] ** 0.5

    growth = growth[1:]

    growth = sorted(growth, key=lambda x: float(x[1]))
    median_values[0] = get_median(growth, 1)
    growth = sorted(growth, key=lambda x: float(x[2]))
    median_values[1] = get_median(growth, 2)
    growth = sorted(growth, key=lambda x: float(x[3]))
    median_values[2] = get_median(growth, 3)

    print("Mean Values:")
    printer(mean_values)

    print("Median Values:")
    printer(median_values)

    print("Standard Deviation Values:")
    printer(standard_deviation)
