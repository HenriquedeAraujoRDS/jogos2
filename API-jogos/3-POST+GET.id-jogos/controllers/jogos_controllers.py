from models.jogos_models import jogos  # Importa o modelo Carro
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os carros
def get_jogos():
    jogos = jogos.query.all()  # Busca todos os carros no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogos.json() for jogos in jogos]  # Converte os objetos de carro para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para criar um novo carro
def create_jogos(jogos_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogos_data for key in ['plataforma', 'titulo', 'gênero', 'desenvolvedor']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. , Plataforma, titulo, genero e deselvondedor são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response

    # Se os dados forem válidos, cria o novo carro
    novo_jogos = jogos(
        titulo=jogos_data['titulo'],
        gênero=jogos_data['gênero'],
        desenvolvedor=jogos_data['desenvolvedor'],
        plataforma=jogos_data['plataforma']
    )

    db.session.add(novo_jogos)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'jogos cadastrado com sucesso.',
            'jogos': novo_jogos.json()  # Retorna os dados do carro cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

# Função para atualizar um carro por ID
def update_jogos(jogos_id, jogos_titulo):
    jogos = jogos.query.get(jogos_id)  # Busca o carro pelo ID

    if not jogos:  # Se o carro não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'jogos não encontrado.'}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogos_titulo for key in ['titulo', 'plataforma', 'gênero' 'desenvolvedor']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, gênero , plataforma, desenvolvedor são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

    # Atualiza os dados do carro
    jogos.titulo = jogos_titulo['titulo']
    jogos.gênero = jogos_gênero['gênero'] # type: ignore
    jogos.desenvolvedor = jogos_desenvolvedor['desenvolvedor'] # type: ignore
    jogos.plataforma = jogos_plataforma['plataforma'] # type: ignore

    db.session.commit()  # Confirma a atualização no banco de dados

    # Retorna a resposta com os dados do carro atualizado
    response = make_response(
        json.dumps({
            'mensagem': 'jogos atualizado com sucesso.',
            'jogos': jogos.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response