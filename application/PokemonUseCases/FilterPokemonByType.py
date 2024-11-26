from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class FilterPokemonByType:
    def __init__(self, pokemon_repository: IPokemonRepository):
        self.__pokemon_repository = pokemon_repository

    def run(self, type: str) -> list[PokemonEntity]:
        return self.__pokemon_repository.filter_pokemon_by_type(type)