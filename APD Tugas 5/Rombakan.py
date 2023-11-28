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
        sortedItems = bubble_sort(nineHoleCourse)
        for i, j in sortedItems:
            print(f'{i} : {j}')
    elif course == '2':
        sortedItems = bubble_sort(eighteenHoleCourse)
        for i, j in sortedItems:
            print(f'{i} : {j}')


def update(course, scorer, score):
    if course == '1':
        nineHoleCourse[scorer] = score
    elif course == '2':
        eighteenHoleCourse[scorer] = score


def delete(course, scorer):
    if course == '1':
        del nineHoleCourse[scorer]
    elif course == '2':
        del eighteenHoleCourse[scorer]


def bubble_sort(course):
    items = list(course.items())
    n = len(items)

    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


def search(course, name):
    foundScorers = []

    if course == '1':
        courseName = '9 Hole Course'
        for scorer, score in nineHoleCourse.items():
            if name.lower() in scorer.lower():
                foundScorers.append((scorer, score))
    elif course == '2':
        courseName = '18 Hole Course'
        for scorer, score in eighteenHoleCourse.items():
            if name.lower() in scorer.lower():
                foundScorers.append((scorer, score))

    if foundScorers:
        print(f"Scorer is found in {courseName} with the keyword '{name}':")
        for scorer, score in foundScorers:
            print(f"{scorer} : {score}")
    else:
        print(f"No scorers found with the keyword '{name}'.")


def filtered(course, threshold):
    belowThresholdScorers = []

    if course == '1':
        courseName = '9 Hole Course'
        for scorer, score in nineHoleCourse.items():
            if score <= threshold:
                belowThresholdScorers.append((scorer, score))
    elif course == '2':
        courseName = '18 Hole Course'
        for scorer, score in eighteenHoleCourse.items():
            if score <= threshold:
                belowThresholdScorers.append((scorer, score))

    if belowThresholdScorers:
        print(f"Scorers in {courseName} with scores higher than {threshold}:")
        for scorer, score in belowThresholdScorers:
            print(f"{scorer} : {score}")
    else:
        print(f"No scorers found in {courseName} with scores higher than {threshold}.")


def main():
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
                        try:
                            while True:
                                print('Enter a name to associate the score:')
                                name = str(input(''))
                                print('Enter the score you obtained:')
                                score = int(input(''))
                                create(course, name, score)
                                print('Score has been added/updated')
                                break
                        except ValueError:
                            print('Enter a valid number')
                    else:
                        print("Selection must be what's shown!")
                    break


            case '2':
                while True:
                    print('')
                    print('1. The 9 Hole Course')
                    print('2. The 18 Hole Course')
                    print("Choose which course's scores you would like to look at:")
                    course = str(input(''))
                    os.system('cls')
                    if course == '1' or course == '2':
                        while True:
                            print('1. Sorted according to scores')
                            print("2. Search a scorer's score")
                            print('3. Filter out some scores')
                            print('Which option would you like to choose?')
                            selection = str(input(''))
                            match selection:
                                case '1':
                                    read(course)
                                    break
                                case '2':
                                    print('Enter the name you would like to search for:')
                                    name = str(input(''))
                                    search(course, name)
                                    break
                                case '3':
                                    while True:
                                        try:
                                            print('Enter the threshold to filter out:')
                                            threshold = int(input(''))
                                            filtered(course, threshold)
                                            break
                                        except ValueError:
                                            print('Enter a valid number')
                        break
                    else:
                        print("Selection must be what's shown!")
                    break

            case '3':
                while True:
                    print('')
                    print('1. The 9 Hole Course')
                    print('2. The 18 Hole Course')
                    print("Choose which course's score had an improvement in:")
                    course = str(input(''))
                    os.system('cls')
                    if course == '1' or course == '2':
                        while True:
                            read(course)
                            print('Type the name of the scorer:')
                            scorer = str(input(''))
                            while True:
                                try:
                                    if course == '1' and scorer in nineHoleCourse:
                                        print('\nEnter the new score')
                                        score = int(input(''))
                                        update(course, scorer, score)
                                        print('Score has been updated')
                                        break
                                    elif course == '2' and scorer in eighteenHoleCourse:
                                        print('\nEnter the new score')
                                        score = int(input(''))
                                        update(course, scorer, score)
                                        print('Score has been updated')
                                        break
                                    else:
                                        print('Please input the right name')
                                except(ValueError):
                                    print('Enter a valid number')
                            break
                    else:
                        print("Selection must be what's shown!")
                    break

                
            case '4':
                while True:
                    print('')
                    print('1. The 9 Hole Course')
                    print('2. The 18 Hole Course')
                    print("Choose which course's score you would like to delete:")
                    course = str(input(''))
                    if course == '1' or course == '2':
                        while True:
                            read(course)
                            print('Type the name of the scorer:')
                            scorer = str(input(''))
                            if course == '1' and scorer in nineHoleCourse:
                                delete(course, scorer)
                                print(f"{scorer} deleted from nineHoleCourse.")
                                break
                            elif course == '2' and scorer in eighteenHoleCourse:
                                delete(course, scorer)
                                print(f"{scorer} deleted from eighteenHoleCourse.")
                                break
                            else:
                                print('Please input the right name')
                    else:
                        print("Selection must be what's shown!")
                    break

                
            case _:
                print("Selection must be what's shown!")


if __name__ == '__main__':
    main()