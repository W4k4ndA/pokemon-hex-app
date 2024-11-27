from abc import ABC, abstractmethod
from ..Entities.PokemonEntity import PokemonEntity


class IPokemonRepository(ABC):
    @abstractmethod
    def get_pokemon_by_id(self, id: int) -> PokemonEntity | None:
        pass

    @abstractmethod
    def get_pokemon_by_name(self, name: str) -> PokemonEntity | None:
        pass

    @abstractmethod
    def filter_pokemon_by_type(self, type: str) -> list[PokemonEntity]:
        pass

    @abstractmethod
    def get_all_pokemons(self) -> list[PokemonEntity]:
        pass
