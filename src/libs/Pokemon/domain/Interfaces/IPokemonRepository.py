""" 
    The IPokemonRepository class is an abstract base class (ABC) that defines an interface for a Pokémon repository. It outlines the methods that must be implemented by any concrete subclass.

Methods:

get_pokemon_by_id(id: int): Returns a PokemonEntity instance with the given ID if it exists in the repository, otherwise returns None.
get_pokemon_by_name(name: str): Returns a PokemonEntity instance with the specified name if it exists in the repository, otherwise returns None.
filter_pokemon_by_type(type: str): Returns a list of PokemonEntity instances with the specified type if any exist, otherwise returns an empty list.
get_all_pokemons(): Returns a list of all PokemonEntity instances in the repository.
Note that these methods are abstract, meaning they must be implemented by any concrete subclass of IPokemonRepository.
"""
from abc import ABC, abstractmethod
from ..Entities.PokemonEntity import PokemonEntity


class IPokemonRepository(ABC):
    @abstractmethod
    def get_pokemon_by_id(self, id: int) -> PokemonEntity | None:
        """
        Returns a PokemonEntity instance with the given id if the Pokemon exists in the
        repository. Otherwise, returns None.

        Parameters:
        id (int): The unique identifier for the Pokemon.

        Returns:
        PokemonEntity | None: The PokemonEntity instance with the given id if it exists,
        otherwise None.
        """
        pass

    @abstractmethod
    def get_pokemon_by_name(self, name: str) -> PokemonEntity | None:
        """
        Retrieves a PokemonEntity instance by its name from the repository.

        Parameters:
        name (str): The name of the Pokemon to be retrieved.

        Returns:
        PokemonEntity | None: The PokemonEntity instance with the specified name if it exists,
        otherwise None.
        """
        pass

    @abstractmethod
    def filter_pokemon_by_type(self, type: str) -> list[PokemonEntity]:
        """
        Retrieves a list of PokemonEntity instances with the specified type from the repository.

        Parameters:
        type (str): The type category of the Pokemon to be retrieved.

        Returns:
        list[PokemonEntity]: A list of PokemonEntity instances with the specified type if any exist,
        otherwise an empty list.
        """
        pass

    @abstractmethod
    def get_all_pokemons(self) -> list[PokemonEntity]:
        """
        Retrieves a list of all PokemonEntity instances from the repository.

        Returns:
        list[PokemonEntity]: A list of all PokemonEntity instances in the repository.
        """
        pass
