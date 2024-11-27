from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonByName:
    def __init__(self, pokemon_repository: IPokemonRepository):
        """
        Initializes a GetPokemonByName instance.

        Parameters:
        pokemon_repository (IPokemonRepository): The PokemonRepository instance to be used to retrieve a Pokemon by name.
        """

        self.__pokemon_repository = pokemon_repository

    def run(self, name: str) -> PokemonEntity:
        """
        Retrieves a PokemonEntity instance by its name from the repository.

        Parameters:
        name (str): The name of the Pokemon to be retrieved.

        Returns:
        PokemonEntity: The PokemonEntity instance with the specified name.
        """
        return self.__pokemon_repository.get_pokemon_by_name(name)
