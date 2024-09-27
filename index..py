# def Prime():
#     tem=True
#     er=n//2
#     for i in range(1,er+1):
#         if n%i==0:
#             print(i)
#             break
# n=int(input('entetr '))                   
# Prime()

# ---------------String Reversal (increment loop)---------------

# def NewR(strN):
#     newSTRR=""
#     for i in range(0,len(strN)):
#         newSTRR=strN[i]+newSTRR
#     return newSTRR
# strN=input("enter a nuw str")
# resul=NewR(strN)
# print(resul)



# reversed sentance---------------

# def Reversal_loop(nstr, i, s1):
#     if i == len(s1):
#         return nstr
#     nstr = s1[i] + nstr
#     return Reversal_loop(nstr, i + 1, s1)
# s1 = input("enter a new string : ")
# result = Reversal_loop("", 0, s1)
# print(result)