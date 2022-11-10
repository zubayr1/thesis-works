def run(VAR, INS):
    RESULT = []
    
    for i in INS:
        if i==2: ##ADD##
            addres = VAR[0]+VAR[1]
            RESULT.append(addres)            
            VAR.pop(0)
            VAR.pop(0)
            VAR.insert(0, addres)
            
        elif i==1: ##EQUAL##
            RESULT.append(VAR[0]==VAR[1])
            VAR.pop(0)
            VAR.pop(0)
            
        elif i==3: ##DUP##
            RESULT.append(VAR[0])
    return RESULT, VAR

def checkHash(arr, hashValue, SALT):
    string = ""
    for i in arr:
        string+= str(i)
    return string+SALT==hashValue ## check if locking/ unlocking script is same as hashvalue##

def reArrangeFun(VAR, INS, varformat):
    reArranged = []
    for i in range(0, len(varformat)):
        if varformat[i] == 1:
            reArranged.append(VAR.pop(0))
        else:
            reArranged.append(INS.pop(0))
    
    return reArranged

def mergeScrpitsFun(LS, US):
    return LS + US

def checkformat(VAR, INS, varformat):
    check=1
    
    varcount=0
    inscount=0
        
    
    for i in varformat:
        if i==1:
            varcount+=1
        elif i==0:
            inscount+=1
        elif i!=0 and i!=1: ## check if varformat all 0 or 1##
            check=0
            
    if varcount!=len(VAR): ##check if num(1's) == len(VAR)##
        check=0
    if inscount!=len(INS): ##check if num(0's) == len(INS)##
        check=0
        
    return check

def main(VAR, INS, LS, US, varformat, LSSALT, USSALT, LSCOMM, USCOMM, PROVERINPUT):
    assert checkformat(VAR, INS, varformat)
    
    
    mergedScripts = mergeScrpitsFun(LS, US)
    reArranged = reArrangeFun(VAR, INS, varformat)
    
    assert mergedScripts==reArranged ##check Arrange(VAR || INS) == LS||US ##
    
    assert (checkHash(LS, LSCOMM, LSSALT))
    assert (checkHash(US, USCOMM, USSALT))
    
    RESULT, VAR_UPDATED = run(VAR, INS)
    
    assert(PROVERINPUT == RESULT)
    
    assert(True == PROVERINPUT[len(PROVERINPUT)-1])
    
    assert(len(VAR_UPDATED)==0)
    
        
    return 

main([1,2,3], [2,3,1], [1,2], [2,3,3,1], [1,1,0,1,0,0], "0", "22", "120", "233122", [3, 3, True])