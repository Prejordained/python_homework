import csv
import os
import traceback
import custom_module
from datetime import datetime

#Task 2

def read_employees():
    result = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row:
                    result['fields'] = row
                    first_row = False
                else:
                    rows.append(row)
        result['rows'] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return result

employees = read_employees()
print(employees)

#Task 3

def column_index(column_name):
    return employees['fields'].index(column_name)

employee_id_column = column_index('employee_id')

#Task 4

def first_name(row_number):
    col = column_index('first_name')
    return employees['rows'][row_number][col]

#Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches

#Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches    

#Task 7

def sort_by_last_name():
    last_name_col = column_index('last_name')
    employees['rows'].sort(key=lambda row: row[last_name_col])
    return employees['rows']


#Task 8

def employee_dict(row):
    result = {}
    id_col = column_index('employee_id')
    for i, field in enumerate(employees['fields']):
        if i == id_col:
            continue
        result[field] = row[i]
    return result

print(employee_dict(employees['rows'][0]))

#Task 9

def all_employees_dict():
    result = {}
    id_col = column_index('employee_id')
    for row in employees['rows']:
        emp_id = row[id_col]
        result[emp_id] = employee_dict(row)
    return result

print(all_employees_dict())

#Task 10

def get_this_value():
    return os.getenv('THISVALUE')

#Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my new secret")
print(custom_module.secret)

#Task 12

def read_minutes():
    def read_csv(filename):
        result = {}
        rows = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                first_row = True
                for row in reader:
                    if first_row:
                        result['fields'] = row
                        first_row = False
                    else:
                        rows.append(tuple(row))
            result['rows'] = rows
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
        return result
    
    minutes1 = read_csv('../csv/minutes1.csv')
    minutes2 = read_csv('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    return set1.union(set2)

minutes_set = create_minutes_set()

#Task 14

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list
    ))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        for row in converted: 
            writer.writerow(row)
    return converted

write_sorted_list()