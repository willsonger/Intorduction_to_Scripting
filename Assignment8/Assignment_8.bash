#!/bin/bash

echo "#################### P1.1 While Loop ##################"
#Initiatlize counter
n=1
#interate the counter to 15
while [ $n -le 15 ]
do
	if [ $n == 16 ]
	then
		echo "terminated"
		break
	fi
	echo "while loop $n"
	(( n++ ))
done
echo "#################### P1.2 Until Loop ###################"
n=0
until false
do
	((n++))
	if [[ $n -eq 5 ]]
	then
		continue
	elif [[ $n -ge 16 ]]
	then
	break
	fi
	echo "until Loop $n"
done
echo "#################### P1.3 For loop ####################"
for ((n=1; n<=15;n++));
do
	echo "for loop $n"
done
echo "############### P2.1 While Loop Summation ##############"

num=20
total=0
while [ $num -le 40 ]
do
	let "total+=num"
	let "++num"
done

echo "The summation of dogots between 20 and 40"
echo "using a while loop is: $total"

echo "############## P2.1 Until loop Summation ##############"
#num=20
#total=0
#until [ $n -eq $t ]
#do
#	let "n+=2"
#done
#echo "the summation of digits between 20 and 40"
#echo "using a until loop is $n"

echo "############## P2.3 For loop Summation ################"

arr=( 20 21 22 23 24 25 26 27 28 29 30
	31 32 33 34 35 36 37 38 39 40 )
sum=0
for i in "${arr[@]/#-*}"; 
do
	(( sum+=i ))
done

echo "The summation of digits between 20 and 40"
echo "using a for loop is: $sum"

echo "####### P3.1 Prime numbers using a while loop ########"
echo "###### P3.2 Prime numbers using a until loop ########"

x=2
until [ $x -gt 50 ]
do
	i=2
	flag=1 #Prime numbers cannot be divided by 2
	while [ $i -le $((x/2)) ]
	do
		if [ $((x%i)) -eq 0 ]
		then
			flag=0
			break
		fi
		((i++))
	done
		if [ $flag - eq 1 ]
		then
			echo "Prime is: $x"
		fi
		((x++))
done
echo "######### P3.3 Prime numbers using a for loop #########"
for ((i=1; i<=50; i++))
do
	output=$(( $i % 2))
	
	if [ $output -ne 0 ]

	then
	echo "prime: $i"
	fi
done


echo "################### P 4 #######################"
echo " Please enter the campus you are enrolled at: corpus, Kingsville, commerce: "
read campus

case $campus in
	"corpus") echo "Texas A&M University Corpus Christi"
		;;
	"Kingsville") echo "Texas A&M University Kingsville" 
		;;
	"commerce") echo "Texas A&M University Commerce" 
		;;
	*) echo "Texas A&M University"
		;;
esac	

varTest=150

if [[ $varTest -ge 1 && $varTest -le 10 ]] ; then
	echo 'between 1 and 20" 

elif [[ $varTest -ge 11 && $varTest -le 20 ]] ; then 
	echo "between 11 and 20"

elif [ $varTest -gt 20 ] ; then 
	echo " Greater than 20"

else 
	echo "less then 1"
fi









