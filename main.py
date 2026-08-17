from funcoesCRUD import inicializar, listar_produtos, cadastrar_produto, atualizar_produto, excluir_produto

from funcoesMOVES import registrar_entrada, registrar_saida, listar_movimentacoes

conexao, cursor = inicializar()

'''
produtos = listar_produtos()
for produto in produtos: print(produto)
print()
'''

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

#Teste das Funções Registrar (Entrada e Saída)
registrar_saida (1, 5)
registrar_saida(1, 1000)
registrar_saida(1, -10)
registrar_entrada(1, 0)
#produtos = listar_produtos()
#for produto in produtos: print(produto)
#registrar_entrada(1, 3)
