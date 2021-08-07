import re


def getList(struct):
    lst = []
    for i in range(len(struct)):
        string = ''
        for j in range(len(struct[i])):
            string += struct[i][j]
            if j != len(struct[i]) - 1:
                string += ' '
        lst.append(string)
    return lst


def getDates(text):
    dates = [
        re.findall(r'\d{2}\.\d{2}\.\d{4}', text),
        getList(re.findall(r'(\d{1,2})\s(янв(?:аря)?|фев(?:раля)?|мар(?:та)?|апр(?:еля)?|мая|июн(?:я)?|июл(?:я)?|'
                           r'авг(?:уста)?|сен(?:тября)?|окт(?:ября)?|ноя(?:бря)?|дек(?:абря)?)\s(\d{4})', text)),
        getList(re.findall(r'(\d{1,2})\s(января|февраля|марта|апреля|мая|июня|июля|'
                           r'августа|сентября|октября|ноября|декабря)(?!\s\d{4})', text))
    ]

    return dates


def readFromFile():
    with open('tests', 'r', encoding='utf-8') as file:
        f = file.read().splitlines()
    return f


tests = readFromFile()
for g in range(len(tests)):
    print("\nИсходный текст: " + tests[g])
    print("Результат: " + str(getDates(tests[g])) + "\n")
