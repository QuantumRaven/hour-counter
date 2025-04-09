#!/usr/bin/env python3

import csv

def sum_csv(file_name, column_index):
    total = 0
    with open("./hours.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float((row[column_index]))
        return total

file_name = "./uber_hours.csv"
column_num = 0
column_sum = sum_csv(file_name, column_num)
print(column_sum)

file_name = "./uber_hours.csv"
column_num = 1
column_sum = sum_csv(file_name, column_num)
print(column_sum/60)
