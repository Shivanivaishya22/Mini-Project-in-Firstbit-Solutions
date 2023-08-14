from ckshop import CakeShop , Cakecustomer , Bill
class ShopMgmt:
    def addcakes(self,c1):
        with open("cklist.txt","a" )as fp:
            fp.write(str(c1))
            fp.write("\n")
    
    def showcakes(self):
        try:
            with open("cklist.txt","r") as fp:
                data = fp.read()
                print(data)

        except FileNotFoundError:
            print("file not exist")
              
    def Requiredcake(self):
        try:
            allcakes = []
            found = False
            with open ("cklist.txt","r") as fp:
                for x in fp:
                    x = x.split(",")
                    if(int(x[3]) == 0):
                        print(x[1] , "cakes are out of stock currently.")
                        found = True
                    else:
                        allcakes.append(x)
                    
        except FileNotFoundError:
            print("cake is not available")

        if(found == True):
            with open("cklist.txt","w") as fp:
                for y in allcakes:
                    y = ",".join(y)
                    fp.write(y)
                    # fp.write("\n")
        else:
            msg = "Nothing is out of stock"
            print(msg.center(100,"*"))

    def editPrizeByid(self,id,prize):
        try:
            found = False
            allcakes = [] 
            with open("cklist.txt","r") as fp:
                for j in fp:
                   j = j.split(",")
                   if(id == int(j[0])):
                       j[2] = str(prize)
                       found = True
                   allcakes.append(j)
                   print(allcakes)
            
        except FileNotFoundError:
            print("File not found")

        if(found == True):
            with open("cklist.txt","w") as fp:
                for ck in allcakes:
                    ck = ",".join(ck)
                    fp.write(ck)
                    fp.write("\n")

    def editCakeName(self,nm,new):
        try:
            found = False
            allcakes = [] 
            with open("cklist.txt","r") as fp:
                for j in fp:
                   j = j.split(",")
                   if(j[1] == nm):
                       j[1] = new
                       found = True
                   allcakes.append(j)
                print(allcakes)
            
        except FileNotFoundError:
            print("File not found")

        if(found == True):
            with open("cklist.txt","w") as fp:
                for ck in allcakes:
                    ck = ",".join(ck)
                    fp.write(ck)
                    # fp.write("\n")
                    print(ck)
   
    def editCakeCountbyid(self,id,count):
        try:
            found = False
            allcakes = [] 
            with open("cklist.txt","r") as fp:
                for j in fp:
                   j = j.split(",")
                   if(id == int(j[0])):
                       j[3] = str(count)
                       found = True
                   allcakes.append(j)
            
        except FileNotFoundError:
            print("File not found")

        if(found == True):
            with open("cklist.txt","w") as fp:
                for ck in allcakes:
                    ck = ",".join(ck)
                    fp.write(ck)
                    print(ck)
                    # fp.write("\n")
    
    def viewBillRecord(self):
        with open ("billrecords.txt" , "r") as cp:
            data = cp.read()
            print(data)

    def showAllCakes(self):
        try:
            found = False
            allcks = []
            with open ("cklist.txt" , "r") as fp2:
                for data in fp2:
                    data = data.split(",")
                    if(int(data[3]) == 0):
                        found = True
                    else:
                        allcks.append(data)
                    
            with open ("cklist.txt","w") as fp:
                  for y in allcks:
                    y = ",".join(y)
                    fp.write(y)
        except FileNotFoundError:
            print("Sorry. Try after sometime...")
        
        if (found == False):
            self.showcakes()

    def addToCart(self):        
        a = input("do you want to buy cake?(y/n): ")        
        if(a == "y"): 
            print("Please give your order...")
            orders = int(input("How many type of cakes do you want to buy: "))
            for o in range(1,orders+1):
                cid = int(input("Enter Cake id: "))
                cq = int(input("Enter no. of Cakes you want to buy: "))  
         
                with open("cklist.txt","r") as fp:   
                    for y in fp:
                    
                       y.split(",")
                       if(cid == int(y[0]) and cq <= int(y[3])):                           
                            c2 = Cakecustomer(cid,cq)
                            with open("cart.txt","a") as fp:   #for adding customers order in the cart
                              fp.write(str(c2))
                              fp.write("\n") 
                            print("Order confirmed!")
                            break
                    else:
                        print("Not available.")
        else:
            print("Thank you for visit...")

    def buyNow1(self):
        allCakes = []
        with open("cklist.txt","r") as fp:
            for line in fp:
                line = line.split(",")
                allCakes.append(line)
        
        with open("cart.txt","r") as fp1:
            for c in fp1:
                c=c.split(",")
                for cake in allCakes:
                    if(c[0] == cake[0]):
                        # print("found")
                        cake[3] = str(int(cake[3])-int(c[1]))
                        cake[3]+="\n"
        print(allCakes)
        with open("cklist.txt","w") as fp:
            for cake in allCakes:
                cake = ",".join(cake)
                fp.write(cake)

    def buyNow(self):
        try:
            price = 0
            with open ("cart.txt","r") as fp:
                for i in fp:
                    i = i.split(",")
                    id = int(i[0])       #id ordered by customer
                    count = int(i[1])    #quantity orderd by customer
                    with open("cklist.txt","r") as fp:
                        for y in fp:
                            y = y.split(",")                           
                            if(id == int(y[0])):
                                nm = y[1]             #name of cake
                                total = int(y[2]) * count         #ckpp * count
                                with open("bill.txt","a") as fp:
                                    c3 = Bill(id ,nm, count , total)
                                    fp.write(str(c3))
                                    fp.write("\n")
                     
                with open("bill.txt" , "r") as fp:                                   
                        for c in fp:                                     
                            c = c.split(",")  
                            price  += int(c[3])
                            print("---------------------------------------------------")
                            print("|  Cake Name  |  CakeId | Cakequantity |  Cakeprice |")
                            print("|  ",c[0],"   | ",c[1],"| ", c[2] ,"   |  ",c[3] ," |")
                        else:
                            print("Your final Bill is ", price)
                            print("Thank you for visiting us!!")
            self.buyNow1()                                                                                                    
        except FileNotFoundError:
            print("You can order something else...") 

        else:
           
            with open ("cart.txt","w") as cp:
                 cp.write("")
            with open ("bill.txt","r") as fp:
                data = fp.read()
            with open ("billrecords.txt","a") as fp:
                fp.write(data)
                fp.write("\n")                    
            with open ("bill.txt" , "w") as fp:
                fp.write("")
    