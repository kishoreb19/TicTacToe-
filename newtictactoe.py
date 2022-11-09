print("---------------")
print("| Tic Tac Toe |")
print("---------------")
print()
a = [1,2,3,4,5,6,7,8,9]
c=1
s=0
while(True):
    print(a[0],"|",a[1],"|",a[2])
    print("---------")
    print(a[3],"|",a[4],"|",a[5])
    print("---------")
    print(a[6],"|",a[7],"|",a[8])
    if c%2 != 0:
        x = int(input("X's Move :"))
        if  x<0 or x>10:
            print("Enter a number b/w 1 to 9 !")
        elif x==1:
            if a[0] == "X" or a[0] == "O":
                print("Wrng")
            else:
                a[0] = "X"
            s=s+1
            c=c+1
        elif x==2:
            if a[1] == "X" or a[1] == "O":
                print("Wrng")
            else:
                a[1] = "X"
            s=s+1
            c=c+1
        elif x==3:
            if a[2] == "X" or a[2] == "O":
                print("Wrng")
            else:
                a[2] = "X"
            s=s+1
            c=c+1
        elif x==4:
            if a[3] == "X" or a[3] == "O":
                print("Wrng")
            else:
                a[3] = "X"
            s=s+1
            c=c+1
        elif x==5:
            if a[4] == "X" or a[4] == "O":
                print("Wrng")
            else:
                a[4] = "X"
            s=s+1
            c=c+1
        elif x==6:
            if a[5] == "X" or a[5] == "O":
                print("Wrng")
            else:
                a[5] = "X"
            s=s+1
            c=c+1
        elif x==7:
            if a[6] == "X" or a[6] == "O":
                print("Wrng")
            else:
                a[6] = "X"
            s=s+1
            c=c+1
        elif x==8:
            if a[7] == "X" or a[7] == "O":
                print("Wrng")
            else:
                a[7] = "X"
            s=s+1
            c=c+1
        elif x==9:
            if a[8] == "X" or a[8] == "O":
                print("Wrng")
            else:
                a[8] = "X"
            s=s+1
            c=c+1
        print("\n\n")
    elif (c%2 == 0):
        o = int(input("O's Move :"))
        if  o<0 or o>10:
            print("Enter a number b/w 1 to 9 !")
        elif o==1:
            if a[0] == "X" or a[0] == "O":
                print("Wrng")
            else:
                a[0] = "O"
            s=s+1
            c=c+1
        elif o==2:
            if a[1] == "X" or a[1] == "O":
                print("Wrng")
            else:
                a[1] = "O"
            s=s+1
            c=c+1
        elif o==3:
            if a[2] == "X" or a[2] == "O":
                print("Wrng")
            else:
                a[2] = "O"
            s=s+1
            c=c+1
        elif o==4:
            if a[3] == "X" or a[3] == "O":
                print("Wrng")
            else:
                a[3] = "O"
            s=s+1
            c=c+1
        elif o==5:
            if a[4] == "X" or a[4] == "O":
                print("Wrng")
            else:
                a[4] = "O"
            s=s+1
            c=c+1
        elif o==6:
            if a[5] == "X" or a[5] == "O":
                print("Wrng")
            else:
                a[5] = "O"
            s=s+1
            c=c+1
        elif o==7:
            if a[6] == "X" or a[6] == "O":
                print("Wrng")
            else:
                a[6] = "O"
            s=s+1
            c=c+1
        elif o==8:
            if a[7] == "X" or a[7] == "O":
                print("Wrng")
            else:
                a[7] = "O"
            s=s+1
            c=c+1
        elif o==9:
            if a[8] == "X" or a[8] == "O":
                print("Wrng")
            else:
                a[8] = "O"
            s=s+1
            c=c+1
        print("\n\n")
    if ((a[0] == "X" and a[1] == "X" and a[2] == "X") or #Horizontal_Check
        (a[3] == "X" and a[4] == "X" and a[5] == "X") or
        (a[6] == "X" and a[7] == "X" and a[8] == "X") or #VERTICAL_Check
        (a[0] == "X" and a[3] == "X" and a[6] == "X") or
        (a[1] == "X" and a[4] == "X" and a[7] == "X") or
        (a[2] == "X" and a[5] == "X" and a[8] == "X") or #Diagonal_Check
        (a[0] == "X" and a[4] == "X" and a[8] == "X") or
        (a[2] == "X" and a[4] == "X" and a[6] == "X")):
        print("X Won !")
        break;
    if ((a[0] == "O" and a[1] == "O" and a[2] == "O") or#Horizontal_Check
        (a[3] == "O" and a[4] == "O" and a[5] == "O") or
        (a[6] == "O" and a[7] == "O" and a[8] == "O") or #VERTICAL_Check
        (a[0] == "O" and a[3] == "O" and a[6] == "O") or
        (a[1] == "O" and a[4] == "O" and a[7] == "O") or
        (a[2] == "O" and a[5] == "O" and a[8] == "O") or #Diagonal_Check
        (a[0] == "O" and a[4] == "O" and a[8] == "O") or
        (a[2] == "O" and a[4] == "O" and a[6] == "O")):
        print("O Won !")
        break;
    elif s>=9:
        print("DRAW MATCH !")
        break;
    
        

        
            
    
