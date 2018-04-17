with open('salary.csv', 'r', encoding='utf-8') as file:
    file_content = file.readlines()
    print(file_content)

print(f'В файле строк - {len(file_content)}')

salary_data =[]

for line in file_content:
    line_proceed = line.replace('\n', '').split(',')
    # забрали имя работника из списка
    worker_name = line_proceed.pop(0)
    # print(worker_name)
    print(f'{worker_name}: {line_proceed}')
    salary_data.append(line_proceed)




print(type(line_proceed))
