import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number

st.title("Dashboard de Vendas :shopping_cart:")
st.set_page_config(layout="wide")

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric("Receita Total", format_number(df['total'].sum(), "R$"))
    with coluna2:
        st.metric('Quantidade de Vendas', f"{df['total'].count():,}")