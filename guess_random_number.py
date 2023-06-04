import random

#1~1000 사이의 숫자 중 하나를 고름.
hit_number= random.randint(1, 1001)

#사용자가 맞추게 될 20번의 리스트를 만듬.
guess_count_list = range(1, 21, 1)

#초기값은 실패값으로 넣어줌.
passfail = False

#20번간 반복함. 사용자가 맞출 경우 멈춤.
for guess_count in guess_count_list :

    guess = int(input("숫자를 맞혀보세요("+str(guess_count)+"번째 시도): "))

    if hit_number == guess:
        passfail = True
        break
    elif hit_number> guess:
        print(str("guess")+"보다 큽니다.", end="")
    else:
        print(str("guess")+"보다 작습니다.", end="")

if passfail == True:
    print("맞췄습니다. 축하합니다.")
else :
    print("모든 기회를 다 사용하셨습니다. 다음에 다시 도전하세요.")
