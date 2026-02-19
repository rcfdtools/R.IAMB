<div align="center"><img alt="rcfdtools" src="../../file/graph/R.IAMB.svg" height="46px"></div>

# 2.2. Vectores - Medio abiótico - Geología
Keywords: `geology` `geological-map` `mot` `uc` `geological-fail` `volcanic` `unidad-geologica` `contacto-geologico` `estructura-falla-lineam`

Descargue el Mapa Geológico de Colombia del [Servicio Geológico Colombiano - SGC](https://www2.sgc.gov.co/MGC/Paginas/mgc_1_5M2023.aspx) y recorte las líneas de falla y unidades cronoestratigráficas hasta el límite municipal del mapa MOT del POT. Describa y explique las fallas y unidades presentes en la zona de estudio. Utilizando la herramienta de geoprocesamiento Intersect, combine el modelo de ocupación territorial MOT con la capa de unidades cronoestratigráficas y a través de un resumen estadístico, obtenga por cada categoría del MOT, las unidades cronoestratigráficas presentes y sus áreas. 

<div align="center"><img src="graph/Geology.png" alt="rcfdtools" width="100%" border="0" /></div>


## Objetivos

* Estudiar la geología de la zona de estudio.
* Estudiar la composición de las unidades cronoestratigráficas.


## Requerimientos

Archivos, actividades previas, lecturas y herramientas requeridas para el desarrollo de esta actividad:

<div align="center">

| Requerimiento                                                                                                 | Descripción                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [:toolbox:Herramienta](https://qgis.org/)                                                                     | QGIS 3.44 o superior.                                                                                                 |
| [:date:magna_origen_nacional.zip](../../file/data/ANLA/magna_origen_nacional.zip)                             | Geodatabase ANLA Magna Origen Nacional.                                                                               |
| [:date:diccionario_datos_geograficos_anla.xlsx](../../file/data/ANLA/diccionario_datos_geograficos_anla.xlsx) | Diccionario de datos geográficos ANLA.                                                                                |
| [:round_pushpin:Zonificacion_Hidrografica_2022.zip](../../file/data/IDEAM/Zonificacion_Hidrografica_2022.zip) | Zonificación Hidrográfica de Colombia a escala 1:100k, IDEAM, 2022.                                                   |
| [:round_pushpin:qgis_basemaps.py](../../file/src/qgis_basemaps.py)                                            | Script en Python para inclusión de mapas base XYZ en QGIS por [opengeos](https://github.com/opengeos/qgis-basemaps).  |

</div>


## 1. Unidad Geológica

Las unidades geológicas comprenden la delimitación y clasificación de una formación geológica que representa la estructura e historia del desarrollo de la corteza terrestre y sus capas más profundas.

1. Ingrese al sitio del [Servicio Geológico Colombiano - SGC](https://www2.sgc.gov.co/MGC/Paginas/mgc_1_5M2023.aspx) y descargue la File Geodatabase del Atlas Geológico de Colombia versión 2023 a escala 1:500K (_agc2023.gdb.zip_) y el archivo de estilos (_agc2023.style_). Guarde y descomprima en la carpeta [/data/SGC/](../../data/SGC). 

<div align="center"><img src="graph/SGC_Download2023.jpg" alt="rcfdtools" width="100%" border="0" /></div>




ContactoGeologico
EstructuraFallaLineam





## Referencias

* [Atlas Geológico de Colombia 2023 a escala 500K.](https://www2.sgc.gov.co/MGC/Paginas/agc_500K2023.aspx)
* [Memoria explicativa del Mapa Geológico de Colombia, Geological Map of Colombia y Atlas Geológico de Colombia 2023.](https://www2.sgc.gov.co/MGC/Documents/MGC_2023/Memoria_mgc_gmc_agc_2023.pdf)


## Control de versiones

| Versión    | Descripción        | Autor                                      | Horas |
|------------|:-------------------|--------------------------------------------|:-----:|
| 2026.02.19 | Versión inicial.   | [rcfdtools](https://github.com/rcfdtools)  |   6   |


##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../CaseStudy/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../XXXX/Readme.md) |
|---------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|----------------------------------|

[^1]: https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Zonificaci-n-Hidrogr-fica-Colombia/5kjg-nuda/about_data 
[^2]: https://archivo.minambiente.gov.co/index.php/noticias/2067

