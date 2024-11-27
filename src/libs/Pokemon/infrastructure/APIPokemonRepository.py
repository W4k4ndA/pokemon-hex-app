import aiohttp
from typing import List
from ..domain.Entities.PokemonEntity import PokemonEntity
from ..domain.Errors.PokemonNotFoundError import PokemonNotFoundError
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
        """
        Retrieves a PokemonEntity instance with the given id from the repository.

        Parameters:
        id (int): The unique identifier for the Pokemon.

        Returns:
        PokemonEntity: The PokemonEntity instance with the given id if it exists,
        otherwise raises a PokemonNotFoundError.

        Raises:
        PokemonNotFoundError: If the Pokemon with the given id does not exist.
        """

        sufix_url = "pokemon/%d" % (id)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        return self.__map_to_entity(data)

    def get_pokemon_by_name(self, name: str) -> PokemonEntity:
        """
        Retrieves a PokemonEntity instance with the given name from the repository.

        Parameters:
        name (str): The name of the Pokemon to be retrieved.

        Returns:
        PokemonEntity: The PokemonEntity instance with the given name if it exists,
        otherwise raises a PokemonNotFoundError.

        Raises:
        PokemonNotFoundError: If the Pokemon with the given name does not exist.
        """

        sufix_url = "pokemon/%s" % (name)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        return self.__map_to_entity(data)

    def filter_pokemon_by_type(self, type: str) -> List[PokemonEntity]:
        """
        Retrieves a list of PokemonEntity instances with the specified type from the API.

        Parameters:
        type (str): The type category of the Pokemon to be retrieved.

        Returns:
        List[PokemonEntity]: A list of PokemonEntity instances with the specified type.
        """
        sufix_url = "type/%s" % (type)
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)

        pokemons = data['pokemon']
        pokes = [[self.get_pokemon_by_name(
            p['pokemon']['name']) for p in pokemons]]
        return pokes

    def get_all_pokemons(self) -> List[PokemonEntity]:
        """
        Retrieves a list of all PokemonEntity instances from the API.

        Returns:
        List[PokemonEntity]: A list of all PokemonEntity instances in the API.
        """
        sufix_url = "pokemon"
        url = "%s%s" % (self.__base_url, sufix_url)
        data = self.__get_url_sync(url)
        pokemons = data['results']
        pokes = [[self.get_pokemon_by_name(p['name']) for p in pokemons]]
        return pokes

    async def __get_url(self, url):
        """
        (NOT IMPLEMENTED)
        Asynchronously retrieves JSON data from a given URL.

        Parameters:
        url (str): The URL from which to fetch the JSON data.

        Returns:
        dict: The JSON response from the URL as a Python dictionary.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    def __get_url_sync(self, url):
        """
        Synchronously retrieves JSON data from a given URL.

        Parameters:
        url (str): The URL from which to fetch the JSON data.

        Returns:
        dict: The JSON response from the URL as a Python dictionary.
        """
        response = requests.get(url)
        if not response:
            raise PokemonNotFoundError("Pokemon not found")
        data = response.json()
        pokemon_image_response = requests.get(data['sprites']['front_default'])
        # Obtaining the image as bytearray
        pokemon_image = BytesIO(pokemon_image_response.content)
        data["sprites"]["front_default"] = pokemon_image
        return data

    def __map_to_entity(self, data: dict) -> PokemonEntity:
        """
        Maps JSON data to a PokemonEntity instance.

        Parameters:
        data (dict): The JSON data representing a Pokemon, typically retrieved from an API.

        Returns:
        PokemonEntity: An instance of PokemonEntity containing the mapped data.
        """
        abilities: List[str] = [h["ability"]["name"]
                                for h in data['abilities']]
        return PokemonEntity(data['id'], data['name'], data['types'][0]['type']['name'], data['weight'], abilities, data['sprites']['front_default'])
