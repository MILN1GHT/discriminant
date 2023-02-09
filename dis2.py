count = 1

"""MAIN CLASS"""
class Mat():
    def disc(self): #function for finding the discriminant
        disc = b ** 2 - 4 * a * c #the basic discriminant formula
        print(disc)

        if disc > 0: #formulas in case the discriminant is greater than 0
            x1 = ((-b) - disc ** 0.5)
            x2 = ((-b) + disc ** 0.5)
            print(x1)
            print(x2)

        elif disc == 0: #function if the discriminant is 0
            x1 = x2 = -b / 2 * a
        else: #if the discriminant is less than zero
            print('root not detected')


m = Mat()

"""MAIN CYCLE"""
while count !=0:
    z = input('discriminant search (y - yes, n - no): ')
    if z == 'y':
        a = float(input('a: ')) #coefficient values
        b = float(input('b: '))
        c = float(input('c: '))

        m.disc()

    elif z == 'n':
        print('Okay, I will see you next time.')
        break

    else:
        print('there is no such option:(')
        break








