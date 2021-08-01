def arithmetic_arranger(problems, show=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        n1 = [x.split(' ')[0] for x in problems]
        n2 = [x.split(' ')[2] for x in problems]
        operands = [x.split(' ')[1] for x in problems]
        if '*' in operands or '/' in operands:
            return "Error: Operator must be '+' or '-'."
        elif False in [x.isdigit() for x in n1 + n2]:
            return "Error: Numbers must only contain digits."
        elif max([len(x) for x in n1 + n2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            results = [eval(x) for x in problems]
            riga_1, riga_2, riga_3, riga_4 = '', '', '', ''
            for i in range(len(operands)):
                l1 = len(n1[i])
                max_l = max([len(x) for x in [n1[i], n2[i]]])
                max_chars = max_l + 2
                riga_1 += f'{n1[i].rjust(max_chars)}    '
                riga_2 += f'{str(operands[i] + " ") + str(n2[i]).rjust(max_l)}    '
                riga_3 += '-' * (max_l + 2) + '    '
                riga_4 += f'{str(results[i]).rjust(max_chars)}    '
            if show:
                final = riga_1.rstrip() + "\n" + riga_2.rstrip() + "\n" + riga_3.rstrip() + "\n" + riga_4.rstrip()
                return final
            else:
                final = riga_1.rstrip() + "\n" + riga_2.rstrip() + "\n" + riga_3.rstrip()
                return final


print(arithmetic_arranger(['1932 + 54', '12 + 233', '89 - 51236', '13 + 89'], show=True))