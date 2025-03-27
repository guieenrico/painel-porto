
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas
df.columns = df.columns.str.strip()

# Converter colunas de data
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], dayfirst=True)
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], dayfirst=True)

# Filtros de data
data_inicio = st.text_input("Data inicial", value=str(df["Início dos Relatórios"].min().date()))
data_fim = st.text_input("Data final", value=str(df["Término dos Relatórios"].max().date()))

df_filtrado = df[(df["Início dos Relatórios"] >= data_inicio) & (df["Término dos Relatórios"] <= data_fim)]

st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_escolhida = st.selectbox("Selecione a campanha", campanhas)
filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_escolhida]

# Pegar valores e tratar se estiverem como texto
gasto = float(filtro["Valor usado (BRL)"].values[0]) if not filtro.empty else 0
resultado = float(filtro["Resultados"].values[0]) if not filtro.empty else 0
custo_por_resultado = float(filtro["Custo por resultados"].values[0]) if not filtro.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado:,.1f}")
col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
