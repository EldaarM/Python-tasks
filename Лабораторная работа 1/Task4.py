users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
visits["Общее количество"] = len(users)
visits["Уникальные посещения"] = len(set(users))
print(visits)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
