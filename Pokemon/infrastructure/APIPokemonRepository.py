import asyncio
import aiohttp
from typing import List
from ..domain.Entities.PokemonEntity import PokemonEntity
from ..domain.Interfaces.IPokemonRepository import IPokemonRepository

class APIPokemonRepository(IPokemonRepository):
    def __init__(self, repository : IPokemonRepository):
        self.__base_url = 'https://pokeapi.co/api/v2/'
    
    async def get_pokemon_by_id(self, id: int) -> PokemonEntity:
        sufix_url = "pokemon/%d" %(id)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = await self.__get_url(url)
        return self.__map_to_entity(data)
    
            
    async def get_pokemon_by_name(self, name: str) -> PokemonEntity:
        sufix_url = "pokemon/%s" %(name)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = await self.__get_url(url)
        return self.__map_to_entity(data)
    
    
    async def filter_pokemon_by_type(self, type: str) -> List[PokemonEntity]:
        sufix_url = "type/%s" %(type)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = await self.__get_url(url)
        
        pokemons = data['pokemon']
        pokes = await asyncio.gather(*[self.get_pokemon_by_name(p['pokemon']['name']) for p in pokemons])
        return pokes
    
    async def get_all_pokemons(self) -> List[PokemonEntity]:
        sufix_url = "pokemon"
        url = "%s%s" % (self.__base_url, sufix_url)
        data = await self.__get_url(url)
        pokemons = data['results']
        pokes = await asyncio.gather(*[self.get_pokemon_by_name(p['name']) for p in pokemons])
        return pokes

    
    async def __get_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
        
    def __map_to_entity(self, data: dict) -> PokemonEntity:
        habilities : List[str] = [h["hability"]["name"] for h in data['abilities']]
        return PokemonEntity(data['id'], data['name'], data['types'][0]['type']['name'], data['weight'], habilities, data['sprites']['front_default'])  

