from funcoesCRUD import inicializar

def registrar_entrada(id_produto, quantidade):
    conexao, cursor = inicializar()

    cursor.execute("""
        UPDATE produtos
        SET estoque = estoque + ?
        WHERE id = ?
    """, (quantidade, id_produto))

    conexao.commit()
    conexao.close()

def registrar_saida(id_produto, quantidade):
    conexao, cursor = inicializar()

    cursor.execute("""
        SELECT estoque
        FROM produtos
        WHERE id = ?
    """, (id_produto,))

    resultado = cursor.fetchone()

    estoque_atual = resultado[0] #posição 0 pois está puxando apenas 1 item da tabela