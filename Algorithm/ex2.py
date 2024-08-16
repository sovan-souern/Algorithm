# ex1:

# text="Hello"
# for i in range(len(text)):
#     print(text[i])
# ex2:

# text="Hello"
# for i in range(len(text)):
#     print(i)
# ex3:

# text=input("Enter your text: ")
# result="No"
# for i in range (len(text)):
#     if text[i].upper()==text[i]:
#         result="Yes"
# print(result)

# ex4

# text = input("Enter Text : ")
# result = 0
# letter = ""
# for i in range(len(text)):
#     if text[i] == " ":
#         letter += ""
#     else:
#         letter += text[i]
#         result += int(text[i])
# print(letter)
# print("Total :",result)

# ex5
# Q1:

# text = "454639"
# odd_count = 0
# even_count = 0

# for char in text:
#     if int(char) % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(odd_count)
# print(even_count)

# Q2:

# text = "454639"
# sum = 0 
# for i in range(len(text)):
#     sum += int(text[i])
# print(sum)



# Q3 
# text = "454639"
# sum = 0
# for i in range(len(text)):
#     num = int(text[i])
#     if num % 2 == 0:
#         sum += num
# print(sum)


# Q4

text = "454639"
result = ""
for i in range(len(text) - 1, -1, -1):
    result += text[i]
print(result)

# Q4
# text = "454639"
# lastindex = len(text) - 1
# result = ""
# for i in range(len(text)):
#     result += text[lastindex-i]
# print(result)

# ex6:

# num=int(input("Enter your num: "))
# if num%2==1:
#     print("odd")
# else:
#     print("even")

#Ex7:

# isfound_num=False
# while not isfound_num:
#     num=int(input("enter your num: "))
#     if num >=10 and num <=20:
#         print("Continue")
#     else:
#         isfound_num=True
# print("Out of range")


#Ex8:
# Q1

# text = "9394884039"
# count_8 = 0
# for i in range(len(text)):
#    if text[i] == "8":
#       count_8 += 1
# print(count_8)

# Q2

# text = "9394884039"
# isfound=False
# index=0
# while not isfound:
#     if text[index] == '8':
#         print(index)
#         isfound=True
#     index+=1



#Ex9:

# Q1:
# string = "3 4 5 6"
# result=""
# for cha in string:
#     if cha!=" ":
#        result+=cha
# print(result)

# Q2