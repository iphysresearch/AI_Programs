有如下的数据，其中第一列为用户ID，后面数列为他的朋友ID

A B C D E F 
B A H C D E I
C B E G A J
D A B E 
E H A B C D G
F A J G
G C E F I
H B J E
I G B
J H C F

编写map-reduce任务完成：找到所有有共同朋友的用户ID对
生成格式为 (用户ID,用户ID 共同朋友ID)

B,C A
D,A E


# cat data.txt | python3 mapper.py | python3 reducer.py