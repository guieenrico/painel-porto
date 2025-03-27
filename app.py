
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados
df = pd.read_csv("dados.csv", sep=";", encoding="utf-8")

# Conversão de datas
df["Inicio dos Relatorios"] = pd.to_datetime(df["Inicio dos Relatorios"], dayfirst=True)
df["Termino dos Relatorios"] = pd.to_datetime(df["Termino dos Relatorios"], dayfirst=True)

# Filtros por data
data_inicial = st.date_input("Data inicial", df["Inicio dos Relatorios"].min().date())
data_final = st.date_input("Data final", df["Termino dos Relatorios"].max().date())

filtro = df[
    (df["Inicio dos Relatorios"].dt.date >= data_inicial) &
    (df["Termino dos Relatorios"].dt.date <= data_final)
]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Seleção da campanha
campanhas = filtro["Nome da campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

filtro = filtro[filtro["Nome da campanha"] == campanha_selecionada]

# KPIs
gasto = filtro["Valor usado (BRL)"].values[0]
resultado = filtro["Resultados"].values[0]
custo_por_resultado = filtro["Custo por resultados"].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado:,.1f}")
col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")

# Gráfico de barras: alcance por campanha
st.markdown("### Alcance por Campanha")
fig, ax = plt.subplots()
filtro_plot = df[
    (df["Inicio dos Relatorios"].dt.date >= data_inicial) &
    (df["Termino dos Relatorios"].dt.date <= data_final)
]
agrupado = filtro_plot.groupby("Nome da campanha")["Alcance"].sum()
agrupado.sort_values(ascending=True).plot(kind="barh", ax=ax)
st.pyplot(fig)
