#!/usr/bin/python3
import libs.Pokemon.infrastructure.guiui as baseui

"""This code serves as the entry point for the application. It initializes and runs a graphical user
interface (GUI) for interacting with Pokémon data. The application is designed using a hexagonal 
architecture, ensuring that each layer and class is responsible for a specific part of the 
application's functionality. 

The `PokemonGui` class extends `PokemonGUIUI`, which is a GUI component built using Tkinter. This class
is responsible for displaying the interface and handling user interactions. It delegates retrieving and
displaying Pokémon data to the `TKinterPokemonController`, which acts as an intermediary between the
GUI and the application's business logic.

The controller accesses the Pokémon data through a service container, which provides use case classes 
like `GetPokemonByName` and `GetPokemonById`. These use cases interact with the `APIPokemonRepository`,
a repository class responsible for fetching data from an external API (PokeAPI in this case).

This separation of concerns allows each layer to focus on its designated responsibilities, promoting a 
clean and maintainable codebase. The GUI layer manages user interaction, the controller handles 
communication between the UI and the business logic, and the repository layer deals with data retrieval
and persistence.
"""


class PokemonGui(baseui.PokemonGUIUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = PokemonGui()
    app.run()
