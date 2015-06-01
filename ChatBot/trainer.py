

d = dict()

# d["Hi"]= "Hello world"

def begin():
        botSays = "Hello!"
        while True:
            userInput = raw_input(botSays + '\n')
            if userInput == "break":
                    break
            d[botSays] = userInput
            botSays = userInput
            


begin()


print "here is the d: " ,d
