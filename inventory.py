# Initialize Shoe class with parameters country, code, product, cost, quantity
class Shoe:

    # Constructor with attributes 'country', 'code', 'product', 'cost' and 'quantity'
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define get_cost() method, wich return the cost of the shoes
    def get_cost(self):
        return self.cost

    # Define get_quantity() method, wich return the quantity of the choes
    def get_quantity(self):
        return self.quantity
    
    # This method returns a string representation of a class.
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# The list 'shoe_list' will store a list of objects of shoes.
# The list 'top_list' will store a list of the top of the table
shoe_list = []
top_list = []

# Function open the file 'inventory.txt' with 'try-except' method and read the data from this file,
# then create a shoes object with this data and append this object into the shoe_list. 
# One line in this file represents data to create one object of shoes.
# Skip first line
def read_shoes_data():
    file = None
    try:
        file = open('inventory.txt', 'r', encoding='utf-8')
        
    except FileNotFoundError as ex:
            print("\nThe file that you are trying to open does not exist!")
            print(ex,'\n')
   
    finally:
        if file is not None:
            file_read = file.readlines() 
            for number, line in enumerate(file_read):
                if number == 0:
                    top_list.extend(line.strip().split(','))
                elif number > 0:
                    shoe_list.append(Shoe(line.split(",")[0],line.split(",")[1],line.split(",")[2],float(line.split(",")[3]),int(line.strip('\n').split(",")[4])))
                
            return file.close()

# This function allow a user to capture data about a shoe and use this data to create 
# a shoe object and append this object inside the shoe list.
# Check each variables inputed data for errors of value (with 'try-except' method), 
# length and not empty (with 'if-else' method) in loop
def capture_shoes():
    while True:
        country = input("\nEnter country of product: ")
        print()
        if len(country) > 23 or country == '':
            print("Too long country name it's empty! Try again.")
        else:
            break
    
    while True:
        code = input("Enter the code of product: ")
        print()
        if len(code) > 15 or code == '':
            print("Too long code or it's empty! Try again.")
        else:
            break
    
    while True:
        product = input("Enter product name: ")
        print()
        if len(product) > 31 or product == '':
            print("Too long product name or it's empty! Try again.")
        else:
            break  
    
    while True:
        try:
            cost = round(float(input("Enter price of your product: ")),2)
            if len(str(cost)) > 15:
                print("It's too much!! Try again.")
            else:  
                print()
                break
        except ValueError:
            print("\nYou entered wrong value of cost!Try again!\n")
       
    while True:
        try:         
            quantity = int(input("Enter number of quantity: "))
            if len(str(quantity)) > 15:
                print("It's too much!! Try again.")
            else:
                print()
                break  
        except ValueError:
            print("\nYou entered wrong value of quantity!Try again!\n")            

    shoe_list.append(Shoe(country,code,product,cost,quantity))
    print("\nNew item was add to stock!\n")
    return shoe_list

