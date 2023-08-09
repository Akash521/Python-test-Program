# #1. program to reverse number 

# num = int(input("please enter number to reverse :"))
# reverse =0
# while num!=0:
#     reverse = reverse*10 + num%10
#     num=(num//10)
# print("this is reverse of %d " %reverse)    

#2. program to reverse string. 

# abc=""
# ab="akash"
# for i in ab:
#     # abc+=i
#     abc = i + abc
#     # abc.insert(0,i)
# # print(' '.join(str(e) for e in abc))
# print(abc)

#3. count character in list

# a=['a','b','r','b','a','r','a','a','a','b','b','s','y']
# count={}
# heightest_occ_name=0
# non_repeat=1
# for i in a:
#     if(i in count):
#         count[i] +=1
#     else:
#         count[i] =1

# print(count)
# for key, value in count.items():
#     if(heightest_occ_name < value):
#         heightest_occ_name = value
#         print(key)
#     elif(non_repeat == value):
#         print(key)


# print(heightest_occ_name)    # print()
# print(count)


# print(sorted(count))

#4. Check amestrong number 
# num=370
# num_list=[]
# for j in str(num):
#     num_list.append(int(j))
# l=len(num_list)
# sum=0
# for i in num_list:
#     sum=sum+pow(i,l)

# if(sum == num):
#     print('amestrong')
# else:
#     print('not amestrong')        

#5. check prime number
# def prime_check(num):
#     if(num < 2):
#        return "not prime"
#     else:
#         if(num == 2):
#             return "prime"
#         else:
#             for i in range(2,num):
#                 if(num % i == 0 ):
#                     return "not prime"
#             return "prime"
# print(prime_check(7))                        

#6. sum number
# d=23466
# a =0
# for i in str(d):
#     a+=int(i)
# print(a)

#7.swap two number without using thrid variable 
# a = 12 
# b =2
# a = a-b
# b= a+b
# a=b-a
# print(a)
# print(b)

# 8. swap two number using 3 variable
# a=12
# b=2
# temp =a
# a=b
# b=temp
# print(a)
# print(b)

#9. find average 
#total sum  number in list/length of list

#10. calculate factorial of number
# num =6 
# b=1
# for i in range(num+1):
#     if(i==0): 
#         pass
#     else:
#         b =b*i
# print(b)
    #print(i)

#11. sum 1 to 100 in one line 
#print(sum(range(1,100+1)))

#12. check odd or even

# num =56

# if(num%2 == 0):
#     print('even')
# else:
#     print('odd')    

#13. find power without using function of pow
# a = 2
# b=3
# c=1
# for i in range(1,b+1):
#     c=a*c
#     print(c)
# result=1;
# # while b != 0:
# for i in range(1,b+1):
#     result = 2 * result
#     # b-=1
# print(result)

#14. simple interest formula 

# simple interest = (principle * rate of interest * time)/100


#remove one character form the string and count of that occurnce



# str_1 = "akash borana"
# remove_char = 'a'
# results=""
# count=0
# for i in str_1:
#     # print(i)
#     if(remove_char == i):
#         # i =" "
#         results+=" "
#         count+=1;

#         # pass
#     else:
#         results+=i
        
# print(results) 
# print(count)   



# string="keep learning"
# print(string[:-1])
# 


#check string is palandrome or not 

# orignal_string = "madaw"
# for_palndrome=""

# for i in orignal_string:
    
#     for_palndrome = i+for_palndrome
#     print(for_palndrome)

# print(for_palndrome)
# if(orignal_string == for_palndrome):
#     print("pailendrom")
# else:
#     print("not pailendrom")   
# v
# 
# check given character is vowel
# 
# voval = ['a','e','i','o,','u','A','E','I','O','U']
# given_letter = "O" 
# for i in voval:
#     if(given_letter == i):
#         given_letter="-"
#         print(given_letter)
#     else:
#         pass   

# check word is string or int
# given_word = 'f'
# print(type(given_word))

# if(type(given_word) == 'str'):
#     print('string')
# elif(type(given_word) == 'int'):
#     print('int')    

