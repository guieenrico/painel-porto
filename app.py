
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.image("logo-clara.png", width=150)
st.title("Gestão de Tráfego")
st.header("Painel de Resultados - Porto de Areia Santa Eliza")

# Leitura e tratamento dos dados
df = pd.read_csv("dados.csv")
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"])
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"])

# Filtros por data
data_inicial = pd.to_datetime(st.text_input("Data inicial", "2024/08/12"))
data_final = pd.to_datetime(st.text_input("Data final", "2025/03/26"))
df = df[(df["Início dos Relatórios"] >= data_inicial) & (df["Término dos Relatórios"] <= data_final)]

# Filtro por campanha
campanhas = df["Nome da campanha"].unique()
campanha_escolhida = st.selectbox("Selecione a campanha", campanhas)
filtro = df[df["Nome da campanha"] == campanha_escolhida]

# Extração de valores
gasto = filtro["Valor usado (BRL)"].values[0]
leads = filtro["Resultados"].values[0]
custo_por_resultado = filtro["Custo por resultados"].values[0]

# Tratamento para valores com separador de milhar
gasto = float(str(gasto).replace(".", "").replace(",", "."))
leads = float(str(leads).replace(".", "").replace(",", "."))
custo_por_resultado = float(str(custo_por_resultado).replace(".", "").replace(",", "."))

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.0f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráfico de barras
st.subheader("Comparativo de Campanhas")
fig, ax = plt.subplots()
df_plot = df.copy()
df_plot["Gasto"] = df_plot["Valor usado (BRL)"].astype(str).str.replace(".", "").str.replace(",", ".").astype(float)
ax.barh(df_plot["Nome da campanha"], df_plot["Gasto"])
st.pyplot(fig)
