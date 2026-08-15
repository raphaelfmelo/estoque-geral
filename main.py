from funcoesCRUD import listar_produtos, cadastrar_produto, atualizar_produto, excluir_produto

produtos = listar_produtos()
for produto in produtos: print(produto)



#Teste da Função Cadastrar
'''
cadastrar_produto(
    'Webcam X',
    'Periféricos',
    'Câmeras',
    159.90,
    10,
    3
)
'''

#Teste da Função Atualizar
'''
atualizar_produto(
    1,
    "Logitech G403 Pro",
    "Periférico",
    "Mouse",
    219.90,
    20,
    5
)
'''

#Teste da Função Excluir
'''
excluir_produto(5)
print()

produtos = listar_produtos()
for produto in produtos: print(produto)
'''