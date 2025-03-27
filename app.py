import streamlit as st
import pandas as pd
import plotly.express as px

# Logo
st.image("logo-clara.png", width=150)

# Título
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas
df.columns = df.columns.str.strip()

# Converter datas
df["Inicio dos Relatorios"] = pd.to_datetime(df["Inicio dos Relatorios"], dayfirst=True)
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], dayfirst=True)

# Filtros de data
data_inicial = pd.to_datetime(st.text_input("Data inicial", value=str(df["Inicio dos Relatorios"].min().date())))
data_final = pd.to_datetime(st.text_input("Data final", value=str(df["Término dos Relatórios"].max().date())))

# Aplicar filtro de data
df_filtrado = df[(df["Inicio dos Relatorios"] >= data_inicial) & (df["Término dos Relatórios"] <= data_final)]

# Filtro por campanha
campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Verificar se filtro está vazio
if not filtro.empty:
    gasto = filtro["Valor usado (BRL)"].values[0]
    leads = filtro["Resultados"].values[0]
    
    # Tentar converter custo por resultado em número
    try:
        custo_por_resultado = float(filtro["Custo por resultados"].values[0])
    except:
        custo_por_resultado = None

    col1, col2, col3 = st.columns(3)
    col1.metric("Gasto", f"R$ {gasto:,.2f}")
    col2.metric("Leads", f"{leads}")
    if custo_por_resultado is not None:
        col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")
    else:
        col3.metric("Custo por Lead", "N/A")

    # Gráfico de barras
    fig = px.bar(filtro, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto da Campanha Selecionada")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Nenhum dado disponível para o filtro selecionado.")
