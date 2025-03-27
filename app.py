
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas com espaços extras ou formatação
df.columns = df.columns.str.strip()

# Converter datas
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], dayfirst=True, errors='coerce')
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], dayfirst=True, errors='coerce')

# Filtros por data
data_inicial = pd.to_datetime(st.text_input("Data inicial", "2024/08/12"))
data_final = pd.to_datetime(st.text_input("Data final", "2025/03/26"))

df_filtrado = df[(df["Início dos Relatórios"] >= data_inicial) & (df["Término dos Relatórios"] <= data_final)]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("# Gestão de Tráfego")
st.markdown("## Painel de Resultados - Porto de Areia Santa Eliza")

# Selecionar campanha
campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_escolhida = st.selectbox("Selecione a campanha", campanhas)

# Filtrar por campanha
filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_escolhida]

# Calcular métricas
gasto = filtro["Valor usado (BRL)"].values[0] if not filtro.empty else 0
leads = filtro["Resultados"].values[0] if not filtro.empty else 0
try:
    custo_por_resultado = float(filtro["Custo por resultados"].values[0]) if not filtro.empty else 0
except:
    custo_por_resultado = 0

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráfico de barras: Gasto por campanha
fig = px.bar(df_filtrado, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto por Campanha")
st.plotly_chart(fig)

# Gráfico de barras: Leads por campanha
fig2 = px.bar(df_filtrado, x="Nome da campanha", y="Resultados", title="Leads por Campanha")
st.plotly_chart(fig2)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
