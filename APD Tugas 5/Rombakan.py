import os

nineHoleCourse = {'Kira' : 55,
                  'Athrun' : 55,
                  'Mu' : 43
                  }
eighteenHoleCourse = {'Amuro' : 78,
                       'Quattro' : 100,
                       'Kamille' : 89,
                       'Banagher' : 80
                       }


def create(course, name, score):
    if course == '1':
        nineHoleCourse.update({name : score})
    elif course == '2':
        eighteenHoleCourse.update({name : score})


def read(course):
    if course == '1':
        sorted_items = bubble_sort(nineHoleCourse)
        for i, j in sorted_items:
            print(f'{i} : {j}')
    elif course == '2':
        sorted_items = bubble_sort(eighteenHoleCourse)
        for i, j in sorted_items:
            print(f'{i} : {j}')


def update(course, scorer, score):
    if course == '1':
        nineHoleCourse[scorer] = score
    elif course == '2':
        eighteenHoleCourse[scorer] = score


def delete(course, scorer):
    if course == '1':
        del nineHoleCourse[scorer]
        print(f"{scorer} deleted from nineHoleCourse.")
        
    elif course == '2':
        del eighteenHoleCourse[scorer]
        print(f"{scorer} deleted from eighteenHoleCourse.")


def bubble_sort(course):
    items = list(course.items())
    n = len(items)

    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


while True:
    print('')
    print('Welcome to Golf IT Club')
    print('1. Add a score')
    print('2. Read scores')
    print('3. Update a score')
    print('4. Delete a score')
    print('What would you like to do?')
    
    selection_menu = str(input(''))
    os.system('cls')
    match selection_menu:
        case '1':
            while True:
                print('1. The 9 Hole Course')
                print('2. The 18 Hole Course')
                print('Choose which course you played in:')
                course = str(input(''))
                os.system('cls')
                if course == '1' or course == '2':
                    print('Enter a name to associate the score:')
                    name = str(input(''))
                    print('Enter the score you obtained:')
                    score = int(input(''))
                    create(course, name, score)
                    break
                else:
                    print("Selection must be what's shown!")


        case '2':
            while True:
                print('1. The 9 Hole Course')
                print('2. The 18 Hole Course')
                print("Choose which course's scores you would like to look at:")
                course = str(input(''))
                os.system('cls')
                if course == '1' or course == '2':
                    read(course)
                    break
                else:
                    print("Selection must be what's shown!")


        case '3':
            while True:
                print('1. The 9 Hole Course')
                print('2. The 18 Hole Course')
                print("Choose which course's score had an improvement in (C to return to main menu):")
                course = str(input(''))
                os.system('cls')
                if course == '1' or course == '2':
                    while True:
                        read(course)
                        print('Type the name of the scorer:')
                        scorer = str(input(''))
                        if course == '1' and scorer in nineHoleCourse:
                            print('\nEnter the new score')
                            score = int(input(''))
                            update(course, scorer, score)
                            break
                        elif course == '2' and scorer in eighteenHoleCourse:
                            print('\nEnter the new score')
                            score = int(input(''))
                            update(course, scorer, score)
                            break
                        else:
                            print('Please input the right name')
                elif course.upper() == 'C':
                    break
                else:
                    print("Selection must be what's shown!")

            
        case '4':
            while True:
                print('1. The 9 Hole Course')
                print('2. The 18 Hole Course')
                print("Choose which course's score you would like to delete (C to return to main menu):")
                course = str(input(''))
                if course == '1' or course == '2':
                    while True:
                        read(course)
                        print('Type the name of the scorer:')
                        scorer = str(input(''))
                        if course == '1' and scorer in nineHoleCourse:
                            delete(course, scorer)
                            break
                        elif course == '2' and scorer in eighteenHoleCourse:
                            delete(course, scorer)
                            break
                        else:
                            print('Please input the right name')
                elif course.upper() == 'C':
                    break
                else:
                    print("Selection must be what's shown!")

            
        case _:
            print("Selection must be what's shown!")