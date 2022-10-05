import pandas as pd

DATABASE_PATH = "club.csv"


def calcula_prob(nom1,nom2,temp1,temp2):
    a_gana=(temp1/(temp1+temp2+2))
    b_gana=(temp2/(temp1+temp2+2))
    empate= 1-(a_gana)-(b_gana)
    return f'La probabilidad de que {nom1} equipo gane al {nom2} es del {a_gana*100}%\nLa probabilidad de que {nom2} equipo gane al {nom1} es del {b_gana*100}%\nLa probabilidad de empate es del {empate*100}%'
    
df = pd.read_csv(DATABASE_PATH)
price=df['Market Value Of Club In Millions(£)'].tolist()
clubes=df['Club Name'].tolist()
players=df['Average Age Of Players'].tolist()
div=[]

for i in range(len(price)):
    x=price[i]/players[i]
    div.append(x)

lista_cb=[]

for i in range(len(price)):
    lista_cb.append([clubes[i],div[i]])
print(lista_cb)

#lista_cb[nombres][($)/media_edad]
print('=================================')
print('        TODOS LOS CLUBES')
print('      Y SUS PRECIO/MEDIA EDAD')
print('=================================')
for i in range(len(lista_cb)):
    print(f'Club: {lista_cb[i][0]}\nPrecio/Edad: {lista_cb[i][1]}\n\n')
print('=================================\n\n')

pre1=input('Elegir club para comparar (1): ')
pre2=input('Elegir club para comparar (2): ')

temp1=0
temp2=0
nom1=''
nom2=''

for i in range(len(lista_cb)):
    if(lista_cb[i][0]==pre1):
        nom1=lista_cb[i][0]
        temp1=lista_cb[i][1]
    elif(lista_cb[i][0]==pre2):
        nom2=lista_cb[i][0]
        temp2=lista_cb[i][1]


print(calcula_prob(nom1,nom2,temp1,temp2))