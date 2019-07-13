# Python-Programs

<br><b>Problem 1: Biggest integer which has maximum digit sum in range from 1 to n</b></br>
Tom has an integer n.  He is interested in knowing what positive integer k, which does not exceed n, has the maximum sum of digits. Help him write a program which can find k. If there are several such integers, determine the biggest of them.

<b>Input</b>
The only line contains the positive integer n.

<b>Output</b>
Print the positive integer which does not exceed n and has the maximum sum of digits.

<b>Constraints</b>
1 ≤ n ≤ 1018

<b>Example#1</b>
Input
100
Output
99
9 + 9 = 18.

<b>Example#2</b>
Input
48
Output
48
4 + 8 = 12.




<br><b>Problem 2: Maximal number</b></br>
You are given a string consisting of n digits ('1', '2', '3', ..., '9'). Rearrange the digits to form the maximum possible number.

<b>Input</b>
The first line of input contains an integer n, the length of the given string.
The second line of input contains a string.

<b>Output</b>
Print the string after rearranging its digits.

<b>Constraints</b>
1 <= n <= 100

<b>Example#1</b>
Input
3
231
Output
321
Explanation: We can form the following numbers: 231, 213, 132, 123, 321, 312. The largest is 321.
<b>Example#2</b>
Input
2
12
Output
21
Explanation: We can form the following numbers: 12 and 21. The largest is 21.


<br><b>Problem 3: Larger lettersr</b></br>
You are given a string consisting of n lowercase Latin letters. You must find the count of number of larger alphabets for every character of the string (according to lexicographical order).

<b>Input</b>
The first line of input contains an integer n, the length of the given string.
The second line of input contains a string.

<b>Output</b>
Print the count of number of larger alphabets for every character of the string on a single line. Separate elements by white spaces.

<b>Constraints</b>
1 <= n <= 100

<b>Example#1</b>
Input
3
abc
Output
2 1 0
Explanation: a - 2: 'a' < 'b', 'a' < 'c'. 'b' - 1: 'b' < 'c'. 'c' - 0: There is no letter in this string, which is larger than 'c'.
<b>Example#2</b>
Input
5
aaabb
Output
2 2 2 0 0
Explanation: a - 2: 'a' < 'b' (b at index 3 and index 4). There is no letter in this string, which is larger than 'b'.
