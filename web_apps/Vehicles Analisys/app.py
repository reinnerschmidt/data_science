import streamlit as st
import pandas as pd 
import plotly.express as px 

car_data = pd.read_csv('vehicles_raw.csv') # lendo os dados
st.header('Data Vehicles') #Título
check_data = st.checkbox('See Vehicle Data?')
if check_data:
    st.dataframe(car_data)
# criar as caixas de seleção
check_hist = st.checkbox('Criar um histograma')
check_disp = st.checkbox('Criar um gráfico de dispersão')


     
if check_hist:
     # se o check_hist for selecionado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
    # criar um histograma
    fig = px.histogram(car_data, x="odometer", title='Odometer distribution')
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if check_disp:
    # se o check_disp for selecionado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
         
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y='price', title="Price x odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

options = ['Select Year...','1900-1990', '90s','2000s','2010s']
st.header('Year distribution')
op_md_year = st.selectbox('Model Year', options )

#criar filtros baseado no ano de fabircação
def filter_year (dataframe,op_select):
    if op_select == '1900-1990':
        filtered_data = dataframe[(dataframe['model_year'] >= 1900) & (dataframe['model_year'] < 1990 )]
        return filtered_data
    
    elif op_select  == '90s':
        filtered_data = dataframe[(dataframe['model_year'] >= 1990) & (dataframe['model_year'] <2000 )]
        return filtered_data
    elif op_select == '2000s':
        filtered_data = dataframe[(dataframe['model_year'] >= 2000) & (dataframe['model_year'] < 2010 )]
        return filtered_data

    elif op_select == '2010s':
        filtered_data = dataframe[dataframe['model_year'] >= 2010]
        return filtered_data

#plotando baseado nos filtros
if op_md_year !='Select Year...':
    fig = px.histogram(filter_year(car_data,op_md_year), x='model_year')
    st.plotly_chart(fig)
