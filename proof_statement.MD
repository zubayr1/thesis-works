Prover has to provide a list of variables (VAR) and a list of instructions (INS).

Each element in the lists should be from the concatinated list created by appending locking script (LS) and unlocking script (US) together.

In order to make sure rearranging the VAR and INS into a script format will give the result as (LS || US), prover must also provide a var_format list.

var_format is a binary array comprised with 0s and 1s where 1 in ith position signifies that a variable should be in the ith format in the rearranged list made from VAR and INS.



### Given public values
var_com & ins_com

### I know 
a set of variables VAR, a set of instructions INS and salts VARsalt, INSsalt

### such that

1. var_com = COMM(VAR || VARsalt)

2. ins_com = COMM(INS || INSsalt)

3. RUN(VAR, INS) will return an array RESULT s.t. RESULT[0] = 0