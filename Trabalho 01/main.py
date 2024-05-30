'''
    Autor: Iago Magalhães e Iális Calvacante
    Descrição: Dashboard com StreamLit
    Objetivos:
        - Grafico de barras com 10 paises com mais homicidios
        - caixa de seleção para homens, mulheres ou todos
        - Caixa de seleção para anos
        - Grupos de cards para exibir as informações
        - Gráfico geral com previsão usando série temporal
    - unodc_ddds@un.org

'''

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# df = pd.read_excel("data_cts_intentional_homicide.xlsx", index_col=0)

# Ano = df["Year"].unique()
# Sexo = ['Masculino', 'Feminino', 'Todos']

# anos = st.sidebar.selectbox("Ano", sorted(Ano, reverse=True))
# sexos = st.sidebar.selectbox("Sexo", Sexo)

# col1, col2 = st.columns(2)
# col3, col4 = st.columns(2)









df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Previsão de homicídios ARIMA")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Países com mais homicídios",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)


city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Homicídios por região")
col3.plotly_chart(fig_city, use_container_width=True)


fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Homicídios por sexo")
col4.plotly_chart(fig_kind, use_container_width=True)