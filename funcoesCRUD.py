import sqlite3


# Função para inicialização das variáveis de conexão e manipulação de dados - Python & DB Browser (Banco de Dados)
def inicializar():
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()

    return conexao, cursor


# Função para listar os produtos inseridos na tabela
def listar_produtos():
    conexao, cursor = inicializar()

    cursor.execute(""" SELECT id, nome, categoria, preco, estoque, estoque_minimo
     FROM produtos
     WHERE ativo = 1
     """)

    produtos = cursor.fetchall()
    conexao.close()

    return produtos


# Função para inserir/cadastrar novos produtos na tabela
def cadastrar_produto(nome, categoria, preco, estoque, estoque_minimo):
    conexao, cursor = inicializar()

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, estoque, estoque_minimo)
        VALUES
            (?, ?, ?, ?, ?)  
    """, (nome, categoria, preco, estoque, estoque_minimo))

    conexao.commit()
    conexao.close()


#Função para atualizar informações do produto
def atualizar_produto(id_produto, nome, categoria, preco, estoque, estoque_minimo):
    conexao, cursor = inicializar()

    cursor.execute("""
        UPDATE produtos
        SET
            nome = ?,
            categoria = ?,
            preco = ?,
            estoque = ?,
            estoque_minimo = ?
        WHERE id = ?
    """, (nome, categoria, preco, estoque, estoque_minimo, id_produto))

    conexao.commit()
    conexao.close()


#Função para remover um produto da lista
def desativar_produto(id_produto):
    conexao, cursor = inicializar()

    cursor.execute("""
        UPDATE produtos
        SET ativo = 0
        WHERE id = ?
    """,(id_produto,))

    conexao.commit()
    conexao.close()


#Função para realocar um produto removido da lista para ela novamente
def reativar_produto(id_produto):
    conexao, cursor = inicializar()

    cursor.execute("""
    UPDATE produtos
    SET ativo = 1
    WHERE id = ?
    """, (id_produto,))

    conexao.commit()
    conexao.close()

def listar_produtos_inativos():
    conexao, cursor = inicializar()

    cursor.execute("""
    SELECT id, nome, categoria, preco, estoque, estoque_minimo
    FROM produtos
    WHERE ativo = 0
    """)

    produtos = cursor.fetchall()
    conexao.close()

    return produtos


#Listar produtos com estoque baixo
def listar_produtos_estoque_baixo():
    conexao, cursor = inicializar()

    cursor.execute("""
    SELECT id, nome, categoria, preco, estoque, estoque_minimo
    FROM produtos
    WHERE ativo  = 1
    AND estoque <= estoque_minimo
    """)

    produtos = cursor.fetchall()
    conexao.close()

    return produtos