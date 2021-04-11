#!/bin/bash

myvar=`cat`

eval "curl -X POST  -d 'email="$1"@"$2"\&letter="$myvar"' http://procagent.antispam-msu.site/classificator"
