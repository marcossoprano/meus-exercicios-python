import sqlite3

# Conectar ao banco (ou criar um novo se não existir)
conn = sqlite3.connect("meubanco.db")  
cursor = conn.cursor()

# Criar uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Salvar as mudanças e fechar
conn.commit()
conn.close()
