#14720번
##내 코드
store_num=int(input("우유 가게의 수를 입력하시오:"))
count=0
store_info=list(map(int,input().split()))   # 가게별로 우유 정보 배치  
current_milk=-1
for i in range(store_num):
    if store_info[i]==(current_milk+1)%3:
        count+=1
        current_milk+=1
print(count)
##구글링코드
'''market=int(input())
market_list=list(map(int,input().split()))
count=0
current_milk=-1
for i in range(len(market_list)):
    if market_list[i]==(current_milk+1)%3:
        count+=1
        current_milk+=1
print(count)'''