import sys

fo=0
fm=0
a=0
fo=open(sys.argv[1],"r")
fm=open(sys.argv[2],"w")
text3=fo.readlines()
#user=input("Enter a letter : ")

#inputfile=sys.argv[1]
#ouputfile=sys.argv[2]
#f="Enter the encoded file : "
#print(f,sys.argv)

#g="Enter the file need to be decode : "
#print(g,sys.argv)


List1=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       '1','2','3','4','5','6','7','8','9','0']
List2=['*@',"10","20","30","40","50","60","70","80","90","11","12","13","14","15","52","76","17","18","19","89","21","22","23","24","25","26",
       '@#','$!','%#','^=','8%','EE','-~','/<','>*','!=','$%',')+','#/','>5','%+','1@','*%','^@','98','00','*A','44','99','45','51','#7',
       '!!','##','$$','%%','^^','&&','^&','!F','*G','%/']
#print(len(List1))
#print(len(List2))
List3=[]

#print(text3)
#text4=text3.pop(0)
#print(text4)

while len(text3)!=0:
    text4=text3.pop(0)
    a=0
    List4=[]

    #print(text4[0:0+2])
    for i in range(0, len(text4), 2):
        x = text4[a:a+2]
        List4.append(x)
        a += 2
        
        #for x in text4:
            
        
        
    print(List4)

    #decrypt
    for x in List4:
        if x=="\n":
            fm.writelines("\n")
            continue
        
        y = List2.index(x)
        w = List1[y]
        
        #print(w,end="")
        fm.writelines(w)


fo.close()
fm.close()

