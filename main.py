import random
import art


def deal_card():
    """
    Returns a random card from the list of cards
    :return:
    """
    list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(list_of_cards)
    return card


def calculate_score(cards: list):
    """
    Calculates the score of each player by adding up the
    individual card values
    :param cards:
    :return:
    """
    if 10 in cards and 11 in cards and len(cards) == 2:
        # 0 represents blackjack
        return 0

    score = sum(cards)

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score


def compare(score_c, score_u):
    """
    Compares the scores of both the players and gives a result on whether it
    was a win, lose or draw for the user
    :param score_c:
    :param score_u:
    :return:
    """

    if score_c == score_u:
        print("It's a draw!")

    elif score_c == 0 or score_u > 21:
        print("You lose!")

    elif score_u == 0 or score_c > 21:
        print("You win!")

    else:
        if score_c > score_u:
            print("You lose!")

        elif score_u > score_c:
            print("You win!")


def main():

    user_cards = []
    computer_cards = []
    is_game_over = False

    user_score = None
    computer_score = None

    print(art.logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your cards: {user_cards},   Your score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card and type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(computer_score, user_score)
    print("")
    print("")
    print("")
    should_restart = input("Do you want to restart the game? Press 'y' to restart and 'n' to end the game: ")

    if should_restart == 'y':
        main()
    else:
        return


if __name__ == '__main__':
    main()
