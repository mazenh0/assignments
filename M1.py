def main():
    purchase_price = int(input("Enter the purchase price of your item: "))
    items = int(input("Enter the number of items: "))
    discount = int(input("enter your discount amount (0-100): "))
    total_purchase_price = purchase_price * items 
    discount_price = total_purchase_price - discount
    gst = (discount_price * 0.05) 
    final_price = discount_price + gst 
    print(f"with a purachse of {items} @ ${purchase_price} each equals {total_purchase_price}")
    print(f"with a discount of ${discount} the total is ${discount_price} ")
    print(f"The total for the sale is ${discount_price} plus ${gst} GST equals ${final_price}")
main()
