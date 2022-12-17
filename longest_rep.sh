#!/bin/bash

declare -i count=0
topLetter=''
declare -i newCount=0
string=$1

# loop through all chars
for (( i=0; i<${#string}; i++ ));
do
  letter=${string:$i:1} 

  # check if it is not the same as last character, and set count to 1 if it is
  if [[ "$letter" != "$lastLetter" ]]
  then
    newCount=1
    lastLetter=$letter
   else 
   newCount=$(( newCount + 1))
   lastLetter=$letter
  fi
  if [ "$newCount" -gt "$count" ]
    then
        count=$newCount
        topLetter=$letter
    fi
done



# return the top repeated value
echo "${topLetter},${count}"



