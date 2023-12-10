# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
pages = 100
strings = 50
symbols = 25
volume *= 1024 * 1024
book = pages * strings * symbols * 4
print("Количество книг, помещающихся на дискету:", round(volume // book))
