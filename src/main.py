#!/usr/bin/python3
import asyncio
import tkinter as tk
import tkinter.ttk as ttk
import guiui as baseui
from libs.Pokemon.infrastructure.TKinterPokemonController import TKinterPokemonController
from PIL import Image, ImageTk


class PokemonGui(baseui.PokemonGUIUI):
    def __init__(self, master=None):
        self.__controller = TKinterPokemonController()
        super().__init__(master)

    def pokemon_get_by_name(self):
        name = self.entry_nombre.get()
        pokemon = self.__controller.get_pokemon_by_name(name)
        self.__display_pokemon_data(pokemon)

    def pokemon_get_by_id(self):
        id = int(self.entry_id.get())
        pokemon = self.__controller.get_pokemon_by_id(id)
        self.__display_pokemon_data(pokemon)

    def __display_pokemon_data(self, pokemon):
        text = "Nombre: %s\n\nTipo: %s\n\nPeso: %s\n\nHabilidades: %s" % (
            pokemon.name, pokemon.type, pokemon.weight, pokemon.abilities)
        self.info_text.set("")
        self.info_text.set(text)

        pokemon.image_bytearray = pokemon.image_bytearray.resize((200, 200))
        image_data = pokemon.image_bytearray

        image_tk = ImageTk.PhotoImage(image_data, size=(100, 100))

        self.img_data.delete("all")
        self.img_data.create_image(130, 150, image=image_tk)
        self.img_data.image = image_tk


if __name__ == "__main__":
    app = PokemonGui()
    app.run()
