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