#sum number from the scring 
# strin_1="1abc12312"
# count=0
# for i in strin_1:
#     if(i >='a' and i<='z'):
#         # print(i)
#         pass
#     # else:
#     #     print(type(int(i)))    
#     elif(int(i)>=0 and int(i)<=9):
#         count+=int(i)
# print(count)    


# str_1="akash"
# str_2="borana"
# print("".join([str_1,str_2]))




# ,'z','d','k'

# ab=['a','b','g','s','c']
# ba=[]
# bas=""


# for i in ab:
#     if(i>bas or bas == ""):
#         ba.append(i)
    

    
    # print(len(ba))
    # if(len(ba) ==0):
    #     print(i)
    #     ba.append(i)
    #     ab.remove(i)
    # else:
    #    ba.append(i) 
    #    print(i)
    # print(ba)
        # for j in ba:
        #     print(i+" "+ j)
        #     if(i >j):
        #         # print(i)
        #         print(ba.index(i))
        #         # ba.insert( ba.index(i) +1,i)
        #         # ab.remove(i)


        #     elif(i<j):
        #         ba.index(i)
                # print(i)
                # ba.index(i)
                # ba.insert( ba.index(i) - 1,i)
                # ab.remove(i)




                                
        # pass

# print(ab)  
# print(ba)  
# print(ba)
# print(ab)

       
            # 
            # print(j)
# sort_ab=""
# sorted_arry=[]
# for i in ab:
#     if(i>=sort_ab):
#         sort_ab = i
#         for j in sorted_arry:
#             if(sort_ab )
#         print(i)



#find missing number 


# num=[1,2,3,4,5,6,7,9,10,11,12,13]
# count=0
# missing_number=[]
# for i in num:
#     count+=1
#     if(count == i ):
#         pass
#     else:
#         missing_number.append(count)
#         num.insert(count,i)

# print(missing_number)
# print(num)            


#reverse num

# num=2000333
# reverse_num=''

# # reverse_num=[x for x in str(num) ]

# # print(reverse_num)
# new_list = [x for x in range(1,101) if x < 5]
# print(new_list)

# for i in str(num):
#     reverse_num=i+reverse_num

# print(type(int(reverse_num)))

    

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# fromaddr = "blog.approval@datafeedai.com"
# toaddr = "admin@datafeedai.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Test Subject"
# body = "Write your message here"
# msg.attach(MIMEText(body, 'plain'))
# server = smtplib.SMTP('smtp.zoho.in:587')
# server.starttls()
# server.login(fromaddr, "Akash123#")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()


# docker run -itd --network host --name back-1 backend
# docker run -itd --network host --name frontend frontend

# Backend
# sudo apt update
# apt install python3-pip -y


# Frontend

# sudo apt update
# sudo apt install nodejs -y
# sudo apt install npm -y
#  npm i serve

# snap install serve
# serve -b 0.0.0.0 build


# Write a program to convert List of Dictionaries to List of Lists.
test_list = [{'a': 123, 'b': 10}, {'a': 51, 'b': 7}] 
# Output = [[‘a’, ‘b’], [123, 10], [51, 7]]

parr_dict =[]
li_key=[]
val_dic = []


for i in test_list:
    for key,values in i.items():
        if(key in li_key):
            pass
        else:
            li_key.append(key)

        if(values in val_dic):
            pass
        else:
            val_dic.append(values) 
   
    parr_dict.append(val_dic) 
    val_dic = []       
parr_dict.append(li_key)        
print(parr_dict)




# Write a program to create Nested Dictionary using given List.
# a = {'a': 4, 'b': 5, 'c': 9} 
# b = [8, 3, 2] 
# c= {8: {'a': 4}, 3: {'b': 5}, 2: {'c': 9}}

# dict_t ={}

# for i in b:
#     # print(i)
#     for key, values in a.items():
#         # print(key)
#         dict_t[i]={key:values}
#         a.pop(key)
#         break 
# print(dict_t)
    # i = 



