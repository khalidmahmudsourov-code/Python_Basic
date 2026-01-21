###########Average
# def get_avg(a,b,c):
#     return (a+b+c)/3

# print(get_avg(3,4,5))

################Length
# def get_length(list):
#     i = 0
#     for el in list:
#         i+=1
#     return i    

# numbers = [1,2,3,4,5]
# Series = ["Artugrul","Osman","Orhan"]
# print(get_length(numbers))
# print(get_length(Series))

######################Print element of a list in a single line
# def print_singleLine(list):
#     for el in list:
#         print(el,end=" ")

# numbers = [1,2,3,4,5,6,7,8,9,10]    
# print_singleLine(numbers)
# odd = ["No","yoo","joojoo","cool"]
# print_singleLine(odd)

###############Factorial
# def return_fact(n):
#     fact = 1
#     for el in range(1,n+1):
#         fact = fact*el
#     print(fact)

# return_fact(5)

####################Recursion
# def print_R(n):
#     if n==0:
#         return
#     print(n)
#     print_R(n-1)
# print_R(5)        

####################Factorial_Recursion
# def fact_rec(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact_rec(n-1)
# print(fact_rec(5))
###################Natural Sum
# def Nat_Sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n+Nat_Sum(n-1)
# print(Nat_Sum(10))
#####################Print List using recursion      
# def display(list,index):
#     if index == -1 :
#         return
#     else:
#         print(list[index],end=" ")
#         display(list,index-1)
# numbers = [12,22,33,44,15]
# length = len(numbers) - 1
# display(numbers,length)
# print()

# def display1(list,index):
#     if(index == len(list)):
#         return
#     else:
#         print(list[index],end=" ")
#         display1(list,index+1)
# numbers1 = [2,3,1,7,6,5]  
# display1(numbers1,0)      