# This function iterate over the shoes list and print the details of the shoes returned from the __str__ function
def view_all():
    # Temp list to operate with shoe objects 
    temp_shoe_list = []
    
    # Buildin table
    print()
    print("╔" + "═"*31 + "╦" + "═"*15 + "╦" + "═"*31 + "╦" + "═"*15 + "╦" + "═"*15 + "╗")
    print(f"║\t      {top_list[0]}\t\t║     {top_list[1]}\t║\t     {top_list[2]}\t\t║     {top_list[3]}\t║    {top_list[4]}\t║")
    print("╠" + "═"*7 + "╦" + "═"*23 + "╬" + "═"*15 + "╬" + "═"*31 + "╬" + "═"*15 + "╬" + "═"*15 + "╣")
    
    # check the length of each item in shoe object, and add the required number of spaces using '\t'
    temp_shoe_list = shoe_list
    for num, line in enumerate(temp_shoe_list, start=1):
        str(line).strip()
        
        line_country = line.country
        if len(line.country) < 23:
            line_country = line.country + '\t'
        if len(line.country) < 15:
            line_country = line.country + '\t\t'
        if len(line.country) < 7:
            line_country = line.country + '\t\t\t'
        
        line_product = line.product
        if len(line.product) < 31:
            line_product = line.product + '\t'
        if len(line.product) < 23:
            line_product = line.product + '\t\t'
        if len(line.product) < 15:
            line_product = line.product + '\t\t\t'
        if len(line.product) < 7:
            line_product = line.product + '\t\t\t\t'
        
        line_code = line.code
        if len(line.code) < 15:
            line_code =line.code + '\t'
        if len(line.code) < 7:
            line_code =line.code + '\t\t'
            
        line_cost = line.cost
        if len(str(line.cost)) < 15:
            line_cost = str(line.cost) + '\t'
        if len(str(line.cost)) < 7:
            line_cost = str(line.cost) + '\t\t'
            
        line_qty = line.quantity
        if len(str(line.quantity)) < 15:
            line_qty = str(line.quantity) + '\t'
        if len(str(line.quantity)) < 7:
            line_qty = str(line.quantity) + '\t\t'  
            
        print(f"║{num}\t║{line_country}║{line_code}║{line_product}║{line_cost}║{line_qty}║")
        print("╠" + "═"*7 + "╬" + "═"*23 + "╬" + "═"*15 + "╬" + "═"*31 + "╬" + "═"*15 + "╬" + "═"*15 + "╣")
    print("╚" + "═"*7 + "╩" + "═"*23 + "╩" + "═"*15 + "╩" + "═"*31 + "╩" + "═"*15 + "╩" + "═"*15 + "╝")
   
# This function find the shoe object with the lowest quantity, which is the shoes that need to be
# re-stocked. Ask the user if they want to add to this quantity of shoes and then update it. This quantity also updated
# on the file for this shoe. Check inputed data
def re_stock(): 
    shoe_list.sort(key=lambda x:int(x.get_quantity()))
    print(f"\nThe product with lowest quantity of stock:\n\n{shoe_list[0]}\n")
    
    while True:
        choice_restock = input("1 - restock it\n2 - keep it without changing\n:")
        if choice_restock =='1':
            
            qty_restock = input("\nEnter the quantity you want to add: ")
            if not qty_restock.isdigit():
                print("\nYou entered wrong value of qquantity!\n")
            
            if qty_restock.isdigit():
                print()
                shoe_list[0].quantity = int(qty_restock) + int(shoe_list[0].quantity)
                print("Success!!")
                break
        
        elif choice_restock == '2':
            print("\nStock keeps without changing")
            break
       
        else:
            print("\nYou entered something wrong!\n")
        
    file = open('inventory.txt', 'w', encoding='utf-8')
    shoe_list.sort(key=lambda x:int(x.get_quantity()))
    file.write(f"{top_list[0]},{top_list[1]},{top_list[2]},{top_list[3]},{top_list[4]}\n")
    
    for line in shoe_list:
        file.write(f"{line.country},{line.code},{line.product},{line.cost},{line.quantity}\n")    
    return file.close()

# This function search for a shoe from the list using the shoe code and return this object so that it will be printed.
# chec inputed data
def search_shoe():
    shoe_code = input("\nEnter the code of shoe you need: ")
    print()
    
    line = ''
    for i in shoe_list:
        if i.code == shoe_code:
            print(i)
            line = i
            
    if line == '':
        print(f"\nThere is no item with code -= {shoe_code} =- in stock")

