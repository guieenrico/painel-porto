
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv")
df.columns = df.columns.str.strip()

# Corrigir formatos de datas e valores
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], errors='coerce')
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], errors='coerce')
df["Valor usado (BRL)"] = pd.to_numeric(df["Valor usado (BRL)"], errors="coerce")
df["Custo por resultados"] = pd.to_numeric(df["Custo por resultados"], errors="coerce")
df["Resultado"] = pd.to_numeric(df["Resultado"], errors="coerce")

# Filtros
data_inicial = st.text_input("Data inicial", value=str(df["Início dos Relatórios"].min().date()))
data_final = st.text_input("Data final", value=str(df["Término dos Relatórios"].max().date()))

# Logo
st.image("logo-clara.png", width=150)

st.title("Gestão de Tráfego")
st.header("Painel de Resultados - Porto de Areia Santa Eliza")

campanhas = df["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Aplicar filtros
filtro = df[(df["Nome da campanha"] == campanha_selecionada)]
filtro = filtro[
    (df["Início dos Relatórios"] >= pd.to_datetime(data_inicial)) &
    (df["Término dos Relatórios"] <= pd.to_datetime(data_final))
]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro['Valor usado (BRL)'].sum():,.2f}")
col2.metric("Leads", f"{filtro['Resultado'].sum():,.0f}")

try:
    custo_por_resultado = filtro["Custo por resultados"].mean()
    col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")
except:
    col3.metric("Custo por Lead", "N/A")

# Gráfico de barras com matplotlib
fig, ax = plt.subplots()
filtro.groupby("Nome da campanha")["Valor usado (BRL)"].sum().plot(kind="bar", ax=ax)
ax.set_title("Gasto por Campanha")
ax.set_ylabel("Valor em R$")
st.pyplot(fig)
