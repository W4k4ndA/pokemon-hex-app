from ...Pokemon.infrastructure.APIPokemonRepository import APIPokemonRepository
from ...Pokemon.application.PokemonUseCases.GetPokemonAll import GetPokemonAll
from ...Pokemon.application.PokemonUseCases.GetPokemonById import GetPokemonById
from ...Pokemon.application.PokemonUseCases.GetPokemonByName import GetPokemonByName
from ...Pokemon.application.PokemonUseCases.FilterPokemonByType import FilterPokemonByType

from types import SimpleNamespace

pokemon_repository = APIPokemonRepository()


ServiceContainer = SimpleNamespace(
    pokemon = SimpleNamespace(
        get_all = GetPokemonAll(pokemon_repository),
        get_by_id = GetPokemonById(pokemon_repository),
        get_by_name = GetPokemonByName(pokemon_repository),
        filter_by_type = FilterPokemonByType(pokemon_repository)
    )
)

