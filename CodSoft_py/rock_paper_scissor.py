import random

def find_winner(test_list): # This fuction works perfectly
    table = {
        ('R','S') : 'U',
        ('P','R') : 'U',
        ('S','P') : 'U',
        ('P','S') : 'C',
        ('S','R') : 'C',
        ('R','P') : 'C'
    }

    if test_list in table:
        return table[test_list]


def main_game(user:str, score:dict): 
    print()
    print('Choose :')
    print('R for Rock')
    print('P for Paper')
    print('S for Scissors')
    u_choice = input()

    elements = ['R', 'P', 'S']
    c_choice:str = random.sample(elements, 1)
    c_choice : str = c_choice[0]
    # print('computer choice : ' + c_choice)

    # score = {user:0, 'computer':0}

    if u_choice == c_choice:
        pass

    test_list = (u_choice, c_choice)
    # print(test_list)

    winner = find_winner(test_list)
    print(winner)
    if winner == 'U':
        score[user] = score[user] + 1
    if winner == 'C':
        score['computer'] = score['computer'] + 1
    
    print(user + '\'s choice = ' + u_choice + ' and computer\'s choice = ' + c_choice)
    
    return winner
        
# MAIN
if __name__ == '__main__':
    user = input("Enter your name : ")
    print()

    print("Press S to start or press any key to end the game: ")
    choice = input()
    
    score = {user:0, 'computer':0}

    while choice == 'S':
        winner = main_game(user, score)
        if winner == 'U':
            print("\'" + user + " Won \'")
        else:
            print("\'Computer Won\'")
        print(score)
        print("Press S to start or press any key to end the game: ")
        choice = input()
        
    if choice != 'S':
        print("You quitted the game")
        print("FINAL SCORE")
        print(score)
