from ...Pokemon.infrastructure.APIPokemonRepository import APIPokemonRepository
from ...Pokemon.application.PokemonUseCases.GetPokemonAll import GetPokemonAll
from ...Pokemon.application.PokemonUseCases.GetPokemonById import GetPokemonById
from ...Pokemon.application.PokemonUseCases.GetPokemonByName import GetPokemonByName
from ...Pokemon.application.PokemonUseCases.FilterPokemonByType import FilterPokemonByType

from types import SimpleNamespace

"""
This module defines a Service Container for the Pokémon application. It acts as a centralized registry for the application's services and use cases, which can be accessed throughout the application. 

The ServiceContainer uses an instance of APIPokemonRepository to interact with an external API to retrieve Pokémon data. It provides the following services:

- get_all: Retrieves a list of all Pokémon.
- get_by_id: Retrieves a Pokémon by its unique ID.
- get_by_name: Retrieves a Pokémon by its name.
- filter_by_type: Retrieves a list of Pokémon that match a specific type.

These services are implemented using corresponding use case classes (GetPokemonAll, GetPokemonById, GetPokemonByName, FilterPokemonByType) that encapsulate the application's business logic. 

The ServiceContainer is designed to be consumed by other parts of the application, such as controllers or GUI components, allowing them to access and use these services without needing to know the underlying implementation details.
If the application requires additional services or use cases in the future, they can be added to the ServiceContainer without modifying the existing code.
Adicionaly if the repository changes, it will not affect the ServiceContainer. Just change the APIPokemonRepository to the new one
"""

pokemon_repository = APIPokemonRepository()


ServiceContainer = SimpleNamespace(
    pokemon=SimpleNamespace(
        get_all=GetPokemonAll(pokemon_repository),
        get_by_id=GetPokemonById(pokemon_repository),
        get_by_name=GetPokemonByName(pokemon_repository),
        filter_by_type=FilterPokemonByType(pokemon_repository)
    )
)
