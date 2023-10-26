def hannuota(n,A,B,C):
    if n==1:
        print(A,'移到',C)
    else:
        hannuota(n-1,A,C,B)
        print(A,'移到',C)
        hannuota(n-1,B,A,C)
hannuota(3,'塔1','塔2','塔3')        
