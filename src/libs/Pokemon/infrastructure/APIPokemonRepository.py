import aiohttp
from typing import List
from ..domain.Entities.PokemonEntity import PokemonEntity
from ..domain.Interfaces.IPokemonRepository import IPokemonRepository
import requests
from PIL import Image
from io import BytesIO


class APIPokemonRepository(IPokemonRepository):
    def __init__(self):
        """
        Initializes a APIPokemonRepository instance.

        Sets the base_url attribute to https://pokeapi.co/api/v2/
        """
        self.__base_url = 'https://pokeapi.co/api/v2/'

    def get_pokemon_by_id(self, id: int) -> PokemonEntity:
        sufix_url = "pokemon/%d" % (id)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        return self.__map_to_entity(data)

    def get_pokemon_by_name(self, name: str) -> PokemonEntity:
        sufix_url = "pokemon/%s" % (name)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        return self.__map_to_entity(data)

    def filter_pokemon_by_type(self, type: str) -> List[PokemonEntity]:
        sufix_url = "type/%s" % (type)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)

        pokemons = data['pokemon']
        pokes = [[self.get_pokemon_by_name(
            p['pokemon']['name']) for p in pokemons]]
        return pokes

    def get_all_pokemons(self) -> List[PokemonEntity]:
        sufix_url = "pokemon"
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        pokemons = data['results']
        pokes = [[self.get_pokemon_by_name(p['name']) for p in pokemons]]
        return pokes

    async def __get_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    def __get_url_sync(self, url):
        response = requests.get(url)
        data = response.json()
        pokemon_image_response = requests.get(data['sprites']['front_default'])
        pokemon_image = Image.open(BytesIO(pokemon_image_response.content))
        data["sprites"]["front_default"] = pokemon_image
        return data

    def __map_to_entity(self, data: dict) -> PokemonEntity:
        abilities: List[str] = [h["ability"]["name"]
                                for h in data['abilities']]
        return PokemonEntity(data['id'], data['name'], data['types'][0]['type']['name'], data['weight'], abilities, data['sprites']['front_default'])
