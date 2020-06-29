#! /usr/bin/env python

import sys

for line in sys.stdin:
    word = ["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    label = ["0"]*len(word)
    line = line.strip()
    unpacked = line.split(" ")

    for item in unpacked:     # 扫描data里每一个字符
        for j in word:           # 扫描26个字母j
            if item == j:             # 如果第i个字符=字母j
                label[word.index(j)] = "1"         # 字母j所在排位对应到列表label上值取1
    print(",".join(label))