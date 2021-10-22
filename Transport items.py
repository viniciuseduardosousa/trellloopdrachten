import time
import os
shad = True
while shad == True:
    product = 'car'


    Factory= []
    Factory.append(product)

    print(f"factory:{Factory}")
    print("Distribution:")
    print("Shop:")
    time.sleep(1)
    Factory.clear()
    print(Factory) 
    os.system('clear')


    Distrubution= []
    Distrubution.append(product)

    print(f"factory:")
    print(f"Distribution:{Distrubution}")
    print(f"Shop:")
    time.sleep(1)
    Distrubution.clear()
    print(Distrubution) 
    os.system('clear')



    Shop= []
    Shop.append(product)

    print(f"factory:")
    print(f"Distribution:")
    print(f"Shop: {Shop}")
    time.sleep(1)
    Shop.clear()
    print(Shop) 
    os.system('clear')
    
    x = input("Repeat? y/n \n")
    if x == 'n':
        break





