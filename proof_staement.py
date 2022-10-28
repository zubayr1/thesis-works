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

def main(VAR, INS, LS, US, varformat, LSSALT, USSALT, LSCOMM, USCOMM):
    assert checkformat(VAR, INS, varformat)
    
    
    mergedScripts = mergeScrpitsFun(LS, US)
    reArranged = reArrangeFun(VAR, INS, varformat)
    
    assert mergedScripts==reArranged ##check Arrange(VAR || INS) == LS||US ##
    
    assert (checkHash(LS, LSCOMM, LSSALT))
    assert (checkHash(US, USCOMM, USSALT))
    
    return 

main( [1,2,4],  [3,5], [1,2],  [3,4,5], [1,1,0,1,0], "0", "22", "120", "34522")