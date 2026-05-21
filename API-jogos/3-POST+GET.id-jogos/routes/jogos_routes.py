from flask import Blueprint, request
from controllers.jogos_controllers import get_jogos, create_jogos, update_jogos, get_jogos_by_id

# Define um Blueprint para as rotas de "Carro"
get_jogos_routes = Blueprint('jogos_routes', __name__)  # blueprint e todo o crud feito

# Rota para listar todos os carros (GET)
@get_jogos_routes.route('/jogos', methods=['GET'])
def jogos_get():
    return get_jogos()

# Rota para buscar um carro pelo ID (GET)
@jogos.route('/jogos/<int:jogos_id>', methods=['GET']) # type: ignore
def jogos_get_by_id(jogos_id):
    return get_jogos_by_id(jogos_id)

# Rota para criar um novo carro (POST)
@jogos_routes.route('/jogos', methods=['POST']) # type: ignore
def jogos_post():
    return create_jogos(request.json)  # request usado para acessar as informacoes enviadas em formato json

# Rota para atualizar um carro pelo ID (PUT)
@jogos_routes.route('/jogos/<int:jogos_id>', methods=['PUT'])
def jogos_put(jogos_id):
    return update_jogos(jogos_id, request.json)