import streamlit as st
import pandas as pd

from funcoesMOVES import listar_movimentacoes

st.header('Histórico de Movimentações')

movimentacoes = listar_movimentacoes()

df = pd.DataFrame(
    movimentacoes,
    columns= [
        "Produto",
        "Tipo",
        "Quantidade",
        "Data"
    ]
)
st.dataframe(df, hide_index= True)