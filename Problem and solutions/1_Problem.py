# flipkart wants to discount at 5000+ = 20% and 3000+ = 10% on purchase Amount
purchase_amount=6500
if (purchase_amount>=5000):
    discount=0.2*purchase_amount
    print(f"get 20% percent discount Rs.{discount}")
elif(purchase_amount>=3000):
     discount=0.1*purchase_amount
     print(f"get 10% percent discount Rs.{discount}")
else:
     print("NO discount")
final_purchase_amount=purchase_amount-discount
print(f"you get this product only : Rs.{final_purchase_amount}")