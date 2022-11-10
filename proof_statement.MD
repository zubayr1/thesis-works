Prover has to provide a list of variables (VAR) and a list of instructions (INS).

Each element in the lists should be from the concatinated list created by appending locking script (LS) and unlocking script (US) together.

In order to make sure rearranging the VAR and INS into a script format will give the result as (LS || US), prover must also provide a var_format list.

var_format is a binary array comprised with 0s and 1s where 1 in ith position signifies that a variable should be in the ith format in the rearranged list made from VAR and INS.


The prover also needs to provide a PROVERINPUT list.

When running the variable list VAR and instruction list INS, 
for each instruction ins from INS, a specific operation (ADD, EQUAL, DUP etc) will be performed with one or more varaible from the VAR list
and the corresponding result will be appended in a RESULT list.

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

