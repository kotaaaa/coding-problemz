import re


def is_num(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


def solution(file_object):
    lines = file_object.getvalue().split("\n")
    response = []
    for line in lines:
        if not is_num(line):
            continue
        if int(line) < -1000000000 or 1000000000 < int(line):
            continue
        response.append(int(line))
    return response


# Example usage:
#
# for i in solution(file_object):
#     print(i)
