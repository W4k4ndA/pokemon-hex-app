from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class FilterPokemonByType:
    def __init__(self, pokemon_repository: IPokemonRepository):
        """
        Initializes a FilterPokemonByType instance.

        Parameters:
        pokemon_repository (IPokemonRepository): The PokemonRepository instance to be used to filter the Pokemon by type.
        """
        self.__pokemon_repository = pokemon_repository

    def run(self, type: str) -> list[PokemonEntity]:
        """
        Retrieves a list of PokemonEntity instances with the specified type from the repository.

        Parameters:
        type (str): The type category of the Pokemon to be retrieved.

        Returns:
        list[PokemonEntity]: A list of PokemonEntity instances with the specified type if any exist, otherwise an empty list.
        """
        return self.__pokemon_repository.filter_pokemon_by_type(type)
