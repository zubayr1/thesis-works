Prover has to provide a list of variables (VAR) and a list of instructions (INS).

Each element in the lists should be from the concatinated list created by appending locking script (LS) and unlocking script (US) together.

In order to make sure rearranging the VAR and INS into a script format will give the result as (LS || US), prover must also provide a varformat list.

varformat is a binary array comprised with 0s and 1s where 1 in ith position signifies that a variable should be in the ith format in the rearranged list made from VAR and INS.


The prover also needs to provide a PROVERINPUT list.

Let's assume a run() function which takes VAR list and INS list such that:

#### run(VAR, INS):
for each instruction in INS, it will perform a certain operation (ADD, EQUAL, DUP etc) on one or multiple number of variables from VAR list (taking from 0th element in the VAR list)
and will append the output to the end of a RESULT list.
At the end the function will return the RESULT list.


In order for the prover to prove the statement completely, RESULT must be equal to PROVERINPUT


### Given public values
LSCOMM, USCOMM

### I know 
a set of variables VAR, a set of instructions INS, the varformat, the scripts LS & US, salts LSSALT, USSALT, the input list PROVERINPUT

### such that

1. varformat has all values either 0 or 1

2. numberof(1's) in varformat == len(VAR)

3. numberof(0's) in varformat == len(INS)

4. Arrange((VAR || INS), varformat) == LS||US 

5. LSCOMM = COMM(LS, LSSALT)

6. USCOMM = COMM(US, USSALT)

7. PROVERINPUT = run(VAR, INS)

8. True = PROVERINPUT[len(PROVERINPUT)-1]

