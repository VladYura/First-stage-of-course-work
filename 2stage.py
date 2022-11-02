from main import main
from input_data import input_addictions, start_tree


def logic(q1, q2):
    if q1 == 0 and q2 == 0:
        return (0, 'x')
    elif q1 == 0 and q2 == 1:
        return (1, 'x')
    elif q1 == 1 and q2 == 0:
        return ('x', 1)
    else:
        return ('x', 0)


last_table = main(input_addictions, start_tree)

Qt = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0]
]


def sort(output):
    res = []
    for i in range(15):
        for item in output:
            if item[0] == f'a{i + 1}':
                res.append(item)
    return res


def write_condition(output):
    q_addict = {}
    count = 0
    for i in range(15):
        for item in output:
            if item[0] == f'a{i + 1}':
                q_addict[f'a{i + 1}'] = Qt[count]
                count += 1

    print(f'КЬЮШКИ: ')
    for i in q_addict.items():
        print(i)
    print()

    return q_addict


def create_q(output, key, condition):
    q = []
    for i in range(len(output)):
        q.append(condition[output[i][1][key]])

    for i in q:
        print(i)
    return q


# Qt0 = [
#     [0, 0, 1, 0],
#     [0, 1, 0, 0],
#     [0, 1, 1, 1],
#     [1, 0, 0, 0],
#     [1, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 1, 1, 1],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

# Qt1 = [
#     [0, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 0, 1],
#     [0, 1, 1, 1],
#     [1, 0, 0, 0],
#     [1, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]


Qt0 = create_q(sort(last_table), 0, write_condition(last_table))
Qt1 = create_q(sort(last_table), 1, write_condition(last_table))


def create_jump_table(q, q0, q1):
    output = []

    for j in range(len(q[0])):
        result0 = []
        result1 = []
        for i in range(len(q)):
            result0.append(logic(q[i][j], q0[i][j]))
            result1.append(logic(q[i][j], q1[i][j]))
        output.append([f'JK{j + 1}', [result0, result1]])
        # print(f'Триггер {j + 1}')
        # print(f'J{j + 1}      K{j + 1}')
        # for k in range(len(result0)):
        #     print(*result0[k],'  ', *result1[k])

    return output


def create_map_carno():
    out = []
    for i in range(4):
        line = []
        for j in range(8):
            line.append('x')
        out.append(line)
    return out


def refactor_map_carno_4x8(res_list, letter):
    map = create_map_carno()
    index_i = [0, 1, 3, 2]
    index_j = [0, 1, 3, 2, 7, 6, 4, 5]
    count = 0
    num_lst = 0
    for i in index_i:
        if count == 16:
            count = 0
            num_lst = 1
        for j in index_j:
            try:
                map[i][j] = res_list[num_lst][count][letter]
                count += 1
            except IndexError:
                map[i][j] = 'x'
                count += 1
    return map


def main(q, q0, q1):
    out = create_jump_table(q, q0, q1)
    JK = []
    for i in range(4):
        J = refactor_map_carno_4x8(out[i][1], 0)
        K = refactor_map_carno_4x8(out[i][1], 1)
        JK.append([J, K])
    for index, lst in enumerate(JK):
        for i, item in enumerate(lst):
            if i == 0:
                print(f'J{index + 1}')
            else:
                print(f'K{index + 1}')
            for j in item:
                print(*j)
            print()

main(Qt, Qt0, Qt1)
