
import streamlit as st
import pandas as pd

# Carrega os dados
df = pd.read_csv("dados.csv", sep=";")

# Título e logo
st.image("logo-clara.png", width=150)
st.markdown("<h2 style='text-align: center;'>Gestão de Tráfego</h2>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Seletor de campanha
campanhas = df["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Filtrar os dados pela campanha selecionada
filtro = df[df["Nome da campanha"] == campanha_selecionada]

# Extração de dados
gasto = filtro["Valor usado (BRL)"].values[0]
resultados = filtro["Resultados"].values[0]
custo_por_resultado = filtro["Custo por resultados"].values[0]

# Exibir métricas
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultados}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
