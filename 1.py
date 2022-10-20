schedule = []

def tableprint(dicts):
     print("{:<3} {:<15} {:<6} {:<10} {:<10} {:<9}".format('Num','Task','Time','Date','Status','Result'))
     for dict in dicts:
         num, task, time, date, status, result = dict.values()
         print("{:<3} {:<15} {:<6} {:<10} {:<10} {:<9}".format(num, task, time, date, status, result))

task = str(input('Введите название блокнота, с которым хотите работать: '))
if task == 'notebook1':
     with open ('notebook1.csv', 'r', encoding='utf-8') as f:
         for i in f:
             num = int(i.split(',')[0])
             task = i.split(',')[1]
             time = i.split(',')[2]
             date = i.split(',')[3]
             status = i.split(',')[4]
             result = i.split(',')[5]
             schedule.append({'num': num, 'task': task, 'time': time, 'date': date, 'status': status, 'result' : result})
if task == 'notebook2':
     with open ('notebook2.csv', 'r', encoding='utf-8') as f:
         for i in f:
             num = int(i.split(',')[0])
             task = i.split(',')[1]
             time = i.split(',')[2]
             date = i.split(',')[3]
             status = i.split(',')[4]
             result = i.split(',')[5]
             schedule.append({'num': num, 'task': task, 'time': time, 'date': date, 'status': status, 'result' : result})

tableprint(schedule)
print(" ")
action = int(input('Что вы хотите сделать с файлом? \n'
                    '1 - Добавить строку \n'
                    '2 - Изменить строку \n'
                    '3 - Удалить строку \n'
                    'Введите цифру: '))
if action == 1:
     num1 = int(input('Ведите порядковый номер: '))
     task1 = input('Введите задание: ')
     time1 = input('Введите время: ')
     date1 = input('Введите дату: ')
     status1 = input('Введите приоритет: ')
     result1 = input('Введите статус: ')
     schedule.append({'num': num1, 'task': task1, 'time': time1, 'date': date1, 'status': status1, 'result' : result1})
     tableprint(schedule)

if action == 2:
     num = int(input('Введите номер изменяемой строки: '))
     new_str = (schedule[num - 1])
     print(new_str)
     change, new_val = str(input('Введите что хотите поменять и изменение через запятую: ')).split(',')
     print(new_val, change)
     new_str[change] = new_val
     tableprint(schedule)

if action == 3:
     num = int(input('Введите номер строки, которую хотите удалить: '))
     new_str = (schedule[num - 1])
     schedule.remove(new_str)
     for string in schedule:
         if int(string['num']) > num - 1:
             string['num'] -= 1
     tableprint(schedule)


print()
