import sys
fo=0
fx=0
fo=open(sys.argv[1],"r")
fx=open(sys.argv[2],"w")
text=fo.readlines()

#user=input("Enter a letter : ")
List1=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       '1','2','3','4','5','6','7','8','9','0']
List2=['*@',"10","20","30","40","50","60","70","80","90","11","12","13","14","15","52","76","17","18","19","89","21","22","23","24","25","26",
       '@#','$!','%#','^=','8%','EE','-~','/<','>*','!=','$%',')+','#/','>5','%+','1@','*%','^@','98','00','*A','44','99','45','51','#7',
       '!!','##','$$','%%','^^','&&','^&','!F','*G','%/']

#print(text)
#text1=text.pop(0)

while len(text)!=0:
    text1=text.pop(0)
    for x in text1:
        if x=="\n":
            fx.writelines("\n")
            break
        
        
        y=List1.index(x)
        z=List2[y]
        #print(z,end="")
        fx.writelines(z)
        #List3.append(z)
    
#print()
fo.close()
fx.close()
