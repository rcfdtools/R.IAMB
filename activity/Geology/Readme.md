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

La capa _UnidadGeologica_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene varios dominios asociados:

<div align="center"><img src="graph/ANLA_UnidadGeologica.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Dominios: Dom_Geol_Eon, Dom_Geol_Era, Dom_Geol_Per, Dom_Geol_Epo, Dom_Geol_Eda

<div align="center"><img src="graph/ANLA_Dom_Geol_Eon.jpg" alt="rcfdtools" width="25%" border="0" /><img src="graph/ANLA_Dom_Geol_Era.jpg" alt="rcfdtools" width="25%" border="0" /><img src="graph/ANLA_Dom_Geol_Per.jpg" alt="rcfdtools" width="25%" border="0" /><img src="graph/ANLA_Dom_Geol_Epo.jpg" alt="rcfdtools" width="25%" border="0" /><img src="graph/ANLA_Dom_Geol_Eda.jpg" alt="rcfdtools" width="25%" border="0" /></div>

> Para los dominios Dom_Geol_Epo y Dom_Geol_Eda, solo se ha incluido en las ilustraciones, una muestra de los primeros valores codificados. Consulte la lista completa de valores en el diccionario de datos.

1. Ingrese al sitio del [Servicio Geológico Colombiano - SGC](https://www2.sgc.gov.co/MGC/Paginas/mgc_1_5M2023.aspx) y descargue la File Geodatabase del Atlas Geológico de Colombia versión 2023 a escala 1:500K (_agc2023.gdb.zip_) y el archivo de estilos (_agc2023.style_). Guarde y descomprima en la carpeta [/data/SGC/](../../file/data/SGC). 

<div align="center"><img src="graph/SGC_Download2023.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS, cree un nuevo mapa de proyecto y guarde como _/map/Geology.qgz_ y establezca el CRS 9377. Agregue al mapa la capa de unidades cronoestratigráficas (_UC_ y _UCAnot_)contenidas en la GDB `/data/SGC/agc2023.gdb/Geologia/` y ajuste la simbología a valores únicos representando el campo de atributos `Simbolo_UC`. Podrá observar que los colores de representación no se ajustan a los definidos en la [Tabla Cronoestratigráfica Internacional](../../file/ref/ChronostratChart2023-04SpanishAmer.pdf)[^1]. Rotule a partír de las localizaciones definidas en _UCAnot_ desactivando la visualización del rectángulo envolvente al rótulo.

<div align="center"><img src="graph/ChronostratChart2023-04SpanishAmer.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_AddLayer1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Para incorporar en QGIS los estilos contenidos en el archivo _agc2023.style_ del SGC diseñados para ArcGIS, es necesario convertir el archivo .style a formato XML. Desde el menú _Plugins / Manage and Install Plugins..._, instale SLYR (Community Edition).

<div align="center"><img src="graph/QGIS_PluginSLYR.png" alt="rcfdtools" width="100%" border="0" /></div>

Descargue desde https://github.com/lsgunth/mdbtools-win/archive/master.zip, el gestor de bases de datos _mdbtools_ para Windows y descomprima en la carpeta [/tools/](../../file/tools).

En el panel del Processing Tool o desde las propiedades del proyecto QGIS, acceda a las opciones de configuración y en la pestaña SLYR realice la asociación de ruta a MDB Tools.

<div align="center"><img src="graph/QGIS_MDBTools.png" alt="rcfdtools" width="100%" border="0" /></div>

Ejecute el Processing Toolbox / SLYR / Style databases / Convert ESRI style to QGIS style XML, así obtendrá el archivo de estilos en formato XML, guarde como [/data/SGC/agc2023.xml](../../file/data/SGC/agc2023.xml).

<div align="center"><img src="graph/QGIS_StyleToXML.png" alt="rcfdtools" width="100%" border="0" /></div>

4. Desde el menú _Settings_ de QGIS, ejecute el _Style Manager_ e importe todos los estilos contenidos en el archivo XML convertido.

<div align="center"><img src="graph/QGIS_StyleManager1.png" alt="rcfdtools" width="100%" border="0" /></div>

Verifique los estilos importados como agc2023 en el grupo Tags.

<div align="center"><img src="graph/QGIS_StyleManager2.png" alt="rcfdtools" width="100%" border="0" /></div>

> La importación de los estilos no actualiza automáticamente los colores aplicados a las unidades cronoestratigráficas, su aplicación puede ser realizada manualmente utilizando los códigos y colores importados.

Para aplicar un estilo, en la tabla de contenido de clic sobre una de las UC (p. ej., C-Pi), en el panel de simbología podrá observar que se ha incluido un grupo de estilo nuevo, denominado _agc2023_. Para aplicar el estilo _C-Pi_, correspondiente a _Dioritas, granodioritas, cuarzodioritas, tonalitas y gabros_, seleccione el símbolo correspondiente.

<div align="center"><img src="graph/QGIS_Style.jpg" alt="rcfdtools" width="100%" border="0" /></div>






## 2. ContactoGeologico

2. En QGIS, cree un nuevo mapa de proyecto y guarde como _/map/Geology.qgz_ y establezca el CRS 9377. Agregue al mapa la capa de unidades cronoestratigráficas (_UC_ y _UCAnot_) y fallas geológicas (_Fallas_ y _FallasAnot_) contenidas en la GDB `/data/SGC/agc2023.gdb/Geologia/` y ajuste la simbología a valores únicos representando el campo de atributos `Simbolo_UC`.


## 3. EstructuraFallaLineam




## Referencias

* [Atlas Geológico de Colombia 2023 a escala 500K.](https://www2.sgc.gov.co/MGC/Paginas/agc_500K2023.aspx)
* [Memoria explicativa del Mapa Geológico de Colombia, Geological Map of Colombia y Atlas Geológico de Colombia 2023.](https://www2.sgc.gov.co/MGC/Documents/MGC_2023/Memoria_mgc_gmc_agc_2023.pdf)
* https://opengislab.com/blog/2019/3/16/converting-esri-styles-to-qgis-styles-using-slyr


## Control de versiones

| Versión    | Descripción        | Autor                                      | Horas |
|------------|:-------------------|--------------------------------------------|:-----:|
| 2026.02.19 | Versión inicial.   | [rcfdtools](https://github.com/rcfdtools)  |   6   |


##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../CaseStudy/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../XXXX/Readme.md) |
|---------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|----------------------------------|

[^1]: Cohen, K.M., Finney, S.C., Gibbard, P.L. y Fan, J.-X. (2013; actualizado) The ICS International Chronostratigraphic Chart. Episodes 36: 199-204. 
[^2]: 

