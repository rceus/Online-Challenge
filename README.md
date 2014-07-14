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


