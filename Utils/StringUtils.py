import re


def split(string):
    splitted = []
    tmp = ""
    for i in range(len(string)):
        if i > 2 and ("А" <= string[i] <= "Я" or "A" <= string[i] <= 'Z') and (
                (string[i - 1] == " " and string[i - 2] in [',', '?']) or string[i - 1] in [',', '?']):
            splitted.append(tmp)
            tmp = string[i]
        elif string[i] == '.':
            splitted.append(tmp)
            tmp = ''
        else:
            tmp += string[i]
    if tmp != '':
        splitted.append(tmp)
    return splitted


def processStringList(strs: list) -> list:
    lines = []
    for line in strs:
        lines.extend(split(str(line)))
    for i in range(len(lines)):
        if 'і' in lines[i]:
            lines[i] = ""
        lines[i] = re.sub('[^а-яА-Яёa-zA-Z ]+', ' ', lines[i])
        lines[i] = ' '.join([x for x in lines[i].split(' ') if x.rstrip() != ""])
        if len(lines[i]) < 10:
            lines[i] = ""
        # print(lines[i])
    lines = [x for x in lines if x.rstrip() != ""]
    return lines
