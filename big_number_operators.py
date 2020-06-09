number_1 = '9000000000000000000000000000000000000000000000000000000000000'
number_2 = '9000000000000000000000000000000000000000000000000000000000000'


def multiply_big_number(str_number1, str_number2) -> str:
    result = ''
    str_number1 = list(str_number1)
    str_number2 = list(str_number2)
    i = 0
    list_item = list()
    for i in range(1, len(str_number1) + 1):
        a = int(str_number1[0 - i])
        carry = 0
        item = ''
        for j in range(1, len(str_number2) + 1):
            b = int(str_number2[0 - j])
            c = a * b + carry
            carry = c // 10
            n = c % 10
            item = str(n) + item
        if carry != 0:
            item = str(carry) + item
        zero = "".zfill(i - 1)
        item += zero
        list_item.append(item)
        i += 1

    for i in range(1, len(list_item)):
        if i == 1:
            result = sum_big_number(list_item[0], list_item[1])
        else:
            result = sum_big_number(result, list_item[i])

    print(result)
    return result


def sum_big_number(str_number1, str_number2) -> str:
    size_1 = len(str_number1)
    size_2 = len(str_number2)
    loop = min(size_1, size_2)
    result = ''
    carry = 0
    for i in range(1, loop + 1):
        a = int(str_number1[-i])
        b = int(str_number2[-i])
        c = a + b + carry
        carry = c // 10
        n = c % 10
        result = str(n) + result
    if size_1 > loop:
        if carry > 0:
            result = sum_big_number(str_number1[:-loop], str(carry)) + result
        else:
            result = str_number1[:-loop] + result

    elif size_2 > loop:
        if carry > 0:
            result = sum_big_number(str_number2[:-(loop + 1)], str(carry)) + result
        else:
            result = str_number2[0:-loop] + result
    elif carry > 0:
        result = str(carry) + result
    return result


# print(sum_big_number('55', '55'))
multiply_big_number('999', '2')
