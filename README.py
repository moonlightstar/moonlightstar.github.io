# moonlightstar.github.ioN=input("enter a number:")
3.75
-3.75

#S
S=0
if N[0]=="-":
    S=1
    N=N[1:]
#ToBinary

IntB=""
FloatB=""

N=float(N)
IntN=int(N)
FloatN=N%1

while IntN!=0:
    IntB=str(IntN%2)+IntB
    IntN=IntN//2

while FloatN!=0:
    FloatN*=2
    FloatB+=str(int(FloatN))
    FloatN=FloatN%1

#正規化
Bin=IntB+"."+FloatB
正規化=""
次方=0

if IntB!="":
    正規化=IntB[1:]+FloatB
    次方=len(IntB)-1
else:
    FirstOne=True
    for i in range (len(FloatB)):
        if FirstOne==True:
            if FloatB[i]=="1":
                FirstOne=False
                正規化+="1."
                次方-=1
            else:
                     次方-=1
        else:
                正規化+=FloatB[i]
#E
E=""
次方+=127
while 次方!=0:
    E=str(次方%2)+E
    次方=次方//2
if len(E)<8:
    for i in range(8-len(E)):
        E="0"+E

#M
M=正規化
if len(M)<23:
    for i in range(23-len(M)):
        M=M+"0"


print(S,E,M)
