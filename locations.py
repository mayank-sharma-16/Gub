import random 

def get_country():
    f = open('files/countries.txt')
    countries = f.readline().split(',')
    f.close()
    return(random.choice(countries))