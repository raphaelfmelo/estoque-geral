import streamlit as st
import pandas as pd

from funcoesCRUD import listar_produtos, listar_produtos_estoque_baixo
from funcoesMOVES import listar_movimentacoes

st.set_page_config(
    page_title='Estoque Geral',
    page_icon= '📦',
    layout= 'wide'
)

st.title('📦 Estoque Geral')

st.subheader('Sistema de gerenciamento de estoque')

st.write(
    '''
    Bem-Vindo ao Estoque Geral!
    
    Utilize o menu lateral para gerenciar produtos, 
    registrar movimentações e consultar o histórico.    
    ''')

st.divider()

produtos = listar_produtos()
produtos_baixo_estoque = listar_produtos_estoque_baixo()
movimentacoes = listar_movimentacoes()

quantidade_produtos = len(produtos)
quantidade_baixo_estoque = len(produtos_baixo_estoque)
quantidade_movimentacoes = len(movimentacoes)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Produtos ativos', quantidade_produtos)

with col2:
    st.metric('Estoque Baixo', quantidade_baixo_estoque)

with col3:
    st.metric('Movimentações', quantidade_movimentacoes)

st.header('⚠️ Produtos com baixo estoque')

if produtos_baixo_estoque:
    df = pd.DataFrame(
        produtos_baixo_estoque,
        columns= [
            'ID do Produto',
            'Nome',
            'Categoria',
            'Preço',
            'Estoque',
            'Estoque Mínimo'
        ]
    )
    st.dataframe(df, hide_index=True)

else:
    st.success('Nenhum produto está com estoque baixo.')
