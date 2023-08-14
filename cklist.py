from ckshop import CakeShop 
from shopmgmt import ShopMgmt

if(__name__ == "__main__"):
    cakes = ShopMgmt()
    choice = 0
    username = "Owner"
    password = "1234"
    s = "Welcome to Shivani's Sweet Treat"
    print(s.center(120,"~"))
    ans = input("Are you a owner or customer?(o/c) : ")
    if(ans == "o"):
        uname = input("Enter username: ")
        pas = input("Enter password: ")
        if(uname == username and pas == password):
            while (choice != 9):
                print(''' 
                  1. Add Cakes
                  2. View Cakes
                  3. Required Cakes
                  4. Edit Cakecount by Id
                  5. Edit Prize by Id
                  6. Edit CakeName
                  7. View Bill Records
                  8. Exit
                       ''')
                choice = int(input("Please Enter your choice: "))
                if(choice == 1):
                    c = "*_*Add some Cakes in your shop*_*"
                    print(c.center(125,"-"))
                    cid = int(input("Enter Cake id: "))
                    cname = input("Enter Cakename: ")
                    cpkg = int(input("Enter Cost per kg: "))
                    cc = int(input("Enter no. of Cakes available: "))
                    c1 = CakeShop(cid,cname,cpkg,cc)
                    cakes.addcakes(c1)
     
                elif(choice == 2):
                   d = "*_*_Cakes in our shop_*_*"
                   print(d.center(100,"~"))
                   cakes.showcakes()

                elif(choice == 3):
                   b =" Lets Check stock of our shop..."
                   print(b.center(130,"-"))
                   cakes.Requiredcake()
                
                elif(choice == 4):
                    p = "Lets Add some more cakes in our Shop..."
                    print(p.center(100,"~"))
                    ans = input("Dou you want to update your cake stock?(y/n): ")
                    if(ans == "y"):
                        id = int(input("Enter cake id whose cakecount you want to get updated?: "))
                        count = int(input("Enter new count of cake: "))
                        cakes.editCakeCountbyid(id,count)
                    else:
                        g = "Thank you..!!"
                        print(g.rjust(240,"~"))
                
                elif(choice == 5):
                    id = int(input("Enter cake id whose prize to change? "))
                    prize = int(input("Enter new prize of cake? "))
                    cakes.editPrizeByid(id,prize)

                elif(choice == 6):
                    nm = input("Enter old cake name: ")
                    new = input("Enter new cake name: ")
                    cakes.editCakeName(nm,new)
                
                elif(choice == 7):
                    b = "*__Bill Records__*"
                    print(b.center(230,"-"))
                    cakes.viewBillRecord()
                else:
                     g = "Thank you"
                     print(g.rjust(130,"~"))

        else:
            print("Oops!! Seems you did not entered correct id or password.")        
            
    elif(ans == "c"):
        uchoice = 0
        while(uchoice != 4):
            print('''
                     1. Show All Cakes
                     2. Add To Cart
                     3. Buy Now                     
                     4. Exit
                     ''')
            t = "**--Dear Customer , Welcome to Our shop--**"
            print(t.center(140,"-"))
            uchoice = int(input("Enter Customers choice: "))
            if(uchoice == 1): 
                c = "--*--Menu--*"
                print(c.center(200,"~"))
                print("| id | Name | Rs | Quantity |")
                cakes.showAllCakes()

            elif(uchoice == 2):
                cakes.addToCart()

            elif(uchoice == 3):
                d = "--*--Bill--*--"
                print(d.center(150,"-"))
                cakes.buyNow()
            
            elif(uchoice == 4):
                print("Thank you for your visit!!")
    else:
        print("--------------------------Please make sure your identity to us--------------------------------")