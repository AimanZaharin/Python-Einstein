def main():

    mass = int(input("m: "))
    calc(mass)

def calc(mass):

    total = mass * 300000000 * 300000000 
    print("E:", total)

main()