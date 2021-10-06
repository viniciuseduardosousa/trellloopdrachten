print("YO wat wil je laten stotteren? \n")

running = True
while running == True:
    antwoord = input("typ hier: ")
    userlist = antwoord.split()
    for x in userlist:
        if len(x) > 2:
            print(x[0:2]+"..", x[0:2]+".." ,x)
        else:
            print(x)
    break
