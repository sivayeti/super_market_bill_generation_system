from datetime import datetime

name=input("Enter your name:")

#LIST OF ITEMS
lists= '''
     Rice    Rs 20/kg
     Sugar   Rs 30/kg
     Salt    Rs 20/kg
     Oil     Rs 80/litre
     Paneer  Rs 110/kg
     Maggi   Rs 50/kg
     Boost   Rs 90/each
     Colgate Rs 85/each
'''

#print(lists)

##declaration 
price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]

#rates for items
items={
    'rice'   : 20,
    'sugar'  : 30,
    'salt'   : 20,
    'oil'    : 80,
    'panner' : 110,
    'maggi'  : 50,
    'boost'  : 90,
    'colgate': 85
}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)

for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or to exit press 2:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the item you want to buy:")
        quantity=int(input("Enter the quantity :"))
        if item in items.keys():
            price=quantity*(items[item])
            totalprice+=price
            #pricelist.append(item)
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice+= (gst+totalprice)

        else:
            print("sorry you entered item is not in items list")
    else:
        print("you entered wrong number")
    
    inp=input("Can i bill the items yes or no:")
    if inp=='yes':
        #pass
        if finalprice!=0:
            print(25*"=","Siva Super Market",29*"=")
            print(28*" ","Bangalore")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","Quantity",8*" ","Price")
            #for i in range(len(pricelist)):
            for i in range(len(ilist)):
                print(i,10*" ",ilist[i],11*" ",qlist[i],14*" ",plist[i])
                print(75*"-")
            print("Total Amount:",38*" ","Rs",totalprice)
            print("gst amount:",40*" ","Rs ",gst)
            print(75*"-")
            print(50*" ","final Amount:","Rs ",finalprice)
            print(75*"-")
            print(20*" ","Thanks for Visiting")
            print(75*"-")

