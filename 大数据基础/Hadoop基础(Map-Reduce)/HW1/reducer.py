#!/usr/bin/env python

from operator import itemgetter
import numpy as np
import sys

lineword = [0,0,0,0,0,0,0,0,0,0]
current_word = None
current_count = 0
word = ["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

i=0

for line in sys.stdin:
    line = line.strip()    # 去掉空格
    line = line.split(",")   # 以“，”分割
    line = list(map(int, line))  # 将str转为int

    lineword[i] = line     # 将每行转为一个大的lineword列表，每元素是原先的一行
    i +=1 

for k in range(len(lineword)):
    for j in range(k):         # 不重复的j，k排列序列   代表相比较的两个字母
        add_line = np.array(lineword[k]) +np.array(lineword[j])     # 相比较的两个字母下朋友的代码之和 add_line
        add_line[j] = 0                          # add_line 中相比较两个字母对应值取0， 相同朋友值是2
        add_line[k] = 0
        same_index = np.where(add_line==2)[0]       # same_index 是相同朋友的序列号吗
        same = [0]*len(same_index)
        c = 0
        for l in same_index:
            same[c] = word[l]
            c += 1
        print(word[j],",",word[k],","," ".join(same))