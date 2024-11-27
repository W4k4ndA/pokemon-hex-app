#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from libs.Pokemon.infrastructure.TKinterPokemonController import TKinterPokemonController


class PokemonGUIUI:
    def __init__(self, master=None):
        """
        Initializes a PokemonGUIUI instance.
        It builds the GUI with all the widgets and sets up the event handlers.

        Args:
            master (tk.Tk): The toplevel widget to use as master.

        Attributes:
            __controller (TKinterPokemonController): The controller to use for the GUI.
            mainwindow (tk.Tk): The main window of the GUI.

        """
        self.__controller = TKinterPokemonController()

        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(background="red", height=200, width=200)
        toplevel1.geometry("332x617")
        toplevel1.resizable(False, False)
        toplevel1.title("PokedeX")
        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, relief="ridge", width=200)
        self.img_data = tk.Canvas(frame1, name="img_data")
        self.img_data.configure(background="black", cursor="none")
        self.img_data.place(
            anchor="nw",
            height=280,
            relx=0.03,
            rely=0.03,
            width=240,
            x=0,
            y=0)
        frame1.place(height=300, relx=0.09, rely=0.18, width=260, x=0, y=-30)
        self.info = tk.Message(toplevel1, name="info")
        self.info_text = tk.StringVar()
        self.info.configure(
            background="green",
            font="{Calibri} 9 {bold}",
            justify="left",
            padx=1,
            pady=1,
            relief="raised",
            textvariable=self.info_text)
        self.info.place(height=150, width=150, x=30, y=430)
        self.entry_nombre = ttk.Entry(toplevel1, name="entry_nombre")
        self.entry_nombre.configure(font="{Calibri} 11 {}")
        self.entry_nombre.place(width=80, x=200, y=450)
        self.label_nombre = ttk.Label(toplevel1, name="label_nombre")
        self.label_nombre.configure(
            background="#ff0000",
            compound="center",
            font="{Calibri} 12 {bold}",
            justify="center",
            text='Nombre')
        self.label_nombre.place(bordermode="inside", x=212, y=425)
        self.btn_nombre = ttk.Button(toplevel1, name="btn_nombre")
        self.nombre_buscar = tk.StringVar(value='Fnd')
        self.btn_nombre.configure(
            cursor="hand2",
            text='Fnd',
            textvariable=self.nombre_buscar)
        self.btn_nombre.place(bordermode="outside", width=30, x=290, y=449)
        self.btn_nombre.configure(command=self.pokemon_get_by_name)
        self.entry_id = ttk.Spinbox(toplevel1, name="entry_id")
        self.entry_id.configure(
            font="{Calibri} 11 {}",
            from_=1,
            increment=1,
            to=300)
        _text_ = '1'
        self.entry_id.delete("0", "end")
        self.entry_id.insert("0", _text_)
        self.entry_id.place(width=80, x=205, y=550)
        self.btn_id = ttk.Button(toplevel1, name="btn_id")
        self.btn_id.configure(cursor="hand2", text='Fnd')
        self.btn_id.place(
            anchor="nw",
            bordermode="inside",
            width=30,
            x=293,
            y=548)
        self.btn_id.configure(command=self.pokemon_get_by_id)
        self.label_id = ttk.Label(toplevel1, name="label_id")
        self.label_id.configure(
            background="#ff0000",
            compound="center",
            font="{Calibri} 12 {bold}",
            justify="center",
            text='ID')
        self.label_id.place(bordermode="inside", x=235, y=525)
        label1 = ttk.Label(toplevel1)
        label1.configure(
            background="#eb0214",
            compound="top",
            font="{Forte} 36 {}",
            foreground="#ffff00",
            justify="center",
            relief="sunken",
            text='POKEDEX')
        label1.place(x=50, y=10)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        """
        Starts the main event loop of the GUI.

        This method starts the main event loop of the GUI. The GUI will not appear
        on the screen until this method is called. The method does not return until
        the user closes the GUI.

        """
        #
        self.mainwindow.mainloop()

        # User Defined methods
    # use the use case via TKinerPokemonController's __controller instance
    def pokemon_get_by_name(self):
        """
        Retrieves a PokemonEntity instance by its name from the repository via the
        controller instance and displays its data in the GUI.

        This method retrieves a PokemonEntity instance by its name from the repository
        via the controller instance and displays its data in the GUI. The method does
        not return any value.

        """
        name = self.entry_nombre.get()
        pokemon = self.__controller.get_pokemon_by_name(name)
        self.__display_pokemon_data(pokemon)

    # use the use case via TKinerPokemonController's __controller instance
    def pokemon_get_by_id(self):
        """
        Retrieves a PokemonEntity instance by its id from the repository via the
        controller instance and displays its data in the GUI.

        This method retrieves a PokemonEntity instance by its id from the repository
        via the controller instance and displays its data in the GUI. The method does
        not return any value.
        """
        id = int(self.entry_id.get())
        pokemon = self.__controller.get_pokemon_by_id(id)
        self.__display_pokemon_data(pokemon)

        # Helper method for display the pokemon on the data visualizator (text and image)
    def __display_pokemon_data(self, pokemon):
        """
        Displays the data and image of a given PokemonEntity instance in the GUI.

        This method formats the Pokemon's attributes into a string and sets it to 
        a text variable to be displayed in the GUI. It also processes and displays 
        the Pokemon's image.

        Parameters:
        pokemon (PokemonEntity): The PokemonEntity instance containing the data 
        and image to be displayed.
        """
        text = "Nombre: %s\n\nTipo: %s\n\nPeso: %s\n\nHabilidades: %s" % (
            pokemon.name, pokemon.type, pokemon.weight, pokemon.abilities)
        self.info_text.set("")
        self.info_text.set(text)

        pokemon_image = Image.open(pokemon.image_bytearray)
        pokemon_image = pokemon_image.resize((200, 200))

        image_data = pokemon_image

        image_tk = ImageTk.PhotoImage(image_data, size=(100, 100))

        self.img_data.delete("all")
        self.img_data.create_image(130, 150, image=image_tk)
        self.img_data.image = image_tk


if __name__ == "__main__":
    app = PokemonGUIUI()
    app.run()
