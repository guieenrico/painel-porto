
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Carregar dados
df = pd.read_csv("dados.csv")

# Converter colunas de data
df["Inicio dos Relatorios"] = pd.to_datetime(df["Inicio dos Relatorios"], dayfirst=True)
df["Termino dos Relatorios"] = pd.to_datetime(df["Termino dos Relatorios"], dayfirst=True)

# Filtros de data
data_inicial = st.text_input("Data inicial", value=str(df["Inicio dos Relatorios"].min().date()))
data_final = st.text_input("Data final", value=str(df["Termino dos Relatorios"].max().date()))

try:
    data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
    data_final = datetime.strptime(data_final, "%Y-%m-%d")
except:
    st.error("Formato de data inválido. Use AAAA-MM-DD.")

df_filtrado = df[(df["Inicio dos Relatorios"] >= data_inicial) & (df["Termino dos Relatorios"] <= data_final)]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Filtro por campanha
campanhas = df_filtrado["Nome da campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Indicadores principais
gasto = filtro["Valor usado (BRL)"].values[0]
resultado = filtro["Resultados"].values[0]
custo_por_resultado = filtro["Custo por resultados"].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado:,.1f}")
col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")

# Gráficos (exemplo simples)
grafico = px.bar(df_filtrado, x="Nome da campanha", y="Valor usado (BRL)", title="Investimento por Campanha")
st.plotly_chart(grafico)

# Tabela final
st.markdown("### 📋 Dados detalhados")
st.dataframe(df_filtrado)
