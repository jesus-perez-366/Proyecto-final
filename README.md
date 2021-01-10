# <div style="text-align:center"><img src=imagen/house-for-sale2.jpg width="1000"> 
# <div style="text-align:center"> JAPS HOUSE

## Objetivo
   Automatizar la búsqueda en la web de los pisos en alquiler en Madrid  publicados en las diferentes páginas web de inmobiliarias (RedPiso y Habitaclia).

<br>

## Resumen del funcionamiento del código
   Se hace una solicitud POST  desde un formulario html a través de una API, posteriormente se ejecuta una función que realiza el Scraping Web de las inmobiliarias, luego se genera un DataFrame y la respuesta de la solicitud es un mapa con la ubicación de piso y envió de la información (“archivo.cvs”) por email.

<br>

## Funcionamiento de la web

1.- Seleccionar la Provincia.

2.- Seleccionar el Barrio.

3.- Seleccionar el número de habitaciones.

4.- Seleccionar el Orden de los Precios.

5.- Selecionar si desea solo mostrar los primeros 20 resultados.

6.- indicar si desea enviar la informacion a obtener a su correo.

7.- indicar el correo electronico en caso de que en el paso 6 haya indicado una respuesta afirmativa.

8.- HaCer click en "BUSCAR".

<br>

## Imagenes

<div style="text-align:center">Web 
<br>

 <div style="text-align:center"><img src=imagen/web.jpg width="1000">

<br>
<br>
<br>

Resultado de la busqeda

 <div style="text-align:center"><img src=imagen/web_resul.jpg width="1000">

<br>
<br>
<br>

<div style="text-align:center">Al hacer click sobre el icono

Te muestra la informacion sobre el piso (precio, Nº hab, Nº baños y el link)
<br>

 <div style="text-align:center"><img src=imagen/click.jpg width="1000">

<br>
<br>
<br>

Al hacer click sobre "link"

Te abre la paguina web del piso que deseas.

 <div style="text-align:center"><img src=imagen/link.jpg width="1000">







