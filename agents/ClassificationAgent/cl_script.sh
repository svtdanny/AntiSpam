#!/bin/bash

myvar1=`cat`
myvar2=$(echo "$myvar1"|tr -d \''"')

echo $myvar2 >> r.txt
eval "curl -X POST  -d 'email="$1"@"$2"\&letter="$myvar2"' http://procagent.antispam-msu.site/classificator"
