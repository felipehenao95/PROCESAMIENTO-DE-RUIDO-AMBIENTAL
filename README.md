# PROCESAMIENTO-DE-RUIDO-AMBIENTAL

Procesamiento de ruido ambiental

Este programa se diseñó para organizar y realizar el procesamiento de datos de ruido ambiental de 26 estaciones de monitoreo,  principalmente toma todos los datos ya compilados y procesados en archivos de texto y los organiza en dataframes para así realizar las operaciones necesarias para el calculo que exigen las normas internacionales de medición de ruido ambiental, tales como la Resolución 0627 del 2006 y las normativas ISO 1996 -1 y ISO 1996 – 2. A continuación se indica el paso a paso del correcto funcionamiento del programa:

1.	En primera instancia el programa debe reconocer o ubicar las carpetas donde se encuentran todos los archivos procesados y organizados por estación de la siguiente manera:

2.	Una vez estén organizadas las carpetas con los archivos .txt procesados, tenemos que decirle a programa donde están ubicados estos archivos, el script esta separado por funciones y secciones, en la sección llamada """ CREACION DE DIRECCIONES PARA OBTENER DATOS DE CADA ESTACION """ editamos las variables rutLdLn, rutPico, rutimp y rutTerOct, las cuales contienen la ruta donde se encuentran ubicados los archivos procesados.

Ubicación especifica:
Ubicación sencilla (el archivo .py ubicado en la misma carpeta donde están las 26 carpetas de cada estación):

3.	El siguiente paso es correr el script. En la terminal del IDE que se este usando nos indicara las estaciones que cargaron los datos exitosamente, al terminar de compilar los datos de todas las estaciones, el algoritmo realiza las operaciones matemáticas para calcular los indicadores que establecen las normativas, indicadores como: correcciones tonales e impulsivas, LDN, Lpeak, Ld y Ln corregidos y niveles por tercios de octava en ponderación A. 

4.	Una vez se termine todo el procesamiento, el programa creara un archivo de Excel con el compilado de resultados de todas las estaciones en una misma hoja llamada "EMRIS" y adicional creara 26 hojas de Excel con los resultados finales de cada estación, así como se muestra a continuación:
 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ambient noise processing

This program was designed to organize and perform the processing of environmental noise data from 26 monitoring stations, mainly it takes all the data already compiled and processed in text files and organizes them in dataframes in order to perform the necessary operations for the calculation that are required in the international standards for environmental noise measurement, such as Resolution 0627 of 2006 and the ISO 1996 -1 and ISO 1996 - 2 standards. Below is the step by step of the correct operation of the program:

1.	In the first instance, the program must recognize or locate the folders where all the processed files are located and organized by station as follows: 

2.	Once the folders with the processed .txt files are organized, we have to tell the program where these files are located, the script is separated by functions and sections, in the section called """ CREACION DE DIRECCIONES PARA OBTENER DATOS DE CADA ESTACION """ We edit the variables rutLdLn, rutPico, rutimp and rutTerOct, which contain the path where the processed files are located.

-	Specific location
-	Simple location (the .py file located in the same folder where the 26 folders for each station are):

3.	The next step is to run the script. In the IDE terminal that is being used, it will indicate the stations that loaded the data successfully, when finishing compiling the data from all the stations, the algorithm performs the mathematical operations to calculate the indicators established by the regulations, indicators such as: tonal corrections and impulsive, corrected LDN, Lpeak, Ld and Ln, and A-weighted third-octave levels.

4.	Once all the processing is finished, the program will create an Excel file with the results of all the stations compiled in the same sheet called "EMRIS" and additionally it will create 26 Excel sheets with the final results of each station.
