
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Sidebar para selecionar a campanha
campanhas = df["campanha"].unique()
campanha_selecionada = st.sidebar.selectbox("Selecione a campanha", campanhas)

# Filtrar os dados com base na campanha selecionada
filtro = df[df["campanha"] == campanha_selecionada]

# Calcular métricas
gasto_total = filtro["gasto"].values[0]
alcance_total = filtro["alcance"].values[0]
impressoes = filtro["impressoes"].values[0]
cliques = filtro["cliques"].values[0]
conversoes = filtro["cliques_wpp"].values[0]

# Layout principal
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro['gasto'].values[0]:,.2f}")
col2.metric("Alcance", f"{int(alcance_total):,}")
col3.metric("Impressoes", f"{int(impressoes):,}")

col4, col5 = st.columns(2)
col4.metric("Cliques", f"{int(cliques):,}")
col5.metric("Conversões (Leads)", f"{int(conversoes):,}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
