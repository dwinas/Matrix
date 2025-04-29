
import math
import os
import random
import re
import sys



matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
text = []

for i in range(len(matrix[0])):

    for line in matrix:
        text.append(line[i])


text = "".join(text)

matrix = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', text)

print("Text: ", matrix)