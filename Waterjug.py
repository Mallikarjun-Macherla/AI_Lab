import math
a=int(input("Enter jug A capacity:"))
b=int(input("Enter jug B capacity:"))
ai=int(input("Initially water in jug A:"))
bi=int(input("Initially water in jug B:"))
af=int(input("Final state of jug A:"))
bf=int(input("Final state of jug B:"))

if a<=0 or b<=0:
    print("Jug capacities must be positive:")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("Negative values are not allowed:")
    exit(1)

def wjug(a,b,ai,bi,af,bf):
    print("List of Operations you can do:\n")
    print("1.fill jug A completely")
    print("2.fill jug B completely")
    print("3.Empty jug A completely")
    print("4.Empty jug B completely")
    print("5.pour from jug A till jug B is full or A becomes empty")
    print("6.pour from jug b till jug A is full or B becomes empty")
    print("7.pour all from jug B to jug A")
    print("8.pour all from jug B to jug A")
    while(ai!=af or bi!=bf):
        op=int(input("Enter the operation:\n"))
        if op==1:
            ai=a
        elif op==2 :
            bi=b
        elif op==3:
            ai=0
        elif op==4:
            bi=0
        elif op==5:
            pamn = min(ai,b-bi)
            ai-=pamn
            bi +=pamn
        elif op==6:
            pamn=min(bi,a-ai)
            bi -=pamn
            ai +=pamn
        elif op==7:
            pamn = min(ai,b-bi)
            ai+=pamn
            bi -=pamn
        elif op==8:
            pamn = min(ai,b-bi)
            bi+=pamn
            ai-=pamn
        else:
            print("Invalid operation please choose a number between 1-8")
            continue
        print(f"Jug A: {ai},jug B:{bi}")
        if ai == af and bi ==bf:
            print("final state reached: Jug A=",ai,",Jug B=",bi)
            return
        print("Final state Reached: Jug A=",ai,",Jug B=",bi)
gcd = math.gcd(a,b)
if(af<=a and bf<=b) and (af% gcd ==bf % gcd ==0):
    wjug(a,b,ai,bi,af,bf)
else:
    print("The final state is not achievable with given capacities.")
    exit(1)
            
            
