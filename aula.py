import streamlit as st
import pandas as pd

st.image('IMG-20200103-WA0000.jpg',use_column_width= 'always')

paginas = ['Home', 'Rascunhos', 'Gráficos']

pagina = st.sidebar.selectbox('Seleciona a página que você deseja', paginas)

dados = pd.read_excel('CLJ1.xlsx')

if pagina == 'Home': 
    st.markdown('# Meu Web App*')

    st.write(dados)

if pagina == 'Rascunhos':
    

    var = st.sidebar.selectbox('Selecione uma variável: ',['TIPO', 'PARTICIPANTE'])

    ms= dados['VALOR'].groupby(dados[var]).mean()

    st.write(ms)
    st.table(ms)
    st.table(dados.describe())

if pagina == 'Gráficos': 

    variaveis = dados.columns.tolist()  

    var1 = st.selectbox('Selecione uma variável: ',variaveis)

    plot = dados['PARTICIPANTE'].value_counts().plot(kind = 'barh')
    st.pyplot(plot.figure)

    plot = dados[var1].value_counts().plot(kind = 'barh')
    st.pyplot(plot.figure)


    plot = dados['VALOR'].groupby(dados[var1]).mean().plot(kind = 'barh')
    st.pyplot(plot.figure)
