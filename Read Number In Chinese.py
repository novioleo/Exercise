# Read Number in Chinese (25)
# https://www.nowcoder.com/pat/1/problem/4312
# 时间限制 1000 ms 内存限制 65536 KB 代码长度限制 100 KB 判断程序 Standard (来自 小小)
# 题目描述
# Given an integer with no more than 9 digits, you are supposed to read it in the traditional Chinese way.  Output "Fu" first if it is negative.  For example, -123456789 is read as "Fu yi Yi er Qian san Bai si Shi wu Wan liu Qian qi Bai ba Shi jiu".  Note: zero ("ling") must be handled correctly according to the Chinese tradition.  For example, 100800 is "yi Shi Wan ling ba Bai".
#
# 输入描述:
# Each input file contains one test case, which gives an integer with no more than 9 digits.
#
#
# 输出描述:
# For each test case, print in a line the Chinese way of reading the number.  The characters are separated by a space and there must be no extra space at the end of the line.
#
# 输入例子:
# -123456789
#
# 输出例子:
# Fu yi Yi er Qian san Bai si Shi wu Wan liu Qian qi Bai ba Shi jiu


name_value = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba',
              '9': 'jiu'}


def four_number(num, header=False):
    unit_value = ['', ' Shi', ' Bai', ' Qian']
    num_value = int(num)
    num = str(num_value)
    if num_value == 0:
        return ['ling', ]
    to_return = []
    if num_value < 1000 and header:
        to_return.append('ling')
    first_flag = True
    for i in range(0, len(num)):
        # first occur non-zero number
        if num[-i - 1] != '0' and first_flag:
            first_flag = False
        if not first_flag:
            if num[-i - 1] == '0':
                to_insert = 'ling'
            else:
                to_insert = name_value[num[-i - 1]] + unit_value[i]
            if len(to_return) == 0 or not (to_insert == to_return[0] == 'ling'):
                to_return.insert(int(num_value < 1000 and header), to_insert)
    return to_return


number = str(int(input()))
if number == '0':
    print('ling')
else:
    negative = number[0] == '-'
    if negative:
        number = number[1:]
    unit_value_2 = ['', 'Wan', 'Yi']
    to_display = []
    count = 0
    while True:
        flag = True
        if len(number) < 4:
            flag = False
        if number == '':
            break
        t = number[-4:] if len(number) > 4 else number
        part = four_number(t, flag)
        if len(to_display) == 0 and part == ['ling', ]:
            pass
        elif not (len(to_display) > 0 and to_display[0] == part[0] == 'ling'):
            to_display = part + ([unit_value_2[count], ] if int(t) > 0 else []) + to_display
        if not flag:
            break
        number = number[:-4]
        count += 1

    print(('Fu ' if negative else '') + ' '.join(to_display).strip())
