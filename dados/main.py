import numpy as np
import pandas as pd
import random
 #lista de números 

# Gerar 5 números aleatórios entre 1 e 10 
lista_aleatoria = [random.randint(1, 100) for c in range(20)]
print(lista_aleatoria)

#Calcular a média dos números
media= np.mean(lista_aleatoria)
print(f'A média dos números gerados é: {media} ')

#Identificar os números maiores que a média
maiores_que_media=[num for num in lista_aleatoria if num>media] #significa “para cada número num na lista numeros, inclua num na nova lista soment se ele for maior que media”
print(f'Números maiores que a média: {maiores_que_media}')

#Armazenar os números em um DataFrame do pandas
df_maiores= pd.DataFrame(maiores_que_media,columns=["Números maiores que a Média"])

#Salvar o DataFrame em um arquivo CSV
df_maiores.to_csv("numeros_maiores_que_media.csv", index=False)

print("Arquivo 'numeros_maiores_que_media.csv' salvo com sucesso.")

