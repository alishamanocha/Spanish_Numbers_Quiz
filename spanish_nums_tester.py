from random import choice, random
import random

numbers_file = "spanish_numbers.txt" # contains words for all numbers 0-99 and words for 100, 200, 300, etc.

with open(numbers_file, 'r') as f:
    lines = f.read().splitlines() # put lines from file into list
    tens_and_ones = []
    hundreds=[]
    for x in range(100):
        tens_and_ones.append(lines[x]) # list for words for numbers 0-99
    for x in range(100, 109):
        hundreds.append(lines[x]) # list for words for 100, 200, 300, etc.

def select_num():
    numeral = random.randint(0,1000000000) # pick a random number up until 999,999,999 to quiz the user on
    return numeral

def three_dig_num(numeral): # convert number up until 999 to words (ex. 931 --> novecientos treinta y uno)
    if (numeral==100): # exception: 100 is "cien"
        return hundreds[0][0:4]
    hund_dig = int(numeral/100)
    ten_and_one_dig = numeral%100
    number=""
    if (hund_dig>0): # add hundreds digit to string if applicable
        number+=hundreds[hund_dig-1]
        if (ten_and_one_dig>0):
            number+=" "
    if (ten_and_one_dig>0): # add tens and ones digit to string if applicable
        number+=tens_and_ones[ten_and_one_dig]
    return number

def correct_answer(numeral): # find the full correct translation for any number
    if (numeral==0): # exception: 0 is "cero"
        return tens_and_ones[0]
    else:
        dig_seven_to_nine = numeral % 1000 # hundreds digits
        numeral = int(numeral/1000)
        dig_four_to_six = numeral % 1000 # thousands digits
        numeral= int(numeral/1000)
        dig_one_to_three = numeral # millions digits
        answer=""
        if (dig_one_to_three==1): # one million
            answer += "un millón "
        elif (dig_one_to_three>0): # add millions digits to string if applicable
            answer+= three_dig_num(dig_one_to_three)
            if (answer[len(answer)-3:] == "uno"):
                answer=answer[0:len(answer)-1]
            answer+=" millones "
        if (dig_four_to_six>1): # add thousands digits to string if applicable
            answer+= three_dig_num(dig_four_to_six)
            if (answer[len(answer)-3:] == "uno"):
                answer=answer[0:len(answer)-1]
        if (dig_four_to_six>0):
            answer+= " mil "
        if (dig_seven_to_nine>0): # add hundreds digits to string if applicable
            answer+=three_dig_num(dig_seven_to_nine) 
    return answer.strip(" ")

def check_answer(numeral, answer): # check if user's answer is correct
    return (correct_answer(numeral)==answer.lower()) 

if __name__ == '__main__' :
    print("Welcome to the Spanish Numbers Quiz! You will be tested on numbers as large as 999999999. Type \"stop\" at any time to stop the quiz!")
    continue_playing = True
    while (continue_playing):
            continue_trying = True
            random_num = select_num()
            # give user random number
            print("The number is: " + str(random_num) + ". How do you say this in Spanish? (Type \"give up\" to see the correct answer.)") 
            user_ans = input()
            if user_ans.lower() == 'stop': # quit the quiz
                print("Goodbye!")
                continue_playing = False
                break
            if user_ans.lower() == 'give up': # give up on the question
                print("The correct answer is: " + correct_answer(random_num) + ".")
                continue_trying = False
            while (continue_trying and not check_answer(random_num, user_ans)): # wrong answers
                print("That is not the correct answer. Try again!")
                user_ans = input()
                if user_ans.lower() == 'stop':
                    print("Goodbye!")
                    continue_playing = False
                    break
                if user_ans.lower() == 'give up':
                    print("The correct answer is: " + correct_answer(random_num) + ".")
                    continue_trying = False
            if (continue_trying and continue_playing):
                print("That is correct!")
            
