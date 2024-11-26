from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonAll:
    def __init__(self, pokemon_repository: IPokemonRepository):
        self.__pokemon_repository = pokemon_repository  

    def run(self) -> list[PokemonEntity]:
        return self.__pokemon_repository.get_all_pokemons()