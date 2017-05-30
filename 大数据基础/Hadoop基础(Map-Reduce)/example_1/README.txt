##############################################
# 终端
less text1.txt

wc -l text1.txt

head -10 text.txt

# Hadoop之前，本地测试一下map和reduce
# 以cat的方式，把文件中的数据一行一行的喂给 count_mapper.py，同时排个序
cat text1.txt| head -4 | python2 count_mapper.py

cat text1.txt | python2 count_mapper.py | head -4

# 文件过大的话，可以取一部分看写的map对不对，同时排序
head -50 text1.txt > tmp
cat tmp | python2 count_mapper.py | sort

# 开始聚合
cat tmp | python2 count_mapper.py | sort | python2 count_reducer.py


#############################################

#删除已有文件夹
hadoop fs -rmr /sxydata/input/example_1
hadoop fs -rmr /sxydata/output/example_1

#创建输入文件夹
hadoop fs -mkdir /sxydata/input/example_1

#放入输入文件
hadoop fs -put text* /sxydata/input/example_1

#查看文件是否放好
hadoop fs -ls /sxydata/input/example_1

#本地测试一下map和reduce
head -20 text1.txt | python count_mapper.py | sort | python count_reducer.py

#集群上跑任务
hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file count_mapper.py -mapper count_mapper.py  -file count_reducer.py -reducer count_reducer.py -input /sxydata/input/example_1 -output /sxydata/output/example_1

hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -file count_mapper.py \
    -mapper count_mapper.py  \
    -file count_reducer.py \
    -reducer count_reducer.py  \
    -input /sxydata/input/example_1  \
    -output /sxydata/output/example_1
    
