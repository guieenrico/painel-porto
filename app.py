
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Converter colunas de data
df["Inicio dos Relatorios"] = pd.to_datetime(df["Inicio dos Relatorios"], dayfirst=True)
df["Termino dos Relatorios"] = pd.to_datetime(df["Termino dos Relatorios"], dayfirst=True)

# Filtro por data
data_inicio = st.date_input("Data inicial", df["Inicio dos Relatorios"].min())
data_fim = st.date_input("Data final", df["Termino dos Relatorios"].max())

# Filtrar o DataFrame
df_filtrado = df[
    (df["Inicio dos Relatorios"] >= pd.to_datetime(data_inicio)) &
    (df["Termino dos Relatorios"] <= pd.to_datetime(data_fim))
]

# Título e logo
st.image("logo-clara.png", width=150)
st.markdown("<h2 style='text-align: center;'>Gestão de Tráfego</h2>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Seleção de campanha
campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Filtrar por campanha selecionada
filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Calcular métricas
gasto = filtro["Valor usado (BRL)"].values[0]
resultado = filtro["Resultado"].values[0]
custo_resultado = filtro["Custo por resultados"].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{resultado}")
col3.metric("Custo por Lead", f"R$ {custo_resultado:,.2f}")

# Gráficos gerais com base no filtro de data
st.markdown("### 📊 Gráficos Gerais")

fig1 = px.bar(df_filtrado, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto por Campanha")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(df_filtrado, x="Nome da campanha", y="Resultado", title="Resultados por Campanha")
st.plotly_chart(fig2, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional</div>", unsafe_allow_html=True)
