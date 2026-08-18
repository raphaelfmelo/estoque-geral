import streamlit as st
import pandas as pd

from funcoesCRUD import listar_produtos

from funcoesMOVES import registrar_entrada, registrar_saida, listar_movimentacoes


#Listagem dos Produtos de forma tabelada na página
produtos = listar_produtos()

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
st.dataframe(df, hide_index=True)


#Configuração de recurso para limitar escolha de usuário a produtos existentes na lista - Entrada e Saída
opcoes_produtos = {
    f"(ID {produto[0]}) — {produto[1]}": produto[0]
    for produto in produtos
}


#Registrar Entrada - Criação
st.header('Registrar Entrada')

with st.expander('Registrar entrada de estoque'):

    produto_selecionado = st.selectbox('Produto', options= opcoes_produtos.keys(), key= 'entrada_prod')

    quantidade = st.number_input('Entrada de Estoque', min_value=1, step=1)

    confirmar = st.button('Registrar Entrada')

    if confirmar:
        id_produto = opcoes_produtos[produto_selecionado]

        registrar_entrada(id_produto, quantidade)
        st.success('Entrada registrada!')
        st.rerun()


#Registrar Saída - Criação
st.header('Registrar Saída')

with st.expander('Registrar saída de estoque'):

    produto_selecionado = st.selectbox('Produto', options= opcoes_produtos.keys(), key='saida_prod')

    quantidade = st.number_input('Saída de Estoque', min_value=1, step=1)

    confirmar = st.button('Registrar Saída')

    if confirmar:
        id_produto = opcoes_produtos[produto_selecionado]

        registrar_saida(id_produto, quantidade)
        st.success('Saída registrada!')
        st.rerun()