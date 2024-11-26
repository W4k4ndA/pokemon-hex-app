from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ..domain.Entities.PokemonEntity import PokemonEntity
from ...Shared.Infrastructure.ServiceContainer import ServiceContainer


class TKinterPokemonController:
    
    def get_pokemon_by_name(self, name: str) -> PokemonEntity | None:
        pokemon = ServiceContainer.pokemon.get_by_name.run(name)
        return pokemon
    
    def get_pokemon_by_id(self, id: int) -> PokemonEntity | None:
        pokemon = ServiceContainer.pokemon.get_by_id.run(id)
        return pokemon
        
    def filter_pokemon_by_type(self, type: str) -> list[PokemonEntity]:
        pokemons = ServiceContainer.pokemon.filter_by_type.run(type)
        return pokemons
    
    def get_all_pokemons(self) -> list[PokemonEntity]:
        pokemons = ServiceContainer.pokemon.get_all.run()
        return pokemons
        