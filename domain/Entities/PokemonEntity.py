


# Definimos nuestro dominio
class PokemonEntity:
    def __init__(self, id: int, name: str, type: str, weight: float, abilities: list[str], image_bytearray: str):
        """
        Initializes a PokemonEntity instance.

        Parameters:
        id (int): The unique identifier for the Pokemon.
        name (str): The name of the Pokemon.
        type (str): The type category of the Pokemon (e.g., Water, Fire).
        weight (float): The weight of the Pokemon.
        abilities (list[str]): A list of abilities that the Pokemon possesses.
        image_bytearray (str): The bytearray representation of the Pokemon's image.
        """
        self.id = id
        self.name = name
        self.type = type
        self.abilities = abilities
        self.weight = weight
        self.image_bytearray = image_bytearray
    
    