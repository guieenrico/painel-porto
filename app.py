
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Corrige possíveis espaços e acentos nos nomes das colunas
def padronizar_colunas(df):
    df.columns = df.columns.str.strip().str.lower().str.normalize('NFKD')        .str.encode('ascii', errors='ignore').str.decode('utf-8')
    return df

# Carregar os dados
df = pd.read_csv("dados.csv", sep=";")
df = padronizar_colunas(df)

# Converter datas
df["inicio dos relatorios"] = pd.to_datetime(df["inicio dos relatorios"], errors="coerce")
df["termino dos relatorios"] = pd.to_datetime(df["termino dos relatorios"], errors="coerce")

# Filtros por data
data_inicial = st.date_input("Data inicial", value=df["inicio dos relatorios"].min().date())
data_final = st.date_input("Data final", value=df["termino dos relatorios"].max().date())

filtro = df[(df["inicio dos relatorios"].dt.date >= data_inicial) & (df["termino dos relatorios"].dt.date <= data_final)]

# Seleção de campanha
campanhas = filtro["nome da campanha"].dropna().unique()
campanha = st.selectbox("Selecione a campanha", campanhas)

# Métricas da campanha selecionada
filtro = filtro[filtro["nome da campanha"] == campanha]

gasto = filtro["valor usado (brl)"].astype(str).str.replace(",", ".").astype(float).sum()
resultado = filtro["resultado"].astype(str).str.replace(",", ".").astype(float).sum()
custo_por_resultado = gasto / resultado if resultado != 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado:,.0f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráfico
fig, ax = plt.subplots()
filtro.groupby("nome da campanha")["valor usado (brl)"].sum().plot(kind="bar", ax=ax)
st.pyplot(fig)
