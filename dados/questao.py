import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats 

data= pd.DataFrame(
    {
        'idade': np.random.randint(18,70,size=200),
        'sastifacao': np.random.randint( 1,6, size=200),
        'segmento': np.random.choice(['A','B','C'], size=200)
    }
)
print(data)

listamedias=[]
listamedianas=[]
listamodas=[]

segmentos=sorted(data['segmento'].unique())
for segmento in segmentos:
    segmento_data = data[data['segmento']==segmento]['sastifacao']

    media=segmento_data.mean()
    mediana= segmento_data.median()
    moda= segmento_data.mode().iloc[0]
    listamedias.append(media)
    listamedianas.append(mediana)
    listamodas.append(moda)

    print(f'Segmento {segmento}:')
    print(f' Média de satisfação: {media}')
    print(f' Mediana de satisfação: {mediana}')
    print(f' Moda de satisfação: {moda}')
    print("\n")

dados_segmentos= {
    'Segmento': segmentos,
    'Média de Satisfação': listamedias,
    'Mediana de Satisfacao': listamedianas,
    'Moda de Satisfação': listamodas
}
df_segmentos= pd.DataFrame(dados_segmentos)
print(df_segmentos)