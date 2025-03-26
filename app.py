
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv("dados.csv", sep=';')

# Corrigir nomes de colunas para facilitar uso no código
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Título e logo
st.image("logo-clara.png", width=180)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Filtro por campanha
campanhas = df["nome_da_campanha"].unique()
campanha_escolhida = st.selectbox("Selecione a campanha", campanhas)
filtro = df[df["nome_da_campanha"] == campanha_escolhida]

# Métricas principais
col1, col2 = st.columns(2)
col1.metric("Gasto", f"R$ {filtro['valor_usado_(brl)'].values[0]:,.2f}")
col2.metric("Resultados", filtro["resultados"].values[0])

# Gráficos
fig1 = px.bar(df, x="nome_da_campanha", y="valor_usado_(brl)", title="Gasto por Campanha")
fig2 = px.bar(df, x="nome_da_campanha", y="resultados", title="Resultados por Campanha")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
