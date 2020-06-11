from datetime import datetime

number_1 = '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
number_2 = '888888888888888888888888888999999999999999999999999999999999999999999999999999999999999999999999999999999'


def multiply_big_number(str_number1, str_number2) -> str:
    result = ''
    i = 0
    list_sub_number = list()
    for i in range(1, len(str_number1) + 1):
        a = int(str_number1[0 - i])
        carry = 0
        sub_number = ''
        for j in range(1, len(str_number2) + 1):
            b = int(str_number2[0 - j])
            c = a * b + carry
            carry = c // 10
            n = c % 10
            sub_number = str(n) + sub_number
        if carry != 0:
            sub_number = str(carry) + sub_number
        zero = "0" * (i - 1)
        sub_number += zero
        list_sub_number.append(sub_number)
        i += 1

    for i in range(1, len(list_sub_number)):
        if i != 1:
            result = sum_big_number(result, list_sub_number[i])
        else:
            result = sum_big_number(list_sub_number[0], list_sub_number[1])

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
start_time = datetime.now().timestamp()
multiply_big_number(number_1, number_2)
end_time = datetime.now().timestamp()
print('total run-time: %f ms' % ((end_time - start_time) * 1000))
