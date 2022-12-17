#!/bin/bash

declare -i count=0
topLetter=''
declare -i newCount=0
string=$1

for (( i=0; i<${#string}; i++ ));
do
  letter=${string:$i:1} 
  echo "${newCount}"
   
  # check if it is the same as last character
  if [[ "$letter" == "$lastLetter" ]] || [ "$newCount" -eq 0 ]
  then
    #newCount=$(echo "${string}" | tr -cd $letter | wc -c |tr -d ' ') #count the number of times
    newCount=$(( newCount + 1))
    lastLetter=$letter
    if [ "$newCount" -gt "$count" ]
    then
        count=$newCount
        topLetter=$letter
    fi
   else
    newCount=0
  fi
done

echo "${topLetter},${count}"



