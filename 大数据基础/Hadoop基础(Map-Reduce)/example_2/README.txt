#这个例子是统计人造草坪和天然草坪的数量 i.e. 找“True”and“False”


#Hadoop之前，本地测试一下map和reduce
head -20 stadiums.csv | python mapper.py | sort | python reducer.py
head -20 stadiums.csv | python lower_mapper.py | sort


#删除已有文件夹
hadoop fs -rmr /sxydata/input/example_2
hadoop fs -rmr /sxydata/output/example_2

#创建输入文件夹
hadoop fs -mkdir /sxydata/input/example_2

#放入输入文件
hadoop fs -put stadiums.csv /sxydata/input/example_2

#查看文件是否放好
hadoop fs -ls /sxydata/input/example_2

#集群上跑任务
hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py -input /sxydata/input/example_2 -output /sxydata/output/example_2

hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
    -file mapper.py \
    -mapper mapper.py	\  
    -file reducer.py 	\
    -reducer reducer.py \
    -input /sxydata/input/example_2  \
    -output /sxydata/output/example_2