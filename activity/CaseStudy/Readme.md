<div align="center"><img alt="rcfdtools" src="../../file/graph/R.IAMB.svg" height="46px"></div>

# 2.1. Vectores - Proyecto o caso de estudio
Keywords: `case-study` `base-maps` `project-area`

En el caso de estudio se ha definido como límite geográfico la cuenca hidrográfica del Río Bogotá, la cual se encuentra incluída en la capa geográfica de [Zonificación Hidrográfica de Colombia](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Zonificaci-n-Hidrogr-fica-Colombia/5kjg-nuda/about_data) a escala 1:100k actualizada por el IDEAM en el año 2022.

> La actualización en escala 1:100,000 de la capa de zonificación hidrográfica de Colombia a escala 1:500.000 del 2013, utilizada hasta el ENA2018. Esta capa es la unidad de análisis utilizada en el ENA2022. Representa las unidades de análisis hidrográficas para el ordenamiento ambiental del territorio definidas por el IDEAM. La actualización del producto se realizó con base en la información dispuesta por HydroSheds y la edición sobre cartografía básica a escala 1: 100000, dispuesta por el IGAC en el 2016. Es importante mencionar, que en la zonificación hidrográfica del año 2013, con el fin de generar una cobertura de la zonificación hidrográfica en zonas marítimas en las que existen estaciones de IDEAM o de otras entidades como la DIMAR o el INVEMAR, entre otras, las cuales requieren asignación de codificación acorde con su ubicación, se hizo necesario en su momento definir estas sub-zonas hidrográficas, estas no necesariamente implican la generación de productos temáticos específicos. Para la presente actualización de la zonificación hidrográfica del año 2022, no se incluyen las áreas marino-costeras que se delimitan en la zonificación hidrográfica del año 2013, debido a que no se cuenta con información oficial a escala 1:100.000 que permitan su delimitación. [^1]


## Objetivos

* Definir el límite geográfico de la zona de estudio y área de influencia del proyecto.
* Identificar los límites geográficos de las autoridades ambientales dentro de la zona de estudio.


## Requerimientos

Archivos, actividades previas, lecturas y herramientas requeridas para el desarrollo de esta actividad:

<div align="center">

| Requerimiento                                                                                                  | Descripción                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [:toolbox:Herramienta](https://qgis.org/)                                                                      | QGIS 3.44 o superior.                                                                                                 |
| [:date:magna_origen_nacional.zip](../../file/table/ANLA/magna_origen_nacional.zip)                             | Geodatabase ANLA Magna Origen Nacional.                                                                               |
| [:date:diccionario_datos_geograficos_anla.xlsx](../../file/table/ANLA/diccionario_datos_geograficos_anla.xlsx) | Diccionario de datos geográficos ANLA.                                                                                |
| [:round_pushpin:Zonificacion_Hidrografica_2022.zip](../../file/table/IDEAM/Zonificacion_Hidrografica_2022.zip) | Zonificación Hidrográfica de Colombia a escala 1:100k, IDEAM, 2022.                                                   |
| [:round_pushpin:qgis_basemaps.py](../../file/src/qgis_basemaps.py)                                             | Script en Python para inclusión de mapas base XYZ en QGIS por [opengeos](https://github.com/opengeos/qgis-basemaps).  |

</div>


## 1. Zona de estudio 

1. En QGIS, cree un mapa nuevo en blanco con el nombre _/map/CaseStudy.qgz_, agregue la capa [/data/IDEAM/h_znhd_2022_100K.shp](../../file/data/IDEAM/h_znhd_2022_100K.shp) y abra la tabla de atributos, podrá observar que se compone de 316 Sub-zonas Hidrográficas y que la capa utiliza el EPSG 4686. 

<div align="center"><img src="graph/QGIS_AddLayer.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. Para verificar la localización y geo-referenciación correcta de la capa, ejecute el script [qgis_basemaps.py](../../file/src/qgis_basemaps.py) y agregue el mapa base de Google Maps y Google Satellite. Podrá observar que 

<div align="center"><img src="graph/QGIS_XYZMap1.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_XYZMap2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Rotule e identifique la Sub-zona Hidrográfica 2120 correspondiente a la Cuenca del Río Bogotá.

Rótulo: `'AH: '  || "COD_AH"  ||  ' - '  ||  "nom_ah"   || '\n'  ||  'ZH: '  ||  "COD_ZH"   ||  ' - '  ||   "nom_zh" || '\n'  ||  'SZH: '  ||  "COD_SZH"   ||  ' - '  ||   "nom_szh"`  

<div align="center"><img src="graph/QGIS_Identify.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. Filtre el polígono correspondiente a la Sub-zona Hidrográfica 2120.

<div align="center"><img src="graph/QGIS_Filter.jpg" alt="rcfdtools" width="100%" border="0" /></div>


## 2. Incorporación a capa ANLA: AreaProyecto

1. En la carpeta 




AreaInfluencia









## Referencias

*


## Control de versiones

| Versión    | Descripción        | Autor                                      | Horas |
|------------|:-------------------|--------------------------------------------|:-----:|
| 2026.02.13 | Versión inicial.   | [rcfdtools](https://github.com/rcfdtools)  |   6   |


##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../GISBasicEA.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../M01A02a/Readme.md) |
|--------------------------------|-----------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------|

[^1]: https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Zonificaci-n-Hidrogr-fica-Colombia/5kjg-nuda/about_data 
