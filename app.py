
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurações da página
st.set_page_config(page_title="Painel de Resultados", layout="wide")

# Carregar dados
df = pd.read_csv("dados.csv")

# Corrigir nomes de colunas
df.columns = df.columns.str.strip()

# Garantir que datas estejam no formato datetime
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], errors="coerce")
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], errors="coerce")

# Filtros por data
data_inicial = st.date_input("Data inicial", value=df["Início dos Relatórios"].min().date())
data_final = st.date_input("Data final", value=df["Término dos Relatórios"].max().date())

# Filtro por período
df_filtrado = df[(df["Início dos Relatórios"] >= pd.to_datetime(data_inicial)) & 
                 (df["Término dos Relatórios"] <= pd.to_datetime(data_final))]

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Selecionar campanha
campanhas = df_filtrado["Nome da campanha"].dropna().unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Filtrar dados por campanha
filtro = df_filtrado[df_filtrado["Nome da campanha"] == campanha_selecionada]

# Converter colunas numéricas
filtro["Valor usado (BRL)"] = pd.to_numeric(filtro["Valor usado (BRL)"], errors="coerce")
filtro["Custo por resultados"] = pd.to_numeric(filtro["Custo por resultados"], errors="coerce")
filtro["Resultados"] = pd.to_numeric(filtro["Resultados"], errors="coerce")

# Calcular custo por resultado
try:
    custo_por_resultado = filtro["Custo por resultados"].values[0]
except:
    custo_por_resultado = 0

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {filtro['Valor usado (BRL)'].values[0]:,.2f}")
col2.metric("Leads", f"{filtro['Resultados'].values[0]:,.0f}")
col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")

# Gráfico simples (exemplo)
st.markdown("### Gráfico de Impressões vs Alcance")
filtro["Impressões"] = pd.to_numeric(filtro["Impressoes"], errors="coerce")
filtro["Alcance"] = pd.to_numeric(filtro["Alcance"], errors="coerce")

fig, ax = plt.subplots()
ax.bar(["Impressões", "Alcance"], [filtro["Impressões"].values[0], filtro["Alcance"].values[0]])
st.pyplot(fig)
