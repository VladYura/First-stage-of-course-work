from functions import *
from input_data import input_addictions, start_tree


# Главная функция скрипта
# Запускает все остальные функции в нужном порядке нужное количество раз
def main(names, start):
    letters = ['C', 'D', 'E', 'F']

    out = start_progress(start)
    for i in out:
        print(i)

    print()
    dict_out = conclusion_dict('B', out)
    print(dict_out)

    out = group_substitution(out, names, dict_out)

    print()
    for i in out:
        print(i)

    for letter in letters:
        print()
        out = mid_game(out, letter)
        for i in out:
            print(i)

        print()
        dict_out = conclusion_dict(letter, out)
        print(dict_out)

        out = group_substitution(out, names, dict_out)

        print()
        for i in out:
            print(i)

    final_ans = super_last_func(out, dict_out)
    print()
    for i in final_ans:
        print(i)

    return final_ans


