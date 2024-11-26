
from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonById:
    def __init__(self, pokemon_repository: IPokemonRepository):
        self.__pokemon_repository = pokemon_repository

    def run(self, id: int) -> PokemonEntity:
        return self.__pokemon_repository.get_pokemon_by_id(id)