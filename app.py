
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas com espaços e acentos
df.columns = df.columns.str.strip()

# Converter datas
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], dayfirst=True)
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], dayfirst=True)

# Filtros de data
data_inicial = st.date_input("Data inicial", df["Início dos Relatórios"].min().date())
data_final = st.date_input("Data final", df["Término dos Relatórios"].max().date())

filtro_data = df[
    (df["Início dos Relatórios"] >= pd.to_datetime(data_inicial)) &
    (df["Término dos Relatórios"] <= pd.to_datetime(data_final))
]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("## Painel de Resultados - Porto de Areia Santa Eliza")

# Filtro por campanha
campanhas = filtro_data["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)
filtro = filtro_data[filtro_data["Nome da campanha"] == campanha_selecionada]

# Tratamento para cálculo
gasto = float(filtro["Valor usado (BRL)"].values[0]) if not filtro.empty else 0
leads = float(filtro["Resultado"].values[0]) if not filtro.empty else 0
custo_por_resultado = gasto / leads if leads > 0 else 0

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.0f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráficos adicionais
fig = px.bar(filtro_data, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto por Campanha")
st.plotly_chart(fig, use_container_width=True)
