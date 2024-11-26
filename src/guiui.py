#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class PokemonGUIUI:
    def __init__(self, master=None):
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
        self.mainwindow.mainloop()

    def pokemon_get_by_name(self):
        pass

    def pokemon_get_by_id(self):
        pass


if __name__ == "__main__":
    app = PokemonGUIUI()
    app.run()
