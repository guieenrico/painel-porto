import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Título e Logo
st.image("logo-clara.png", width=150)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("## Painel de Resultados - Porto de Areia Santa Eliza")

# Filtro por campanha
campanhas = df["nome_campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)
filtro = df[df["nome_campanha"] == campanha_selecionada]

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro['gasto'].values[0]:,.2f}")
col2.metric("Cliques no WhatsApp", f"{filtro['cliques_wpp'].values[0]}")
col3.metric("Leads (conversas)", f"{filtro['leads'].values[0]}")

# Gráficos
st.markdown("### Gasto por Campanha")
fig = px.bar(df, x="nome_campanha", y="gasto", title="Gasto por Campanha")
st.plotly_chart(fig, use_container_width=True)

# Tabela
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