# This function calculate the total value for each item and print it in table.
# check the length of each shoe object, and add the required number of spaces using '\t'
def value_per_item():
    # build table
    print()
    print("╔" + "═"*31 + "╦" + "═"*15 + "╦" + "═"*31 + "╦" + "═"*15 + "╦" + "═"*15 + "╦" + "═"*15 + "╗")
    print(f"║\t      {top_list[0]}\t\t║     {top_list[1]}\t║\t    {top_list[2]}\t\t║     {top_list[3]}\t║   {top_list[4]}\t║     Value     ║")
    print("╠" + "═"*7 + "╦" + "═"*23 + "╬" + "═"*15 + "╬" + "═"*31 + "╬" + "═"*15 + "╬" + "═"*15 + "╬" + "═"*15 + "╣")
   
    temp_shoe_list = shoe_list
    for num, line in enumerate(temp_shoe_list, start=1):
        
        str(line).strip()
        
        line_country = line.country
        if len(line.country) < 23:
            line_country = line.country + '\t'
        if len(line.country) < 15:
            line_country = line.country + '\t\t'
        if len(line.country) < 7:
            line_country = line.country + '\t\t\t'
        
        line_product = line.product
        if len(line.product) < 31:
            line_product = line.product + '\t'
        if len(line.product) < 23:
            line_product = line.product + '\t\t'
        if len(line.product) < 15:
            line_product = line.product + '\t\t\t'
        if len(line.product) < 7:
            line_product = line.product + '\t\t\t\t'
        
        line_code = line.code
        if len(line.code) < 15:
            line_code =line.code + '\t'
        if len(line.code) < 7:
            line_code =line.code + '\t\t'
            
        line_cost = line.cost
        if len(str(line.cost)) < 15:
            line_cost = str(line.cost) + '\t'
        if len(str(line.cost)) < 7:
            line_cost = str(line.cost) + '\t\t'
            
        line_qty = line.quantity
        if len(str(line.quantity)) < 15:
            line_qty = str(line.quantity) + '\t'
        if len(str(line.quantity)) < 7:
            line_qty = str(line.quantity) + '\t\t'
           
        line_value = line.get_cost() * line.get_quantity()
        if len(str(line_value)) < 15:
            line_value = str(line_value) + '\t'
        if len(str(line_value)) <= 7:
            line_value = str(line_value) + '\t'  
        
        print(f"║{num}\t║{line_country}║{line_code}║{line_product}║{line_cost}║{line_qty}║{line_value}║")
        print("╠" + "═"*7 + "╬" + "═"*23 + "╬" + "═"*15 + "╬" + "═"*31 + "╬" + "═"*15 + "╬" + "═"*15 + "╬" + "═"*15 + "╣")
    print("╚" + "═"*7 + "╩" + "═"*23 + "╩" + "═"*15 + "╩" + "═"*31 + "╩" + "═"*15 + "╩" + "═"*15 + "╩" + "═"*15 + "╝")

# This function determine the product with the highest quantity and print this shoe as being for sale
def highest_qty():
    shoe_list.sort(key=lambda x:int(x.get_quantity()), reverse=True)
    print(f"\nThis shoe needs to be for sale:\n\n{shoe_list[0]}\n")
 
# Function of menu 
def menu():
    print()
    print('1. View all stock')
    print('2. Capture shoes')
    print('3. Lowest quantity')
    print('4. Search shoe')
    print('5. View values')
    print('6. Highest quantity')
    print('0. Quit')
    print()

# Create variablle for user choice from menu
# Before start call function to read data from file
# Then, if shoe_list not empty,  the program will call the appropriate function 
# depending on the user's choice,depending on the user's choice.
# If shoes_list empty - print error message and quit
menu_choice = ''
read_shoes_data()
while True:
    
    if shoe_list != []:
        menu()
        menu_choice = input("Enter number (1- 6), or 0 - to quit: ")
        
        if menu_choice == '1':
            view_all()
            
        elif menu_choice == '2':
            capture_shoes()
            
        elif menu_choice == '3':
            re_stock()
        
        elif menu_choice == '4':
            search_shoe()
            
        elif menu_choice == '5':
            value_per_item()
            
        elif menu_choice == '6':
            highest_qty()  
            
        elif menu_choice == '0':
            print("\nGoodbye!\n")
            break
 
    elif shoe_list == []:
        print("There are no items in stock!\n")
        break
        


