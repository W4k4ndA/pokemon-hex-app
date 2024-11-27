from tkinter import *
from tkinter import messagebox
from ..domain.Errors.PokemonNotFoundError import PokemonNotFoundError
from ..domain.Entities.PokemonEntity import PokemonEntity
from ...Shared.Infrastructure.ServiceContainer import ServiceContainer


"""
The TKinterPokemonController class is a controller that interacts with a Pokémon service to retrieve Pokémon data.

Methods:

get_pokemon_by_name(name: str): Retrieves a Pokémon by its name, returning the Pokémon entity if found, or displaying an error message if not found.
get_pokemon_by_id(id: int): Retrieves a Pokémon by its ID, returning the Pokémon entity if found, or displaying an error message if not found.
filter_pokemon_by_type(type: str): Retrieves a list of Pokémon that match a specific type.
get_all_pokemons(): Retrieves a list of all Pokémon.
Note that all methods rely on the ServiceContainer.pokemon service to perform the actual data retrieval.
"""


class TKinterPokemonController:

    def get_pokemon_by_name(self, name: str) -> PokemonEntity | None:
        """
        Retrieves a Pokémon by its name, returning the Pokémon entity if found, or displaying an error message if not found.

        Parameters:
        name (str): The name of the Pokémon to be retrieved.

        Returns:
        PokemonEntity | None: The Pokémon entity with the specified name if it exists, otherwise None.
        """
        try:
            pokemon = ServiceContainer.pokemon.get_by_name.run(name)
        except PokemonNotFoundError as error:
            messagebox.showerror(
                error, "There is no pokemon with name %s" % (name.upper()))

        return pokemon

    def get_pokemon_by_id(self, id: int) -> PokemonEntity | None:
        """
        Retrieves a Pokémon by its ID, returning the Pokémon entity if found, or displaying an error message if not found.

        Parameters:
        id (int): The ID of the Pokémon to be retrieved.

        Returns:
        PokemonEntity | None: The Pokémon entity with the specified ID if it exists, otherwise None.
        """
        try:
            pokemon = ServiceContainer.pokemon.get_by_id.run(id)
        except PokemonNotFoundError as error:
            messagebox.showerror(
                str(error), "There is no pokemon with id %s" % (id))
        return pokemon

    def filter_pokemon_by_type(self, type: str) -> list[PokemonEntity]:
        """
        Retrieves a list of Pokémon that match a specific type.

        Parameters:
        type (str): The type category of the Pokémon to be retrieved.

        Returns:
        list[PokemonEntity]: A list of PokémonEntity instances with the specified type if any exist, otherwise an empty list.
        """
        pokemons = ServiceContainer.pokemon.filter_by_type.run(type)
        return pokemons

    def get_all_pokemons(self) -> list[PokemonEntity]:
        """
        Retrieves a list of all Pokémon.

        Returns:
        list[PokemonEntity]: A list of all PokémonEntity instances available in the repository.
        """
        pokemons = ServiceContainer.pokemon.get_all.run()
        return pokemons
