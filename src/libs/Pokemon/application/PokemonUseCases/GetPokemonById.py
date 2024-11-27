
from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonById:
    def __init__(self, pokemon_repository: IPokemonRepository):
        """
        Initializes a GetPokemonById instance.

        Parameters:
        pokemon_repository (IPokemonRepository): The PokemonRepository instance to be used to get the Pokemon by id.
        """
        self.__pokemon_repository = pokemon_repository

    def run(self, id: int) -> PokemonEntity:
        """
        Retrieves a PokemonEntity instance with the given id from the repository.

        Parameters:
        id (int): The unique identifier for the Pokemon.

        Returns:
        PokemonEntity: The PokemonEntity instance with the given id if it exists,
        otherwise raises a PokemonNotFoundError.

        Raises:
        PokemonNotFoundError: If the Pokemon with the given id does not exist in the repository.
        """
        return self.__pokemon_repository.get_pokemon_by_id(id)
