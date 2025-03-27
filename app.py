
import streamlit as st
import pandas as pd

# Carregar dados
df = pd.read_csv("dados.csv")

# Título e logo
st.image("logo-clara.png", width=150)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Painel de Resultados - Porto de Areia Santa Eliza</h2>", unsafe_allow_html=True)

# Selecionar campanha
campanhas = df["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Filtrar dados
filtro = df[df["Nome da campanha"] == campanha_selecionada]

# Garantir que há dados
if not filtro.empty:
    gasto = filtro["Valor usado (BRL)"].values[0]
    resultado = filtro["Resultados"].values[0]

    try:
        resultado_float = float(resultado)
    except:
        resultado_float = 0

    custo_por_resultado = float(gasto) / resultado_float if resultado_float > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Gasto", f"R$ {gasto:,.2f}")
    col2.metric("Leads", f"{resultado}")
    col3.metric("Custo por Resultado", f"R$ {custo_por_resultado:,.2f}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
