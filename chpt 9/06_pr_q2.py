
def game():
    return int(input("enter score"))

score = game()
with open('highscore.txt') as f:
    str_hiscore = f.read()

# if str(str_hiscore) == "":                            #works with input taken manually or input is in str format
#     with open('highscore.txt', 'w') as f:
#         f.write(str(score))

if int(str_hiscore)<score:
    with open('highscore.txt', 'w') as f:
        f.write(str(score))

elif int(str_hiscore)>score:
    print("try again")

