
import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv("dados.csv")

# Título e logo
st.image("logo-clara.png", width=150)
st.markdown("## Porto de Areia Santa Eliza")
st.markdown("### Painel de Resultados das Campanhas")

# Seleção de campanha
campanha = st.selectbox("Selecione a campanha:", df["campanha"].unique())
filtro = df[df["campanha"] == campanha]

# Exibição de métricas
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro["gasto"].values[0]:,.2f}")
col2.metric("Cliques no WhatsApp", int(filtro["cliques_wpp"].values[0]))
col3.metric("Agendamentos", int(filtro["agendamentos"].values[0]))

col4, col5, col6 = st.columns(3)
col4.metric("Visitas", int(filtro["visitas"].values[0]))
col5.metric("Propostas", int(filtro["propostas"].values[0]))
col6.metric("Vendas", int(filtro["vendas"].values[0]))

col7, col8 = st.columns(2)
col7.metric("Valor de Vendas", f"R$ {filtro["valor_vendas"].values[0]:,.2f}")
col8.metric("ROAS", f"{filtro["roas"].values[0]:,.2f}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
