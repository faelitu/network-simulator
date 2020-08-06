import random as rd

def aleatorio():
    rd.seed(a=55) # DEVELOPMENT
    #rd.seed() # PRODUCTION

    u = rd.random() # Generate a number between [0.0, 1.0)
    u = 1.0 - u # Returns a number between (0.0, 1.0]
    return u

print(aleatorio())