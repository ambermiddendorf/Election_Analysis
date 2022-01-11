temperature = int(input("What is the temperature outside?"))
if temperature >80:
    print("Turn on the AC.")
else:
    if temperature <60:
        print("Turn on the furnace.")
    else:    
        print("Open the windows.")