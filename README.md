<h1>Introducción</h1> 
<p>  
Este proyecto es una aplicación de interfaz gráfica para crear una Pokedex que interactua con datos de Pokémon alojados en la api PokemonAPI, <b>diseñada utilizando la arquitectura hexagonal.</b>
La aplicación se divide en tres capas principales: dominio, aplicación e infraestructura.
</p>

<p>
  La idea es que esta aplicacion sirva de referencia, junto con mi otro repo sobre <a href="https://github.com/W4k4ndA/hex_arq_python">arquitectura hexagonal en python</a>,
  para aquellas personas que programamos python y queremos aprender a utilizarlo bajo la premisa de las clean arquitectures.
</p>

<p>
  Este repo esta inspirado en ejemplo de <a href="https://www.youtube.com/watch?v=nFJ3Ba7aOdg&t=1s">Linkfy</a> para crear una app multiplataforma con Flet, creando una Pokedex
  Linkfy es un programador python español cuyo canal de youtube te dejo <a href="https://www.youtube.com/@Linkfydev">aquí</a> y que realmente recomiendo muchisimo. Su contenido es 
  muy digerible, facil y rapido de captar a pesar de que muchas veces explica conceptos que no son para nada triviales. Si programas python, de seguro tendras mas de una cosa que 
  aprender de el. En fin, A diferencia
  de su proyecto, yo en lugar de flet, use Tkinter que es la biblioteca de interfaces graficas que viene incluida en python. Y como Tkinter no tiene soporte para asincronia todos
  mis metodos y funciones se declararon sincronos.
</p>
<p>
  En cualquier caso, el hecho es que puedas ver como se puede aplicar arquitectura hexagonal en cualquier proyecto y tengas una referencia que pueda ayudarte a orientarte
  en algun momento que lo necesites.
</p>
<p>
  Por ultimo, esta Pokedex, a diferencia de la de <a href="https://www.youtube.com/watch?v=nFJ3Ba7aOdg&t=1s">Linkfy</a> permite buscar pokemons por Id y por Nombre
</p>

<h1>Capas de la Arquitectura Hexagonal</h1>

<p>
  La arquitectura hexagonal es un arquitectura de software que forma parte de las clean arquitectures y se podria considerar la mas purista de todas. No ve voy a
   alargar mucho en esto porque en internet abundan los articulos, referencias y videos sobre ella. Sin embargo es bueno recalcarlo para que sepas de que se trata todo esto
</p>
<p>
  Esta arquitectura propone dividir tu software en capas y cada capa tiene una responsabilidad unica y encapsula en si misma una parte del todo que compone tu software. 
  Estas capas son las siguientes:
  <ul>
    <li>Domino</li>
    <li>Aplicacion (No te confuncas, aplicacion es en realidad una interfaz o un enlace entre la infrastructura y el dominio)</li>
    <li>Infraestructura</li>
  </ul>
</p>

<h2>Dominio (Domain)</h2>
<p>
  <b>La capa de dominio se encarga de definir las entidades y reglas de negocio de la aplicación</b>. Esto se representa mediante la creacion de <b>Entidades</b> (clases 
  que modelan tus datos), <b>Interfaces</b> (principalmente para la persistencia de datos) y <b>Value Objects</b> (son clases que definen un dato y un validador para ese dato mediante
  un metodo que se ejecuta sobre el dato pasado como parametro a la clase, todo esto durante la construccion del objeto o la instancia de la clase. Esta vez no se usaron). 
  En este caso, se define la entidad PokemonEntity que representa un Pokémon con sus atributos y métodos. La capa de dominio también define la interfaz 
  IPokemonRepository que especifica los métodos para interactuar con los datos de Pokémon.
  
  Se escribió de esta manera para separar la lógica de negocio de la aplicación de la infraestructura y la interfaz gráfica. De esta forma, se puede cambiar 
  la implementación de la capa de infraestructura sin afectar la lógica de negocio. Por ejemplo, si ahora quisiera que la pokedex fuese una pagina web en lugar de una
  app de escritorio, solo debo definir esto en la infrastructura y hacer uso del modulo Pokemon que usa la app de escritorio. Esto implicaria crear la infraestructura 
  para la app web pero sin necesidad de modificar nada de la ya creada para la app de escritorio.
</p>

<h2>Aplicación (Application)</h2>
<p>
  La capa de aplicación se encarga de crear los casos de uso de la lógica de negocio de la aplicación. Es decir, estblece una conexion entre la infraestrctura y el domino. En este caso, 
  se creo el directorio PokemonUseCases que internamente contiene las clases que implementan los métodos para interactuar con los datos de Pokémon. 
  
  Se escribió de esta manera para encapsular la lógica de negocio de la aplicación y proporcionar una interfaz para interactuar con los datos de Pokémon. Dentro de la 
  arquitectura hexagonal usualmente la capa de aplicacion <b>SOLO</b> contiene una clase intermedia a la que se le inyecta la dependencia del repositorio a traves
  de su constructor y que a su vez tiene un metodo que implementa alguno(s) de los metodos del repositorio. Como dije antes es una capa de "conexion" entre el dominio y la infrastructura.
</p>

<h2>Infraestructura (Infrastructure)</h2>
<p>
  <b>La capa de infraestructura se encarga de implementar la persistencia de datos, la comunicacion con el dominio</b> y donde se implementa la <i>infrastructura</i> de la aplicacion 
  bien sea de escritorio, bien sea movil o sea web. Es por esto que es aqui donde se define la interfaz grafica de usuario que se definio para la aplicacion.
  En este caso, se define la clase APIPokemonRepository que implementa la persistencia de datos mediante una API externa. La capa de infraestructura también define la clase 
  TKinterPokemonController que actúa como un controlador entre la interfaz gráfica y la capa de aplicación (si, otro "conctor" entre ambas cosas).
  
  Se escribió de esta manera para separar la implementación de la persistencia de datos y la comunicación con la interfaz gráfica de la lógica de negocio de la aplicación.
</p>
<p>
  Hay un directorio que se genera llamado Shared. En este directorio se define la clase ServiceContainer que actúa como un contenedor de servicios (o mas bien de dependencias) 
  y proporciona acceso a los métodos de la capa de aplicación.
</p>

<h3>Interfaz Gráfica</h3>

<p>
La interfaz gráfica se implementó utilizando Tkinter y se diseñó mediante la herramienta Pygubu-Designer. La herramienta Pygubu-Designer permite crear la interfaz gráfica de manera gráfica y genera un archivo .ui que se utiliza para crear la interfaz gráfica en la aplicación.

Se utilizó Tkinter para la interfaz gráfica debido a su facilidad de uso y su capacidad para crear interfaces gráficas complejas.
  
</p>

<h1>Conclusión</h1>
<p>
  En resumen, este proyecto es una aplicación de interfaz gráfica para interactuar con datos de Pokémon, diseñada utilizando la arquitectura hexagonal. La aplicación se divide en tres capas principales: dominio, aplicación y infraestructura. La interfaz gráfica se implementó utilizando Tkinter y se diseñó mediante la herramienta Pygubu-Designer. La aplicación está diseñada para ser escalable y mantenible, y se puede cambiar la implementación de la capa de infraestructura sin afectar la lógica de negocio.
</p>
<p>
  Ten en cuenta que no pretendo que mi codigo sea perfecto. En realidad hay varias cosas que no hice que podrian ayudar a que estuviese mas en consonancia con los principios <b>SOLID</b> 
  por ejemplo. Pero la idea era implementar la arquitectura en un proyecto que realmente no la usara para ver como se puede hacer y que sirva de guia para cosas mas grandes.
</p>

