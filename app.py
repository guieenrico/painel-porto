
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas com espaços extras
df.columns = df.columns.str.strip()

# Converter coluna de datas
df["Inicio dos Relatorios"] = pd.to_datetime(df["Inicio dos Relatorios"], dayfirst=True)
df["Termino dos Relatorios"] = pd.to_datetime(df["Termino dos Relatorios"], dayfirst=True)

# Filtros de data
data_inicial = st.text_input("Data inicial", "2024/08/12")
data_final = st.text_input("Data final", "2025/03/26")
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)
df_filtrado = df[(df["Inicio dos Relatorios"] >= data_inicial) & (df["Termino dos Relatorios"] <= data_final)]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Seleção de campanha
campanhas = df_filtrado["Nome da campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)
filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Resultados
gasto = filtro["Valor usado (BRL)"].values[0]
resultado = filtro["Resultado"].values[0]
custo_por_resultado = filtro["Custo por resultados"].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado:,.1f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Gráfico de barras por campanha
st.markdown("### Gráficos por Campanha")
grafico_gasto = px.bar(df_filtrado, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto por Campanha")
grafico_resultado = px.bar(df_filtrado, x="Nome da campanha", y="Resultado", title="Resultados por Campanha")
st.plotly_chart(grafico_gasto, use_container_width=True)
st.plotly_chart(grafico_resultado, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
