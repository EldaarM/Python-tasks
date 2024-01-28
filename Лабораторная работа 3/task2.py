# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, divider=','):
    p_list = []
    first_str = participants_first.split(divider)
    second_str = participants_second.split(divider)
    for i in range(len(first_str)):
        for j in range(len(second_str)):
            if first_str[i] == second_str[j]:
                p_list.append(first_str[i])
    p_list.sort()
    return p_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
