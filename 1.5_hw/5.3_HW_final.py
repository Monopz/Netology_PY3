student_list = {
    'Иван Немцов': {'sex': 'мужчина', 'experience': 'да', 'mark_for_homework': [8, 9, 6, 10, 8], 'mark_for_exam': 9},
    'Алина Шустрая': {'sex': 'женщина', 'experience': 'да', 'mark_for_homework': [6, 8, 6, 9, 7], 'mark_for_exam': 8},
    'Полина Малая': {'sex': 'женщина', 'experience': 'нет', 'mark_for_homework': [5, 10, 6, 9, 5], 'mark_for_exam': 10},
    'Егор Зиновьев': {'sex': 'мужчина', 'experience': 'нет', 'mark_for_homework': [10, 6, 8, 7, 6], 'mark_for_exam': 7},
    'Валерий Мутко': {'sex': 'мужчина', 'experience': 'да', 'mark_for_homework': [6, 7, 8, 7, 8], 'mark_for_exam': 9},
    'Николай Вельможа': {'sex': 'мужчина', 'experience': 'нет', 'mark_for_homework': [4, 7, 5, 8, 7], 'mark_for_exam': 7},
    'Денис Земченко': {'sex': 'мужчина', 'experience': 'да', 'mark_for_homework': [8, 10, 8, 10, 9], 'mark_for_exam': 10}
    }

student = len(student_list)
student_men = len(dict((k, v) for k, v in student_list.items() if v['sex'] == 'мужчина'))
student_women = len(dict((k, v) for k, v in student_list.items() if v['sex'] == 'женщина'))

def average_mark_hw():
    marks_list = []
    for hw_mark in student_list.values():
        for i in hw_mark['mark_for_homework']:
            marks_list.append(i)
    average_mark = round((sum(marks_list) / len(marks_list)), 1)
    print('Средняя оценка на {0} учеников: {1}'.format(student, average_mark))

def average_mark_ex():
    result = 0
    for ex_mark in student_list.values():
        result += ex_mark['mark_for_exam']
        a = round((result / student), 1)
    print('Средняя оценка за экзамен среди всех учеников {0}'.format(a))

def average_hw_m():
    marks_list = []
    for hw_mark in student_list.values():
        if hw_mark['sex'] == 'мужчина':
            for i in hw_mark['mark_for_homework']:
                marks_list.append(i)
    average_hw_men = round((sum(marks_list) / len(marks_list)), 1)
    print('Средняя оценка за домашние задания у мужчин: {}'.format(average_hw_men))

def average_hw_w():
    marks_list = []
    for hw_mark in student_list.values():
        if hw_mark['sex'] == 'женщина':
            for i in hw_mark['mark_for_homework']:
                marks_list.append(i)
    average_hw_wom = sum(marks_list) / len(marks_list)
    print('Средняя оценка за домашние задания у женщин: {}'.format(average_hw_wom))

def average_ex_m():
    result = 0
    for ex_mark in student_list.values():
        if ex_mark['sex'] == 'мужчина':
            result += ex_mark['mark_for_exam']
            average_mark = result / student_men
    print('Средняя оценка за экзамен у мужчин: {}'.format(average_mark))

def average_ex_w():
    result = 0
    for ex_mark in student_list.values():
        if ex_mark['sex'] == 'женщина':
            result += ex_mark['mark_for_exam']
            average_mark = result / student_women
    print ('Средняя оценка за экзамен у женщин: {}'.format(average_mark))

def average_with_exp_hw():
    marks_list = []
    for hw_mark in student_list.values():
        if hw_mark['experience'] == 'да':
            for i in hw_mark['mark_for_homework']:
                marks_list.append(i)
    average_hw_wom = sum(marks_list) / len(marks_list)
    print('Средняя оценка за домашние задания у студентов с опытом: {}'.format(average_hw_wom))

def average_without_exp_hw():
    marks_list = []
    for hw_mark in student_list.values():
        if hw_mark['experience'] == 'нет':
            for i in hw_mark['mark_for_homework']:
                marks_list.append(i)
    average_hw_wom = (round(sum(marks_list) / len(marks_list), 1))
    print('Средняя оценка за домашние задания у студентов без опыта: {}'.format(average_hw_wom))

def average_with_exp_ex():
    result = 0
    for ex_mark in student_list.values():
        if ex_mark['experience'] == 'да':
            result += ex_mark['mark_for_exam']
            average_mark = result / len(dict((k, v) for k, v in student_list.items() if v['experience'] == 'да'))
    print ('Средняя оценка за экзамен у студентов с опытом: {}'.format(average_mark))

def average_without_exp_ex():
    result = 0
    for ex_mark in student_list.values():
        if ex_mark['experience'] == 'нет':
            result += ex_mark['mark_for_exam']
            average_mark = result / len(dict((k, v) for k, v in student_list.items() if v['experience'] == 'нет'))
    print ('Средняя оценка за экзамен у студентов без опыта: {}'.format(average_mark))

def final_mark():
    for mark in student_list.values():
        b = 0
        for a in mark['mark_for_homework']:
            b += a
        a = round((b/5 * 0.6 + 0.4 * mark['mark_for_exam']), 1)
        c = {'final_mark': a}
        mark.update(c)

final_mark()

def best_student():
    marks = []
    for key, value in student_list.items():
        marks.append(value['final_mark'])

    best_students = [[key, value['final_mark']] for key, value in student_list.items() if value['final_mark'] in sorted(marks)[-3:-1]]

    for el in best_students:
        print('Лучший студент: {}, с оценкой {}'.format(el[0], el[1]))

def menu():
    while True:
        print('\nВведите данные, которые Вам необходимо найти')
        print('''
        1. Средняя оценка за домашнее задание по группе.
        2. Средняя оценка за экзамен по группе.
        3. Средняя оценка за домашнее задание среди мужчин.
        4. Средняя оценка за домашнее задание среди женщин.
        5. Средняя оценка за экзамен среди мужчин.
        6. Средняя оценка за экзамен среди женщин.
        7. Средняя оценка за домашнее задание среди студентов с опыт работы.
        8. Средняя оценка за домашнее задание среди студентов без опыта работы.
        9. Средняя оценка за экзамен среди студентов с опыта работы.
        10. Средняя оценка за экзамен среди студентов без опыта работы.
        11. Лучший студент.
        q. Выйти
        ''')

        input_menu = input()
        if input_menu == '1':
            average_mark_hw()
        elif input_menu == '2':
            average_mark_ex()
        elif input_menu == '3':
            average_hw_m()
        elif input_menu == '4':
            average_hw_w()
        elif input_menu == '5':
            average_ex_m()
        elif input_menu == '6':
            average_ex_w()
        elif input_menu == '7':
            average_with_exp_hw()
        elif input_menu == '8':
            average_without_exp_hw()
        elif input_menu == '9':
            average_with_exp_ex()
        elif input_menu == '10':
            average_without_exp_ex()
        elif input_menu == '11':
            best_student()
        elif input_menu == 'q':
            break
        else:
            print('Введите правильную команду.')

menu()
