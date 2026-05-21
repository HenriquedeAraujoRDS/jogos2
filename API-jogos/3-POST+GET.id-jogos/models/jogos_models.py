# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe Carro que representa a tabela 'carros' no banco de dados
class jogos(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogos'  

    # Define as colunas da tabela 'carros'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do carro, chave primária
    titulo = db.Column(db.String(80), nullable=False)  # Coluna para o modelo do carro, não pode ser nulo
    gênero = db.Column(db.String(80), nullable=False)  # Coluna para a marca do carro, não pode ser nulo
    desenvolvedor = db.Column(db.String(80), nullable=False)
    plataforma = db.Column(db.String(80), nullable=False)  # Coluna para o ano do carro, não pode ser nulo

    # Método para retornar os dados do carro como um dicionário
    def json(self):  
        return {
            'id': self.id,  # ID do carro
            'titulo': self.titulo,  # Modelo do carro
            'gênero': self.gênero,  # Marca do carro
            'desenvolvedor': self.desenvolvedor,  # Ano do carro
            'plataforma': self.plataforma
        }
