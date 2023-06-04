import random   #radom 모듈을 불러옴.

#사용자가 입력한 값을 ,와 공백으로 분리함.
guess_str = input("1~45 번호 6개를 쉼표로 분리하여 입력하세요: ").split(", ")
#새 리스트 공간을 만듬.
guess_list = list()

#사용자가 입력한 값을 리스트에 넣음.
for i in guess_str : 
    guess_list.append(int(i))

#로또 숫자를 추출함.
lotto_list = random.sample(range(1, 46, 1), 6)

#사용자가 입력한 값과 로또 숫자가 맞는지 확인함.
hit_count = 0;
for num in guess_list:
    if num in lotto_list:
        hit_count += 1
        
print('입력한 번호는'+str(guess_list)+"입니다.")
print("추첨된 번호는"+str(lotto_list)+"입니다.")
print("축하합니다."+str(hit_count)+"개 맞혔습니다.")
