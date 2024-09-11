import math
a=int(input("Enter A capacity : "))
b=int(input("Enter B capacity : "))
ai=int(input("Initial state of A : "))
bi=int(input("Initial state of B : "))
af=int(input("Final state of A : "))
bf=int(input("Final state of B : "))
if a<=0 or b<=0:
    print("Jug capacitites cannot be negative.")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("negative values not allowed.")
    exit(1)
def wjug(a,b,ai,bi,af,bf):
    print("List of Operations\n")
    print("1. Fill A completely")
    print("2. Fill B completely")
    print("3. Empty A completely")
    print("4. Empty B completely")
    print("5. Pour from A till B is full or A is empty")
    print("6. Pour from B till A is full or B is empty")
    print("7. Pour all from B to A")
    print("8. Pour all form A to B")
    while ai!=af or bi!=bf:
        op=int(input("Enter Operation (1-8) :"))
        if op==1:
            ai=a
        elif op==2:
            bi=b
        elif op==3:
            ai=0
        elif op==4:
            bi=0
        elif op==5:
            pour_amt=min(ai,b-bi)
            ai-=pour_amt
            bi+=pour_amt
        elif op==6:
            pour_amt=min(bi,a-ai)
            bi-=pour_amt
            ai+=pour_amt
        elif op==7:
            pour_amt=min(bi,a-ai)
            ai+=pour_amt
            bi-=pour_amt
        elif op==8:
            pour_amt=min(ai,b-bi)
            bi+=pour_amt
            ai-=pour_amt
        else:
            print("Invalid Operation")
            continue
        print(f" A: {ai}, B: {bi}")
        if ai==af and bi==bf:
            print("Final State Reached: jug A=", ai,", jug B= ", bi)
            return
gcd=math.gcd(a,b)
if(af<=a and bf<=b) and (af%gcd==bf%gcd==0):
    wjug(a,b,ai,bi,af,bf)
else:
    print("The final state is not achievable with givn capacities.")
    exit(1)
