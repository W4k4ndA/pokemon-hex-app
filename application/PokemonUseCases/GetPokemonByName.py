from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonByName:
    def __init__(self, pokemon_repository: IPokemonRepository):
        self.__pokemon_repository = pokemon_repository

    def run(self, name: str) -> PokemonEntity:
        return self.__pokemon_repository.get_pokemon_by_name(name)