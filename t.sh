#!/usr/bin/env bash


#echo "create 'fckup02','fc1'" | hbase shell -n

#hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator="," -Dimporttsv.columns=HBASE_ROW_KEY,fc1:ename,fc1:designation,fc1:manager,fc1:hire_date,fc1:sal,fc1:deptno fckup02 demo/sample_data.csv

echo "scan 'fckup02'" | hbase shell -n

'$(hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator="," -Dimporttsv.columns=HBASE_ROW_KEY,fc1:ename,fc1:designation,fc1:manager,fc1:hire_date,fc1:sal,fc1:deptno fckup02 demo/sample_data.csv)'