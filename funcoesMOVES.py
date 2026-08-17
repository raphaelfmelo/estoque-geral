from funcoesCRUD import inicializar


#Função para registrar a entrada de um produto; Inserindo produto e atualizando o estoque
def registrar_entrada(id_produto, quantidade):
    conexao, cursor = inicializar()

    try:
        if (quantidade <= 0):
            return

        cursor.execute("""
            UPDATE produtos
            SET estoque = estoque + ?
            WHERE id = ?
        """, (quantidade, id_produto))

        if cursor.rowcount == 0:
            return

        cursor.execute("""
            INSERT INTO movimentacoes (produto_id, tipo, quantidade)
            VALUES (?, ?, ?)
        """, (id_produto, 'entrada', quantidade))

        conexao.commit()

    finally:
        conexao.close()



#Função para registrar a saída de um produto identificando o produto, estoque e analisando se é possível antes de atualizar
def registrar_saida(id_produto, quantidade):
    conexao, cursor = inicializar()

    try:
        if (quantidade <= 0):
            return

        cursor.execute("""
            SELECT estoque
            FROM produtos
            WHERE id = ?
        """, (id_produto,))

        resultado = cursor.fetchone()

        if resultado is None:
            print('Erro: Produto não encontrado.')
            return

        estoque_atual = resultado[0] #posição 0 pois está puxando apenas 1 item da tabela

        if estoque_atual < quantidade:
            return

        cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - ?
            WHERE id = ?
        """, (quantidade, id_produto))

        cursor.execute("""
                INSERT INTO movimentacoes (produto_id, tipo, quantidade)
                VALUES (?, ?, ?)
            """, (id_produto, 'saida', quantidade))

        conexao.commit()

    finally:
        conexao.close()


# Função para listar movimentações nomeando produtos
def listar_movimentacoes():
    conexao, cursor = inicializar()

    cursor.execute("""
        SELECT produtos.nome, movimentacoes.tipo, movimentacoes.quantidade, movimentacoes.data
        FROM movimentacoes
        JOIN produtos
        ON movimentacoes.produto_id = produtos.id
    """,)

    movimentacoes = cursor.fetchall()
    conexao.close()
    return movimentacoes