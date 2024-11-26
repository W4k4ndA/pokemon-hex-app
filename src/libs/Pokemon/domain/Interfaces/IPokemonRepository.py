from abc import ABC, abstractmethod
from ..Entities.PokemonEntity import PokemonEntity


class IPokemonRepository(ABC):
    @abstractmethod
    def get_pokemon_by_id(self, id: int) -> PokemonEntity:
        pass

    @abstractmethod
    def get_pokemon_by_name(self, name: str) -> PokemonEntity:
        pass

    @abstractmethod
    def filter_pokemon_by_type(self, type: str) -> list[PokemonEntity]:
        pass

    @abstractmethod
    def get_all_pokemons(self) -> list[PokemonEntity]:
        pass
