import random
import math
from colorama import init, Fore
from say_text import say_text
from listen import listen


def main():
    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Micriphone with name \"{1}\" found for 'microphone (device index = {0})'".format(index, name ))

    init(autoreset=True)

    kol = int(input('Сколько примеров сгенерировать '))
    counter = 0
    while counter < kol:
        list_equation = generate_math_equation()
        print(list_equation[3])
        res_user = input('Если хотите ответить голосом введите "v" ')
        if res_user == 'v':
            try:
                query = float(listen())
                if float(query) == float(solution(list_equation)):
                    say_text('Верно')
                else:
                    say_text('Вы ошиблись')
                    print(float(query))
                    print(float(solution(list_equation)))
                    print('Правилный ответ', solution(list_equation))
            except ValueError:
                say_text('Сказаное Вами, не является числом.')
        else:
            try:
                float(res_user)
                if float(res_user) == float(solution(list_equation)):
                    say_text('Верно')
                else:
                    say_text('Вы ошиблись')
                counter = counter + 1
            except ValueError:
                print(Fore.RED + 'EROOR. Неверный ввод')


def generate_math_equation():
    '''Генерирует рандомный пример'''
    dict_math_sinb = {
        1: '+',
        2: '-',
        3: '*',
        4: '/',
        5: '√'
    }

    list_return = []
    range_number_min = 0
    range_number_max = 100
    math_sinb = random.randint(1, 4)
    list_return.append(dict_math_sinb[math_sinb])
    number1 = random.randint(range_number_min, range_number_max)
    list_return.append(number1)
    number2 = random.randint(range_number_min, range_number_max)
    list_return.append(number2)
    if math_sinb == 5:
        resstr = f"{dict_math_sinb[math_sinb]} {number1}"
    else:
        resstr = f"{number1} {dict_math_sinb[math_sinb]} {number2}"

    if math_sinb == 4 and number2 == 0:
        return generate_math_equation
    list_return.append(resstr)
    return list_return


def solution(list_equation):
    '''Решает переданный в нее пример '''
    match list_equation[0]:
        case '+':
            res = list_equation[1] + list_equation[2]
        case '-':
            res = list_equation[1] - list_equation[2]
        case '*':
            res = list_equation[1] * list_equation[2]
        case '/':
            res_temp = list_equation[1] / list_equation[2]
            res = float('{:.3f}'.format(res_temp))
        case '√':
            res =  math.sqrt(list_equation[1])
    return res

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
