with open('salary.csv', 'r', encoding='utf-8') as file:
    file_content = file.readlines()
    print(file_content)

# print(len(file_content))
print(f'В файле строк - {len(file_content)}')

for line in file_content:
    print(line)
    # # print('********')
    # for element in line:
    #     print(element)