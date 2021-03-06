"""
------------------------------- Задание -------------------------------
Если записать числа от 1 до 5 английскими словами (one, two, three,
four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one
thousand) включительно?
Примечание: Не считайте пробелы и дефисы. Например, число 342 (three
hundred and forty-two) состоит из 23 букв, число 115 (one hundred and
fifteen) - из 20 букв. Использование "and" при записи чисел
соответствует правилам британского английского.
"""

len_nums = {
    "1-9": 36, "11-19": 67, "10": 3, "20": 6, "30": 6, "40": 5, "50": 5,
    "60": 5, "70": 7, "80": 6, "90": 6, "100": 7, "1000": 8, "1-99": 0,
    "1-999": 0, "and": 3
}
len_nums["1-99"] = (
        len_nums["1-9"]*9 + len_nums["10"] + len_nums["11-19"] +
        len_nums["20"]*10 + len_nums["30"]*10 + len_nums["40"]*10 +
        len_nums["50"]*10 + len_nums["60"]*10 + len_nums["70"]*10 +
        len_nums["80"]*10 + len_nums["90"]*10
)
len_nums["1-999"] = (
    len_nums["1-9"]*100 + len_nums["100"]*9 + (len_nums["100"] + len_nums["and"])*891 + len_nums["1-99"]*10
)
print(__doc__)
print("Ответ:", len_nums["1-999"] + len_nums["1000"] + 3)

