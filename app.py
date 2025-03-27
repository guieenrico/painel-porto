
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Carregar os dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas removendo espaços extras e padronizando
df.columns = df.columns.str.strip()

# Converter datas
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], errors="coerce")
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], errors="coerce")

# Filtros de data
data_inicial = st.date_input("Data inicial", value=pd.to_datetime("2024-08-12"))
data_final = st.date_input("Data final", value=pd.to_datetime("2025-03-26"))

df_filtrado = df[(df["Início dos Relatórios"] >= pd.to_datetime(data_inicial)) & 
                 (df["Término dos Relatórios"] <= pd.to_datetime(data_final))]

# Filtro de campanha
campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Tratar valores numéricos com erro
def to_float(val):
    try:
        return float(str(val).replace('.', '').replace(',', '.'))
    except:
        return 0.0

gasto = to_float(filtro["Valor usado (BRL)"].values[0])
leads = to_float(filtro["Resultado"].values[0])
custo_por_resultado = to_float(filtro["Custo por resultados"].values[0])

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.0f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráfico de barras
st.subheader("Gráfico de Alcance vs Impressões")
fig, ax = plt.subplots()
ax.bar(["Alcance", "Impressões"], [to_float(filtro["Alcance"].values[0]), to_float(filtro["Impressoes"].values[0])])
st.pyplot(fig)
