import numpy as np
def edit(s1:str,s2:str):
    """_summary_

    Args:
        s1 (str): _description_
        s2 (str): _description_
    """
    if s1== " " or s2== " " or s1==s2:
        return 0
    if len(s1)==len(s2) and len(s1)<=1 and len(s2)<=1:
        return len(s1)
    if len(s1)==0:
         return len(s2)
    if len(s2)==0:
        return len(s1)
    
    m,n= len(s1)+1,len(s2)+1
    Edit =np.zeros((m,n))
    
    for i in range(m):
        Edit[i,0]=i
    for j in range(n):
        Edit[0,j]=j
    for i in range(1,m):
        for j in range(1,n):
            ins=Edit[i,j-1]+1
            dell = Edit[i-1,j]+1
            if s1[i-1]==s2[j-1]:
                rep = Edit[i-1,j-1]
                
            else:
                rep = Edit[i-1,j-1]+1
            Edit[i,j]=min(ins,dell,rep)
    return int(Edit[m-1,n-1])





word1 = "horse",
word2 = "ros"
# 需要进行一次删除和替换      
print(edit("ab","bc"))
  
  

# def Levenshtein_Distance_Recursive(str1, str2):

#     if len(str1) == 0:
#         return len(str2)
#     elif len(str2) == 0:
#         return len(str1)
#     elif str1 == str2:
#         return 0

#     if str1[len(str1)-1] == str2[len(str2)-1]:
#         d = 0
#     else:
#         d = 1
    
#     return min(Levenshtein_Distance_Recursive(str1, str2[:-1]) + 1,# inserction
#                 Levenshtein_Distance_Recursive(str1[:-1], str2) + 1,# delet
#                 Levenshtein_Distance_Recursive(str1[:-1], str2[:-1]) + d)# replace

# print(Levenshtein_Distance_Recursive("abc", "bd"))
 