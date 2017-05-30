#2个数据源的例子，一个是user信息，一个是购买的food信息

#删除已有文件夹
hadoop fs -rmr /sxydata/input/example_3
hadoop fs -rmr /sxydata/output/example_3_1
hadoop fs -rmr /sxydata/output/example_3_2

#创建输入文件夹
hadoop fs -mkdir /sxydata/input/example_3

#放入输入文件
hadoop fs -put user.txt food.txt /sxydata/input/example_3

#查看文件是否放好
hadoop fs -ls /sxydata/input/example_3

#本地测试一下map和reduce
cat user.txt food.txt | python stage1_mapper.py | sort | python stage1_reducer.py | python stage2_mapper.py | sort | python stage2_reducer.py

#集群上跑任务
hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -Dmapred.reduce.tasks=1 -Dstream.num.map.output.key.fields=2 -file stage1_mapper.py -mapper stage1_mapper.py  -file stage1_reducer.py -reducer stage1_reducer.py -input /sxydata/input/example_3 -output /sxydata/output/example_3_1

hadoop jar /home/ds/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -Dmapred.reduce.tasks=1 -Dstream.num.map.output.key.fields=2 -file stage2_mapper.py -mapper stage2_mapper.py  -file stage2_reducer.py -reducer stage2_reducer.py -input /sxydata/output/example_3_1 -output /sxydata/output/example_3_2