#!/bin/bash

#changed y to b in line 8 to account for 2nd variable b.
echo "Enter number"
read a
echo "Enter second number"
read b
(( sum=a+b ))
echo "The total is $sum"
