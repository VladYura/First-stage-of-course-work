# Словарь зависимостей исходного дерева
input_addictions = {
    'a1': ('a3', 'a2'), 'a2': ('a5', 'a4'), 'a3': ('a7', 'a6'), 'a4': ('a9', 'a8'), 'a5': ('a11', 'a10'),
    'a6': ('a13', 'a12'), 'a7': ('a15', 'a14'), 'a8': ('a1', 'a1'), 'a9': ('a1', 'a1'), 'a10': ('a1', 'a1'),
    'a11': ('a1', 'a1'), 'a12': ('a1', 'a1'), 'a13': ('a1', 'a1'), 'a14': ('a1', 'a1'), 'a15': ('a1', 'a1')
}
# Мой
start_tree = [
    ['a1', (0, 0)], ['a2', (0, 0)], ['a3', (0, 0)], ['a4', (0, 0)], ['a5', (0, 0)], ['a6', (0, 0)], ['a7', (0, 0)],
    ['a8', (0, 0)],
    ['a9', (0, 1)], ['a10', (0, 1)], ['a11', (0, 1)], ['a12', (0, 1)], ['a13', (0, 0)], ['a14', (0, 0)], ['a15', (0, 0)]
]
# Миша
# start_tree = [
#     ['a1', (0, 0)], ['a2', (0, 0)], ['a3', (0, 0)], ['a4', (0, 0)], ['a5', (0, 0)], ['a6', (0, 0)], ['a7', (0, 0)],
#     ['a8', (0, 0)],
#     ['a9', (0, 1)], ['a10', (0, 1)], ['a11', (0, 1)], ['a12', (0, 0)], ['a13', (0, 1)], ['a14', (0, 0)], ['a15', (0, 0)]
# ]
# Паша
# start_tree = [
#     ['a1', (0, 0)], ['a2', (0, 0)], ['a3', (0, 0)], ['a4', (0, 0)], ['a5', (0, 0)], ['a6', (0, 0)], ['a7', (0, 0)],
#     ['a8', (0, 0)],
#     ['a9', (0, 1)], ['a10', (0, 1)], ['a11', (0, 1)], ['a12', (0, 0)], ['a13', (0, 1)], ['a14', (0, 0)], ['a15', (0, 0)]
# ]
# Саня
# start_tree = [
#     ['a1', (0, 0)], ['a2', (0, 0)], ['a3', (0, 0)], ['a4', (0, 0)], ['a5', (0, 0)], ['a6', (0, 0)], ['a7', (0, 0)],
#     ['a8', (0, 1)],
#     ['a9', (0, 1)], ['a10', (0, 1)], ['a11', (0, 0)], ['a12', (0, 0)], ['a13', (0, 0)], ['a14', (0, 0)], ['a15', (0, 1)]
# ]
