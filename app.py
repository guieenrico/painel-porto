
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Logo
st.image("logo-clara.png", width=150)

# Título
st.title("Gestão de Tráfego")
st.header("Painel de Resultados - Porto de Areia Santa Eliza")

# Carregar dados
df = pd.read_csv("dados.csv", encoding="utf-8")
df.columns = df.columns.str.strip()  # Remover espaços extras
df.rename(columns={df.columns[0]: "Início dos Relatórios"}, inplace=True)  # Segurança

# Converter datas
df["Início dos Relatórios"] = pd.to_datetime(df["Início dos Relatórios"], errors="coerce")
df["Término dos Relatórios"] = pd.to_datetime(df["Término dos Relatórios"], errors="coerce")

# Filtros de data
data_inicial = st.date_input("Data inicial", df["Início dos Relatórios"].min().date())
data_final = st.date_input("Data final", df["Término dos Relatórios"].max().date())

filtro_data = df[(df["Início dos Relatórios"].dt.date >= data_inicial) & (df["Término dos Relatórios"].dt.date <= data_final)]

# Seleção de campanha
campanhas = filtro_data["Nome da campanha"].dropna().unique()
campanha_escolhida = st.selectbox("Selecione a campanha", campanhas)

filtro = filtro_data[filtro_data["Nome da campanha"] == campanha_escolhida]

# Garantir valores numéricos
filtro["Custo por resultados"] = pd.to_numeric(filtro["Custo por resultados"], errors="coerce")
filtro["Valor usado (BRL)"] = pd.to_numeric(filtro["Valor usado (BRL)"], errors="coerce")
filtro["Resultado"] = pd.to_numeric(filtro["Resultado"], errors="coerce")

# Exibir métricas
col1, col2, col3 = st.columns(3)
col1.metric("Alcance", f"{int(filtro['Alcance'].sum()):,}".replace(",", "."))
col2.metric("Valor investido", f"R$ {filtro['Valor usado (BRL)'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col3.metric("Custo por Lead", f"R$ {float(filtro['Custo por resultados'].mean()):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Gráfico simples de resultados
st.subheader("Resultados por Campanha")
fig, ax = plt.subplots()
filtro_data.groupby("Nome da campanha")["Resultado"].sum().plot(kind="barh", ax=ax)
st.pyplot(fig)
