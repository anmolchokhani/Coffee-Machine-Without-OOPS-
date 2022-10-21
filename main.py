from resources import MENU, resources

all_times = ['espresso','latte','cappuccino','report']
total_profit=0
def prompt_user():
    
    # welcome = "welcome to our coffee shop".title()
    print("\nwelcome to our coffee shop".title(), "\nHERE IS OUR MENU")
    print("************")
    for key in MENU.keys():
        print(f"{key.upper()}: ${MENU[key]['cost']}")
    print("************")
    tryagain = True
    while tryagain:
        user_choice= input('What would you like? (espresso/latte/cappuccino): ').lower()
        if user_choice not in all_times:
            print("Incorrect choice try again")
        else:
            tryagain = False
        if user_choice== 'report':
            report()
            return
    return user_choice


def report():
    for keyy,resource in resources.items():
        keyy = keyy.title()
        if keyy =='Coffee':
            print(f"{keyy}: {resource}g")
        else:   
            print(f"{keyy}: {resource}ml")

def users_drink(user_choice):
    for item in MENU[user_choice]['ingredients'].keys():
        menu_item= MENU[user_choice]['ingredients'][item]
        if menu_item > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return

    for item in MENU[user_choice]['ingredients'].keys():
        resources[item] -= MENU[user_choice]['ingredients'][item]
    return "milgaya"




def insert_coins():
    print("Please insert coins")
    quarters= int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money= quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total_money
    


def main():
    global total_profit
    thing= True
    while thing:
        user_choice = prompt_user()
        if user_choice != None:
            
            total_money = insert_coins()
            cost = MENU[user_choice]['cost']
            if cost> total_money:
                print("Sorry that's not enough money. Money refunded.")
            else:
                drink = users_drink(user_choice)
                if drink == None:
                    print(f"Here is your entire refund ${round(total_money,2)}")
                else:
                    total_profit =  total_profit + cost
                    print(f"Enjoy your {user_choice}☕")
                    print(f"Here is your change ({round(total_money,2)}-{cost}) ${round(total_money-cost,2)}")
            thing = input("For Next Customer Please Press True or false: ".title())
        else:
            main()
        

main()






