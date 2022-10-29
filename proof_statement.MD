Prover has to provide a list of variables (VAR) and a list of instructions (INS).

Each element in the lists should be from the concatinated list created by appending locking script (LS) and unlocking script (US) together.

In order to make sure rearranging the VAR and INS into a script format will give the result as (LS || US), prover must also provide a var_format list.

var_format is a binary array comprised with 0s and 1s where 1 in ith position signifies that a variable should be in the ith format in the rearranged list made from VAR and INS.



### Given public values
LSCOMM, USCOMM

### I know 
a set of variables VAR, a set of instructions INS, the varformat, the scripts LS & US, salts LSSALT, USSALT

### such that

1. varformat has values all 0 or 1

2. number(1's) in varformat == len(VAR)

3. num(0's) in varformat == len(INS)

4. Arrange((VAR || INS), varformat) == LS||US 

5. LSCOMM = COMM(LS, LSSALT)

6. USCOMM = COMM(US, USSALT)

