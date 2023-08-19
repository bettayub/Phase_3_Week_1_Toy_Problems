# Project Name

## Phase 3 Week 1(Toy Problems)

# Author

## Bett Ayub

## Project Description

### Phase 3 Week 1(Toy Problems)
 

Prerequisite
1. Create a repository on your GitHub account.

2. Use Python to wire down the solution.

3. Push the solution to the above repository once done.

4. Submit the repository link for grading

5. Ensure your repository has a well written README.

 

NOTE: You are required to complete ALL the challenges
 

Challenge 1: Converting 12-hour time to 24-hour time
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

Notes
By convention, noon is 12:00 pm, and midnight is 12:00 am.

On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015. 

 

Challenge 2: Two numbers are positive.
Task:
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

Examples:
(2, 4, -3) == True

(-4, 6, 8) == True

(4, -6, 9) == True

(-4, 6, 0) == False

(4, 6, 10) == False

(-14, -3, -4) == False

 

Challenge 3: Consonant value
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

Examples;
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

## Project SetUp and Instructions

### To set up and run the project follow the below steps
```

git remote add origin git@github.com:bettayub/Phase_3_Week_1_Toy_Problems.
git init
git add <filename>
git commit -m "initial commmit"
git push origin master

```
### Technologies Used
```
python
Git 
Vscode
Github
```
# Installation

```

https://github.com/bettayub/Code_Challenge_Bot_Battlr
cd path/to/your/directory
git clone repository_url
cd repository_name
pip install -r requirements.txt
python3 Time.py
python3 Constant_value.py
python3 Numbers.py

```
# Support and Contacts
## You can reach me on bettayub19@gmail.com


# License

Copyright (c) 2023 Bett Ayub Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.