'''num=int(input("숫자를 입력하세요:"))
for i in range(10):
    print(num,"*",i,"=",num*i)'''
'''for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end=" ")
    print("")'''
'''for i in range(10):
    if (i%2==0):
        continue
    print(i)'''
## 자료형 List
'''scorelist=[10,20,30,40,50]
type(scorelist)
print(scorelist[0])
scorelist[4]=100
print(scorelist[4])
print(len(scorelist))
print(scorelist)

scorelist2=[1,2,3,4,5]
print(scorelist+scorelist2)
scorelist2[-1]

scorelist2.append(100) #list 값 추가
print(scorelist2)
scorelist2.remove(5)  #특정한 값을 삭제
print(scorelist2)
del scorelist2[2]  #특정한 인덱스의 값을 삭제
print(scorelist2)
4 in scorelist2 #특정한 값이 리스트에 있는지 확인, 있으면 true 없으면 false'''

#로또 번호 자동 생성기
#1~45까지의 숫자를 랜덤하게 6개 출력해주는 프로그램
import random # 파이썬의 random 모듈 
#random.randint #randint는 끝자리까지 포함함 ex) random.randint(1,6)이면 1부터 6까지 랜덤생성
'''for _ in range(6)'''# for ~ in 사이에 변수를 사용하지 않을시 '_'로 표현하자!
lottonum=[]
while len(lottonum)<6:
    num=random.randint(1,45)
    if num not in lottonum:
        lottonum.append(num)
print(lottonum)
