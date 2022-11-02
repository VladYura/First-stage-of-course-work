# Функция для первого сокращения (она отличается от mid_game, так как входной first_list имеет другую размерность)
def start_progress(first_list):
    output = []
    len_gr = 0
    group_list = []
    iterate = 1
    while True:

        if len(first_list) == len_gr:
            break

        last_no_repeat_item = no_list_append(first_list, group_list, 0, 0)
        group_list = [last_no_repeat_item[0]]
        group = f'B{iterate}'

        for j in range(last_no_repeat_item[1] + 1, len(first_list)):
            if first_list[j][1] == group_list[0][1]:
                group_list.append(first_list[j])

        iterate += 1
        len_gr += len(group_list)
        output.append([group, group_list])
    return output


# Вспомогательная функция
# Определяет, есть ли в output состояние, находящееся в промежуточном списке (group_list это который формирует output)
# Возвращает False, если такое состояние есть, True - наоборот
def find_the_same_items(output, group_list):
    for i in output:
        for j in group_list:
            if j in i[1]:
                return False
    return True


# Выводит заключительный словарь после сокращения
def conclusion_dict(group, output):
    output_dict = {f'{group}{x + 1}': [] for x in range(len(output))}
    p = 0
    for i in output_dict.keys():
        for j in output[p][1]:
            output_dict[i].append(j[0])
        p += 1
    return output_dict


# Вспомогательная функция
# Возвращает состояние, которое не повторялось в промежуточном списке (это который формирует output)
# Принимает ключ key, так как первое сокращение отличается от последующих
# Index - это значение последнего не повторяющегося состояния (иначе output будет состоять из одинаковых групп)
def no_list_append(list1, list2, key, index):
    if key == 0:
        for j in range(len(list1)):
            if list1[j] not in list2:
                return [list1[j], j]
    else:
        for j in range(index, len(list1[1])):
            if list1[1][j] not in list2:
                return [list1[1][j], j]
    return list1[1]


# Замещает группы в состояниях output
# По сути преобразует output для следующего сокращения
# Принимает output, список последовательностей соединений(список names) и словарь после сокращения
def group_substitution(output, name, dic_out):
    for item in output:
        for i in range(len(item[1])):
            item_spis = [0, 0]
            items_in_names = name[item[1][i][0]]
            for key in dic_out.keys():
                if items_in_names[0] in dic_out[key]:
                    item_spis[0] = key
                if items_in_names[1] in dic_out[key]:
                    item_spis[1] = key
            item[1][i][1] = tuple(item_spis)
    return output


# Заключительная функция для вывода итогов всех сокращений
# Принимает output и словарь последнего сокращения
def super_last_func(output, dic_out):
    result = []
    for item in output:
        result.append([dic_out[item[0]][0], (dic_out[item[1][0][1][0]][0], dic_out[item[1][0][1][1]][0])])
    return result


# Основная функция дял сокращения
# Принимает предыдущий output и букву группы
def mid_game(first_list, group_name):
    output = []
    len_gr = 0
    group_list = []
    iterate = 1
    last_no_repeat_item = [0, 0]

    while True:
        # Во всех сокращениях кроме последнего мы сокращаем только первую группу
        # Поэтому здесь прописан if, запускающий функцию для последнего сокращения
        if len(first_list[0][1]) == 1:
            return func_last_stage(first_list, group_name)
        else:
            last_no_repeat_item = no_list_append(first_list[0], group_list, 1, last_no_repeat_item[1])

        group = f'{group_name}{iterate}'
        group_list = [last_no_repeat_item[0]]

        # If, позволяющий выходить из while
        if not find_the_same_items(output, group_list):
            break

        # Поиск повторяющихся групп и формирование промежуточного списка
        for j in range(last_no_repeat_item[1] + 1, len(first_list[0][1])):
            if first_list[0][1][j][1] == group_list[0][1] and find_the_same_items(output, group_list):
                group_list.append(first_list[0][1][j])

        iterate += 1
        len_gr += len(group_list)
        output.append([group, group_list])

    # Цикл для занесения оставшихся групп в output
    for i in range(1, len(first_list)):
        group = f'{group_name}{iterate}'
        first_list[i][0] = group
        output.append(first_list[i])
        iterate += 1

    return output


# Функция исключительно для последнего сокращения
# Так как в первой группе будет находиться только а1, а последнее сокращение будет во второй группе
# Принцип тот же, что и у mid_game, только для второй группы
def func_last_stage(first_list, group_name):
    group_list = []
    a = [0, 0]
    iterate = 1
    len_gr = 0

    group = f'{group_name}{iterate}'
    first_list[0][0] = group
    output = [first_list[0]]
    iterate += 1

    while True:
        if len(first_list[1][1]) == len_gr:
            break
        a = no_list_append(first_list[1], group_list, 1, a[1])
        group_list = [a[0]]
        group = f'{group_name}{iterate}'

        for j in range(a[1] + 1, len(first_list[1][1])):
            if first_list[1][1][j][1] == group_list[0][1] and find_the_same_items(output, group_list):
                group_list.append(first_list[1][1][j])

        iterate += 1
        len_gr += len(group_list)
        output.append([group, group_list])

    for i in range(2, len(first_list)):
        group = f'{group_name}{iterate}'
        first_list[i][0] = group
        output.append(first_list[i])
        iterate += 1

    return output