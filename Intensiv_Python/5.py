with open('salary.csv', 'r', encoding='utf-8') as file:
    file_content = file.readlines()

print(f'В файле строк - {len(file_content)}')

salary_data = []

for line in file_content:
    line_proceed = line.replace('\n', '').split(',')
    worker_name = line_proceed.pop(0)
    salary_data.append(line_proceed)

salary_data_zip = tuple(zip(*salary_data))

for month_data in salary_data_zip:
    print(month_data)
    # summa = 0
    # for salary in month_data:
    #     summa += float(salary)
    summa = sum(map(float, month_data))
    rezult = summa / len(month_data)
    print(f'{rezult:.2f} руб')

