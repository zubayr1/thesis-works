Problem statement (specific):

Given 3 values s1, s2, s3 and 2 instructions i1 (add) and i2(equal)
    check if [s1 i1 s2 i2 s3] (in other words, s1 + s2 == s3)



Problem statement (generic): (also possible with the given code)

Given N values s1, s2, s3, ... , sN and (N-1) instructions i1-iN-1 (add) and iN(equal)
    check if [s1 i1 s2 i2 s3 ... iN-1 sN] (in other words, s1 + s2 + ... + sN-1 == sN)


main():
created by user. variable and instructions are given as arguments.
LEN: length of instructions (to be provided by user as well since zokretes does not allow array length from argument to be used as loop upper-bound)

stack: to be provided by user to indicate how many variables are taken per instruction.
As in the code, 
u32[4] stack = [2,2,2,2]
As you can see, stack length is same as INS length (which is same as LEN)
stack[0] = 2 means the first INS takes 2 variables for its operation (as in this case INS[0] is add; which takes 2 variables si and sj)

main function calls run()


run() - setres():
All these functions, unlike main() are fixed and we can create a library/ module using these (user can import it and use it with the main function defined by him)

run():
calls the operator() function

operator():
this is the most important function where all the operations will take place.
Since zokrates does not allow string argument, instructions are passed using u64 values
in this code, 0x0000000000000001 is used for EQUAL and 0x0000000000000002 is used for ADD
this function uses a RES array (which is initially same as the VAR array) to store operation results

setres():
This function is used to make left shift on RES array.
For example, if initially we have 
RES = VAR = [1,2,3,4]
after the first ADD instruction we change the RES as:
RES = [(1+2),3,4,4]
So basically, we store the result of ADD operation of the first 2 varaibles into the RES[0] and the use left shift to the next elements.


Flow of the result using an example:
say VAR = [1,2,3,6] INS = [2,2,1]
RES = VAR = [1,2,3,6]
iterate#1: INS[0] -> 2: ADD :- RES = [3,3,6,6]
iterate#1: INS[1] -> 2: ADD :- RES = [6,6,6,6]
iterate#1: INS[2] -> 1: EQUAL :- RES = [0,6,6,6] (for EQUAL instruction in operation, if RES[0]==RES[1] then replace the first element in RES with 0)



Finally in main() we check the RES[0] if its equal to 0:
assert(RESULT[0] == 0);
If so, we can conclude that our assertion (in this particular porblem sum of first N-1 variables is equal to the last element)
