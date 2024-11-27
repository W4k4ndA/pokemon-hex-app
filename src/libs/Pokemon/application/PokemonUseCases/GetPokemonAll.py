from ...domain.Entities.PokemonEntity import PokemonEntity
from ...domain.Interfaces.IPokemonRepository import IPokemonRepository


class GetPokemonAll:
    def __init__(self, pokemon_repository: IPokemonRepository):
        """
        Initializes a GetPokemonAll instance.

        Parameters:
        pokemon_repository (IPokemonRepository): The PokemonRepository instance to be used to retrieve all Pokemon.
        """
        self.__pokemon_repository = pokemon_repository

    def run(self) -> list[PokemonEntity]:
        """
        Retrieves a list of all PokemonEntity instances from the repository.

        Returns:
        list[PokemonEntity]: A list of all PokemonEntity instances in the repository.
        """
        return self.__pokemon_repository.get_all_pokemons()
