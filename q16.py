''''
16  Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) 
to pay according to following criteria:
    Marked Price	Discount
              >10000	20%
   >7000 and <=10000	15%
              <=7000	10%

'''

price=int(input("Enter a actual price:"))
if price>10000:
    discount=price*(20/100)
    print("Net amount:"+str(price-discount))
elif price <=10000 and price>7000:
    discount=price*(15/100)
    print("Net amount:"+str(price-discount))
else:
    discount=price*(10/100)
    print("Net amount:"+str(price-discount))


