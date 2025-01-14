#dictionary of Menu with categories of Drinks, Snacks, and Sandwiches
Menu = {
    "Drinks":{
    "D1": ("Water", 1.0, 2),
    "D2": ("Coca Cola", 2.50, 5),
    "D3": ("Pepsi", 2.50, 5),
    "D4": ("Strawberry Fanta", 2.50, 3),
    "D5": ("Orange Juice", 3.50, 8),
    "D6": ("Mango Juice", 3.50, 6),
    "D7": ("Chocolate milk", 3.50, 1),
    "D8": ("Strawberry milk", 3.50, 7)
    },
    "Snacks": {
    "S1": ("Sour Cream pringles", 5.00, 5),
    "S2": ("Spicy Oman Chips", 0.50, 8),
    "S3": ("KitKat", 3.00, 7),
    "S4": ("Black Kinder Bueno", 3.65, 2),
    "S5": ("White Kinder Bueno", 3.65, 4),
    "S6": ("Lays Salt & Vinegar", 0.75, 1),
    "S7": ("Doritos Nacho Cheese", 6.99, 2)
    },
    "Sandwiches": {
    "SW1":("Ham and Cheese", 9.00, 1),
    "SW2":("Avocado Toast", 5.00, 7) ,
    "SW3":("Grilled Veggies", 7.00, 4),
    "SW4":("Buffalo chicken wrap", 13.00, 2),
    "SW5":("BBQ chicken wrap", 15.00, 7),
    "SW6":("Bacon, egg, and cheese", 8.99, 3)
    }
}

#item suggestions based on item ordered
suggestions = {
"D2": ["S1", "S7", "SW5"],
"SW1": ["D3", "D6", ],
"D3": ["SW3", "SW6", "S1"],
"D5": ["SW6", ],
"D8": ["S3", "S4"],
"S1": ["D2", "sw1"],
"S3": ["D7", "D2"],
"S4": ["D8", "D7"],
"S6": ["D1", "D3", "SW1"],
"SW1": ["S1", "S6", "D1", "D3"],
"SW2": ["D1", "S1"],
"SW3": ["D3" ],
"SW4": ["D4", "S2", "D1"],
"SW5": ["D3", "D4", "S4"],
"SW6": ["D2", "D1", "D5"]


}

#Displays the custom text
print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░███░██░▄▄▄██░█████░▄▄▀██░▄▄▄░██░▄▀▄░██░▄▄▄███▄▄░▄▄██░▄▄▄░███▄▄░▄▄██░██░██░▄▄▄████░███░██░▄▄▄██░▀██░██░▄▄▀█▄░▄██░▀██░██░▄▄░████░▄▀▄░█░▄▄▀██░▄▄▀██░██░█▄░▄██░▀██░██░▄▄▄██████
██░█░█░██░▄▄▄██░█████░█████░███░██░█░█░██░▄▄▄█████░████░███░█████░████░▄▄░██░▄▄▄█████░█░███░▄▄▄██░█░█░██░██░██░███░█░█░██░█▀▀████░█░█░█░▀▀░██░█████░▄▄░██░███░█░█░██░▄▄▄██████
██▄▀▄▀▄██░▀▀▀██░▀▀░██░▀▀▄██░▀▀▀░██░███░██░▀▀▀█████░████░▀▀▀░█████░████░██░██░▀▀▀█████▄▀▄███░▀▀▀██░██▄░██░▀▀░█▀░▀██░██▄░██░▀▀▄████░███░█░██░██░▀▀▄██░██░█▀░▀██░██▄░██░▀▀▀██████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

print("""
╔═══╗╔╗          ╔╗               ╔╗      ╔╗ ╔╗                          
║╔═╗║║║          ║║              ╔╝╚╗    ╔╝╚╗║║                          
║║ ╚╝║╚═╗╔══╗╔══╗║║╔╗    ╔══╗╔╗╔╗╚╗╔╝    ╚╗╔╝║╚═╗╔══╗    ╔╗╔╗╔══╗╔═╗ ╔╗╔╗
║║ ╔╗║╔╗║║╔╗║║╔═╝║╚╝╝    ║╔╗║║║║║ ║║      ║║ ║╔╗║║╔╗║    ║╚╝║║╔╗║║╔╗╗║║║║
║╚═╝║║║║║║║═╣║╚═╗║╔╗╗    ║╚╝║║╚╝║ ║╚╗     ║╚╗║║║║║║═╣    ║║║║║║═╣║║║║║╚╝║
╚═══╝╚╝╚╝╚══╝╚══╝╚╝╚╝    ╚══╝╚══╝ ╚═╝     ╚═╝╚╝╚╝╚══╝    ╚╩╩╝╚══╝╚╝╚╝╚══╝
""")


from prettytable import PrettyTable

#function is used to displau the menu in a table format for each category
def disp_menu():
    for category, items in Menu.items():
    
        table = PrettyTable()
        table.field_names = ["Code", "Item", "Price (AED)", "Quantity"]
    
    
        table.align["Code"] = "l"
        table.align["Item"] = "l"
        table.align["Price ($)"] = "l"
        table.align["Quantity"] = "l"

        #adds the items and their descriptions to the table
        for code, (item_name, price, quantity) in items.items():
            table.add_row([code, item_name, price, quantity])
    
    
        print(f"\nCategory: {category}")
        print(table)

#calling the function to display the menu
disp_menu()

#stores selected items here
cart = {}

while True:
    #asks user for item code 
    user_input = input("\n Enter the item code for the item you want or type 'done' to finish your order:").strip().upper()
    if user_input.upper() == "DONE":
        break
    found = False
    for category, items in Menu.items():
        if user_input.upper() in items:
            found = True
            description, price, stock = items[user_input.upper()]
            #updates stock and adds item to the cart
            if stock > 0:
                found = True
                if user_input.upper() in cart:
                    cart[user_input.upper()]["quantity"] += 1
                else:
                    cart[user_input.upper()] = {"description": description, "price": price, "quantity": 1}
                Menu[category][user_input] = (description, price, stock - 1)
                print(f"\n Added {description.strip()} to your order!")
                #recommends items based on order
                if user_input in suggestions:
                    recommended = suggestions[user_input]
                    print("\nYou might also like: ")
                    for rec in recommended:
                        for cat, items, in Menu.items():
                            if rec in items:
                                rec_desc, rec_price, rec_stock = items[rec]
                                if rec_stock > 0:
                                    print(f" - {rec_desc} (Code: {rec}, price: {rec_price} AED)")
            #Tells user that the item is out of stock
            else:
                print(f"\n Sorry, {description.strip()} is out of stock")
                
                break
    #prints error message if item code is not found in the menu
    if not found:  
        print(" INVALID ITEM CODE, PLEASE TRY AGAIN")
        
        
#shows all the items in the cart and calculates the total price
print("\nYour final order:")
total_price = 0
for code, details in cart.items():
    print(f"{details['description']} x {details['quantity']} - {details['price'] * details['quantity']} AED")
    total_price += details['price'] * details['quantity']
    
#Prints total price
print(f"Total price: {total_price:.2f} AED")


while True:
    #Asks money for payment
    try:
        money_given = float(input("\n please enter your amount of money here: "))
        if money_given < total_price:
        #prints error message if money isn't enough
            print(f"This amount of money is not enough, please try again")
        else:
            #Calculates change and gives it to user
            change = money_given - total_price
            print(f"Payment is successful!, your change is {change} AED")
            break
    #if anything other than a number is added, a error message appears
    except ValueError:
        print("Please enter a valid amount")        
    


