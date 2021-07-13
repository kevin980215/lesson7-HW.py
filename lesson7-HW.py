def BIF(num,score):             
  max_num = max(score)          
  min_num = min(score)          
  sum_num = sum(score)          
  avg_num = sum_num/num         
  return max_num,min_num,sum_num,avg_num 

num= input("多少人?")     
num=int(num)
score_list = []         

for i in range(num):         
    score=input('分數')
    score_list.append(int(score))        
print(score_list)

x = BIF(num,score_list)     
print("最高分:",x[0],"最低分:",x[1],"總分:",x[2],"平均分:",x[3])       