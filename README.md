# HAC Tester
A program that was written in python to help the students in my college in their homework

With this program you can:
1. Make test files, for both your sol and teacher sol
2. Diff between yor sol, and teacher sol
3. Tar your files

## How to Use ##
Copy and paste the runner.py in your NoMachine, and run it using terminal
For example: python ruuner.py

You can choose different actions from the menu so it's fairly easy to use.

IMPORTANT: All files must be in the same directory where the runner.py is.

## Making Tests ##

After selecting the first option, you will have 3 options:
1. Teacher Tests
2. Your Tests
3. Both

Teacher Sol must end with sol in the end of its name, example: ex1asol
Your Sol must be the same name but without sol uin the end of it, example: ex1a
And finally .in files must have a valid name, example:
  * `ex1a_test00.in`


After you select which sol you want to make tests for, you will get .out files.

## Diff between tests ##

If you have all of your .out files in the same directory, and you have made the tests using this program, then its easy to do diffs.
All you got to do is just run the program and select the second option, which is making diff.
Then the program will tell you if there is any problems in your sol compared to teacher's sol, example:
 * `Problem in ex1a_test00.in`
Beaware that white spaces and newlines DO count as mistake (the college also counts that as a mistake)
If there isn't any problems you will get a message accordingly.

## Taring your files ##
sss
