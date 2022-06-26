import re

s1= 'Hola buenos dias a todos'
s2= 'Hola buenas tardes a todos'
s3= 'Hola buenas noches a todos'

patron1='dias'
# print(re.search(patron1,s1))           #Realiza busqueda de patron en s1
# print(re.search(patron1,s2))           #Realiza busqueda de patron en s2

ret=re.search(patron1,s1)
if ret:
    print(ret)

