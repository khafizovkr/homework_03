# for pull request
#первая часть
def int_func1(word):
    return ''.join([word[0].upper(), word[1:]])


result = []


def int_func2(word):
    for i in range(len(word)):
        letter = word[i].upper() if i == 0 else word[i]
        result.append(letter)
    return ''.join(result)


def int_func3(word):
    return word.capitalize()


print((int_func1('text')))
print((int_func2('text')))
print((int_func3('text')))

#вторая часть
result = []
def int_func4(word):
    words = word.split()
    for word in words:
        words = ''.join([word[0].upper(), word[1:]])
        result.append(words)
    return ' '.join(result)


def int_func5(word):
    return word.title()


print((int_func4('a b c d e text')))
print((int_func5('a b c d e text')))

#задача через ord(), chr(ord(...)) можно заменить на word[].upper
result = []


def int_func6(word):
    i = 0
    while i < len(word):
        if i == 0:
            letter = chr(ord(word[i]) - 32)
            i += 1
        elif word[i] == ' ':
            letter = ' ' + chr(ord(word[i+1]) - 32)
            i += 2
        else:
            letter = word[i]
            i += 1
        result.append(letter)
    return ''.join(result)


print((int_func6('a b c d e text')))