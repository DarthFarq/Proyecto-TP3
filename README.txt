En Clase.py esta definida la clase Envio. Cada objeto de la clase envio tiene como atributos su Codigo Postal, su Direccion, 
su Pais (Que lo define el metodo country con el primer digito del codigo postal), el tipo de envio y la forma de pago

En Main.py, se carga un archivo de texto que contiene una cantidad de envios separados en cada linea con el siguiente formato:

   499301Revolucion 2024.    51

Siendo los caracteres del 0 al 8 su codigo postal, los del 9 al 28 su direccion, el tipo seria el caracter 29 y la forma de pago el 30.

La primera linea del archivo contiene dos caracteres que pueden ser Soft Control (SC) y Hard Control (HC), que definen que envios
son validos, y cuales no. 
En el primero se toman todos los envios como validos, mientras que en el segundo, para que un envio sea valido se toman las siguientes condiciones:

 1-La direccion no contiene caracteres especiales
 2-No hay dos mayusculas seguidas
 3-Cada palabra contiene la misma cantidad de letras y digitos

En la funcion principal se define un menu de opciones, con cada opcion teniendo su propia funcion, que ejecuta las siguientes instrucciones:

 Opcion 1: Carga un vector con envios desde un archivo de texto
 Opcion 2: Carga un vector con envios por teclado
 Opcion 3: Lista el vector generado de manera ordenada por codigo postal, permitiendo al usuario elegir cuantos envios quiere ver, solicitandole 
	   ingresar la cantidad por teclado
 Opcion 4: Busca un envio en el vector por su direccion
 Opcion 5: Busca un envio en el vector por su codigo postal
 Opcion 6: En caso de que el tipo de control sea HC, muestra la cantidad de envios validos que tiene cada tipo. Si es SC, muestra la cantidad de envios
           por tipo
 Opcion 7: En caso de que el tipo de control sea HC, muestra el importe final acumulado de los envios validos por tipo. Si es SC, muestra el importe final
           acumulado de todos los envios por tipo
 Opcion 8: Muestra el tipo de envio con mayor acumulacion de importes y el porcentaje que representa respecto de la totalidad de importes, con los importes
	   calculados en la opcion 7.
 Opcion 9: Muestra el promedio de todos los imortes finales, y la cantidad de envios con importes finales menores al promedio
 Opcion 10: Salir del menu

