# def fa(n):
#     for i in range(1,n):
#         result=( n-1 *1  )
#     return result+1
# print(fa(5))


# def factorielle(n):
#    if n == 0:
#       return 1
#    else:
#       F = 1
#       for i in range(2,n+1):
#          F = F * i

#       return F
# print(factorielle(5))

# facto = lambda n: n * facto(n-1) if n != 0 else 1
# print(facto(7))



# F = []
# for k in range(50):
#    F.append( factorielle(k) )
# print(factorielle(7))
# ----------------------------------FACTORIELLLE-----------------------#
# def facto(n):
#     if type(n) is not int  or n<=0:
#         return 1
#     else:
#         return n*facto(n-1) 
# print(facto(-1))
# print(facto(5))

# def factorielle(n):
#     if n == 0:
#         return 1
#     else:
#         return n  * factorielle(n-1)
# print(factorielle(5))


# ----------------------------------AGE-----------------------#
# def age(a):
#     if type(a) is int:
#         if a<=7:
#             return "enfant"
#         elif 8<a<18:
#             return "adolescent"
#         elif 19<a<45:
#             return "jeune"
#         else:
#             return "vieillard"
#     else:
#         return -1
# print(age(6))
# print(age(12))
# print(age(43))
# print(age(50))
# print(age("12"))
# print(age(12.3))
# print(age(-2))


# ----------------------------------AGE-----------------------#
# a= dict()
# print(dict())
def facto(n):
    if n==0:
        return -1
    else:
        return n*facto(n-1)
print(facto(5))
