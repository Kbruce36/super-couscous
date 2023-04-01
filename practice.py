def get_customer_info():
    #here we ensure that the customer ID is 7 characters long.
    while True:
        customer_ID = input("enter customer ID: ")
        if len(customer_ID) ==7:
            break
        else:
            print("Customer ID must be 7 characters.")
    #we convert the name to upper case.
    name = input("enter customer name: ").upper()

    #her we have a list of valid town codes
    a = ["EBB", "MBRA", "KLA", ]
    print(a)
    #here we want the user to strictly input a town code from the above list.
    while True:
        #the input from the customer should be in capital letters hence we use the upper()function.
        town_code = input("enter town code from above list: ").upper()
        if town_code in a:
            break
        else:
            print("Invalid town code. Please enter a valid town code.")
#here we get the customer type, either retail or wholesale.
    X = ['WHOLESALE', 'RETAIL']
    print(X)
    while True:
        customer_type = input("Enter customer type either\nretail or wholesale: ").upper()
        if customer_type in X:
            break
        else:
            print('please choose a type in the above list.')
    return{
        'customer ID: ': customer_ID,
        'Name: ': name,
        'Town Code: ': town_code,
        'Customer Type: ': customer_type
        }

#we define a function to get the part order information
def part_order_info(customer_type, town_code):

    part_number = input('enter part number: ')
    description = input('enter part description: ')
    price_per_part = float(input('enter part price: '))
    quantity = int(input('enter quantity: '))
    oversize_status = input("Is this an oversize order \n (yes or no): ")
    b = ['UPS', 'US.postalair', 'fedex ground', 'fedex overnight']
    print(b)
    #we now ensure that the user inputs a valid shipping method
    while True:
        shipping_method = input('Please choose a shipping method \n from the list above as it is: ').upper()
        if shipping_method in b:
            break
        else:
            print("invalid shipping method.\n Please choose one from the above list.")
    
    #calculate the shipping cost basing on the shipping method and quantity.
    if shipping_method == 'UPS':
        shipping_cost = 7.00
    elif shipping_cost == 'US.postalair':
        shipping_cost = 8.5
    elif shipping_method == 'fedex ground':
        shipping_cost = 9.25
    else:
        shipping_cost = 12.00



    # we now calculate the sales tax basing on town code and customer type
    if customer_type.lower() == 'retail':
        if town_code =='KLA':
            sales_tax = 0.1
    
        elif town_code in ['EBB', 'MBRA']:
            sales_tax =0.05
        else:
            sales_tax = 0
    else:
        sales_tax = 0


    total_parts_cost = round(price_per_part*quantity)
    total_sales_tax = round(total_parts_cost*sales_tax)
    total_shipping_cost = round(shipping_cost*quantity)
    overall_total_cost = round(total_parts_cost+total_sales_tax+total_shipping_cost)
    
    return{
        'Part number: ': part_number,
        'Description: ': description,
        'Price per part: ': price_per_part,
        'Quantity: ': quantity,
        'Oversize status: ': oversize_status,
        'Shipping method: ': shipping_method,
        'Cost: ':total_parts_cost,
        'Total sales tax: ': total_sales_tax,
        'Total shipping cost: ': total_shipping_cost,
        'Overall cost: ': overall_total_cost
    }
# we now define a function to enable us write all this information to a text file.
# this gave me alot of problems so do more practice on this
def save_customer_details(details):
    with open("Shipment_file.txt", "a") as a:
        a.write("\n\n")
        a.write("CUSTOMER INFORMATION. \n")
        a.write(f"Customer ID: {details['customer ID: ']}\n")
        a.write(f"Name: {details['Name: ']}\n")
        a.write(f"Town Code: {details['Town Code: ']}\n")
        a.write(f"Customer Type: {details['Customer Type: ']}\n")
        a.write(f"\n\n")
        a.write(f"PART ORDER INFORMATION. \n")
        a.write(f"Part number: {details['Part number: ']}\n")
        a.write(f"Descrition: {details['Description: ']}\n")
        a.write(f"Price per part: {details['Price per part: ']}\n")
        a.write(f"Quantity: {details['Quantity: ']}\n")
        a.write(f"Oversize status: {details['Oversize status: ']}\n")
        a.write(f"Shipping method: {details['Shipping method: ']}\n\n")
        a.write(f"OVERALL COSTS.\n")
        a.write(f"Cost: {details['Cost: ']}\n")
        a.write(f"Sales tax: {details['Total sales tax: ']}\n")
        a.write(f"Shipping and Handling: {details['Shipping method: ']}\n")
        a.write(f"Shipping Cost: {details['Total shipping cost: ']}\n")
        a.write(f"Overall cost: {details['Overall cost: ']}")
#commented out coz i am still looking for a way to input the loop.

    
number_of_parts = input(("enter number of parts: "))
for i in str(range(int(number_of_parts))):
    #how do i insert the arguments without getting an error
    rep = part_order_info(customer_type, town_code)
    print(rep)

# here we call the functions to enable our program to function properly.
customer_info = get_customer_info() 
part_details = part_order_info(customer_info['Customer Type: '], customer_info['Town Code: ']) #had alot of issues here. in-terms of passing the required arguments.       
details = {}
details.update(customer_info)
details.update(part_details)
save_customer_details(details)