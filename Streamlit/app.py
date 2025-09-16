import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("📊 Dashboard de Vendas")

# Leitura dos dados
df = pd.read_csv("vendas.csv", parse_dates=["Data"])

# Sidebar com filtros
st.sidebar.header("Filtros")
regiao = st.sidebar.multiselect("Selecione a Região:", options=df["Região"].unique(), default=df["Região"].unique())
produto = st.sidebar.multiselect("Selecione o Produto:", options=df["Produto"].unique(), default=df["Produto"].unique())

# Aplicando filtros
df_filtrado = df[(df["Região"].isin(regiao)) & (df["Produto"].isin(produto))]

# KPIs
total_vendas = df_filtrado["Vendas"].sum()
media_vendas = df_filtrado["Vendas"].mean()
vendas_por_produto = df_filtrado.groupby("Produto")["Vendas"].sum()

# Mostrando KPIs
st.metric("💰 Total de Vendas", f"R$ {total_vendas:,.2f}")
st.metric("📈 Média por Venda", f"R$ {media_vendas:,.2f}")

# Gráfico de linhas
fig_linha = px.line(df_filtrado, x="Data", y="Vendas", color="Produto", title="Vendas ao Longo do Tempo")
st.plotly_chart(fig_linha)

# Gráfico de barras
fig_barra = px.bar(vendas_por_produto, x=vendas_por_produto.index, y="Vendas", title="Vendas por Produto")
st.plotly_chart(fig_barra)

# Gráfico de pizza
fig_pizza = px.pie(df_filtrado, names="Região", values="Vendas", title="Distribuição de Vendas por Região")
st.plotly_chart(fig_pizza)

# Tabela
st.subheader("📋 Dados filtrados")
st.dataframe(df_filtrado)
