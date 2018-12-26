# -- coding: utf-8 --

import csv
import collections


def csv_write(restaurant_list):
    with open('ranking.csv', "w+") as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(restaurant_list)


def csv_read():
    restaurant_dict = collections.defaultdict(int)
    with open('ranking.csv', "r+") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            restaurant_dict[row['Name']] = int(row['Count'])
    return restaurant_dict


#print(csv_read())
