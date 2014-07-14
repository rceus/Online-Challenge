Online-Challenge
================

Challenge 1
===========

Given a list of integers, your task is to write a program to output an integer-valued list of equal length such that the output element at index 'i' is the product of all input elements except for the input element at 'i'.
In other words, let inputArray by an integer array of length 'n'. The solution,computed into outputArray, would be:

As an example, if inputArray = { 1, 2, 3, 4 }, then

outputArray = { 2*3*4, 1*3*4, 1*2*4, 1*2*3 }.

Your program should run in O(n) time and should be space efficient.

Constraint

The input array size will always have at least two elements in it, that is, n >= 2.
The product of any subset of the input will never exceed the value of a 64 bit integer.
The maximum length of input array is 1000.


Challenge 2
===========
Frequency Counting of Words / Top N words in a document. Given N terms, your task is to find the k most frequent terms from given N terms.

Input format

First line of input contains N, denoting the number of terms to add. 

In each of the next N lines, each contains a term.

Next line contains k, most frequent terms.

Output format

Print the k most frequent terms in descending order of their frequency. If two terms have same frequency print them in lexicographical order.

Sample input

14

Fee

Fi

Fo

Fum

Fee

Fo

Fee

Fee

Fo

Fi

Fi

Fo

Fum

Fee

3

Sample output

Fee

Fo

Fi

Constraint

0 < N < 300000, 
0 < term length < 25.

