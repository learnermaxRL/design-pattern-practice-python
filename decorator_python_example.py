
def beautiful_addition(func):
    def wrapper(*args,**kwargs):
        print ("you are trying to add {}-{}".format(args[0],args[1]))
        func(*args,**kwargs)
        print("Congratulations!")
    
    return wrapper

@beautiful_addition
def plain_addition(x,y):
    print(x+y)
    
    
plain_addition(5,6)