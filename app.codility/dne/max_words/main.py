# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re


def solution(S):
    # write your code in Python 3.8.10
    sentences = re.split("[.?!]", S)
    max_words = 0
    for sen in sentences:
        max_words = max(max_words, len(sen.split()))
    return max_words
