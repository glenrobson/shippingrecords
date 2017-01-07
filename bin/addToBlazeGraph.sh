#!/bin/bash

ls $1 | while read line; 
do
	echo "loading $line"
	curl -v -X POST -H 'Content-Type:application/rdf+xml' --data @"$1/$line" "http://localhost:9999/blazegraph/namespace/ships/sparql?context-uri=file://$line"
done

#file://File_1-8_vtls004583639.xml]
#java.util.concurrent.ExecutionException: java.lang.RuntimeException: java.util.concurrent.ExecutionException: java.lang.IllegalArgumentException: Not a legal boolean value:
