#!/bin/bash

time curl -v -X POST http://localhost:9999/blazegraph/namespace/ships/sparql --data-urlencode "query=`cat sparql/masters.rq`" -H 'Accept:text/csv' > /tmp/results.csv

exit;
cat ~/Downloads/masters\(1\).csv | while read line;
do
	num=`echo $line |sed 's/_vtls.*$//g'|sed 's/^<file:\/\/File_//g'`
	major_no=`echo $num |sed 's/-.*$//g'`
	minor_no=`echo $num |sed 's/^.*-//g'`
	#echo "major $major_no minor $minor_no -$num-"
	printf "%03d%02d:%s\n" "$major_no" "$minor_no" "$line"
done |sed 's/T00:00:00.000Z//g' |sort -n |sed 's/^[0-9][0-9]*://g' > /tmp/master_sorted.csv
