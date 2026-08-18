import streamlit as st
import pandas as pd

from funcoesCRUD import listar_produtos, listar_produtos_inativos, cadastrar_produto, atualizar_produto, desativar_produto, reativar_produto

produtos = listar_produtos()
produtos_inativos = listar_produtos_inativos()

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


#Cadastro de Produto
st.header("Cadastro de Produto")

with st.expander('Cadastrar Produto'):
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



#Edição de Produto
st.header("Edição de Produto")

with st.expander('Editar Produto'):

    opcoes_produtos = {
        f'(ID {produto[0]}) — {produto[1]}': produto[0]
        for produto in produtos
    }

    produto_selecionado = st.selectbox('Produto', options=opcoes_produtos.keys())

    id_produto = opcoes_produtos[produto_selecionado]

    produto_atual = next(
        produto for produto in produtos
        if produto[0] == id_produto
    )

    nome = st.text_input('Nome', value= produto_atual[1])

    categoria = st.text_input('Categoria', value= produto_atual[2])

    preco = st.number_input('Preço', min_value=0.0, value= float(produto_atual[3]), step=0.01)

    estoque = st.number_input('Estoque', min_value=0, value= int(produto_atual[4]), step=1)

    estoque_minimo = st.number_input('Estoque Mínimo', min_value=0, value= int(produto_atual[5]), step=1)

    if st.button('Atualizar Produto'):
        atualizar_produto(id_produto, nome, categoria, preco, estoque, estoque_minimo)
        st.rerun()


#Desativação de Produto
st.header('Remoção de Produto')

with st.expander('Desativar Produto'):
    opcoes_produtos = {
        f'(ID {produto[0]}) — {produto[1]}': produto[0]
        for produto in produtos
    }

    produto_selecionado = st.selectbox('Produto para desativar', options= opcoes_produtos.keys(), key='desativar_prod')

    id_produto = opcoes_produtos[produto_selecionado]

    confirmar = st.checkbox('Tenho certeza que quero desativar esse produto')

    if confirmar:
        if st.button('Confirmar desativação'):
            resultado = desativar_produto(id_produto)
            st.rerun()



st.header('Recuperar Produto')

with st.expander('Reativar Produto'):
    opcoes_inativos = {
        f'(ID {produto[0]}) — {produto[1]}': produto[0]
        for produto in produtos_inativos
    }

    produto_selecionado = st.selectbox('Produto para reativar', options=opcoes_inativos.keys(), key='reativar_prod')

    id_produto = opcoes_inativos[produto_selecionado]

    confirmar = st.checkbox('Tenho certeza que quero reativar esse produto')

    if confirmar:
        if st.button('Confirmar Reativação'):
            resultado = reativar_produto(id_produto)
            st.rerun()
