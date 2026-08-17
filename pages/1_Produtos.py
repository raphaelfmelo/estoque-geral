import streamlit as st
import pandas as pd

from funcoesCRUD import listar_produtos, cadastrar_produto

produtos = listar_produtos()

#Tabela de Produtos - Chamada utilizando biblioteca Pandas
df = pd.DataFrame(
    produtos,
    columns= [
        "ID do Produto",
        "Nome",
        "Categoria",
        "Preço",
        "Estoque",
        "Estoque Mínimo"
    ]
)
st.dataframe(df, hide_index= True)


st.header("Cadastrar Produto")

nome = st.text_input('Nome')
categoria = st.text_input('Categoria')
preco = st.number_input('Preço', min_value=0.0, step=0.01)
estoque = st.number_input('Estoque ', min_value=0, step=1)
estoque_minimo = st.number_input('Estoque Mínimo ', min_value=0, step=1)

confirmar = st.button("Cadastrar")

if confirmar:
    if not nome:
        st.error("Informe o nome do produto.")
    elif not categoria:
        st.error("Informe a categoria.")
    elif preco <= 0:
        st.error("O preço deve ser maior que zero.")

    else:
        cadastrar_produto(nome, categoria, preco, estoque, estoque_minimo)
        st.success('Produto Cadastrado!')
        st.rerun()