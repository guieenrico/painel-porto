
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Dropdown para seleção de campanha
campanha_selecionada = st.selectbox("Selecione a campanha", df["campanha"].unique())
filtro = df[df["campanha"] == campanha_selecionada]

# Cálculo das métricas com base na seleção
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro['gasto'].values[0]:,.2f}")
col2.metric("Conversões", int(filtro['cliques_wpp'].values[0]))
col3.metric("Propostas", int(filtro['compras'].values[0]))

st.markdown("### 📊 Campanhas Detalhadas")
st.dataframe(df)

st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
