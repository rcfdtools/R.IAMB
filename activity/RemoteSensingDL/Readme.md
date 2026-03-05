<div align="center"><img alt="rcfdtools" src="../../file/graph/R.IAMB.svg" height="46px"></div>

# 2.4. Imagen satelital y DEM
Keywords: `sentinel` `landsat` `remote-sensing` `clip-raster`

Descargue, cree un mosaico y recorte imágenes satelitales hasta el límite de la zona de estudio.

<div align="center"><img src="graph/RemoteSensingDL.jpg" alt="rcfdtools" width="70%" border="0" /></div>


## Objetivos

* Estudiar los tipos de suelos presentes en la zona de estudio, sus vocaciones principales y los conflictos identificados por la autoridad catastral nacional.
* Calcular la distribución porcentual de los diferentes suelos identificados en la zona de estudio.
* Aplicar los conceptos y habilidades de homologación de atributos.


## Requerimientos

Archivos, actividades previas, lecturas y herramientas requeridas para el desarrollo de esta actividad:

<div align="center">

| Requerimiento                                                                                                 | Descripción                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [:toolbox:Herramienta](https://qgis.org/)                                                                     | QGIS 3.44 o superior.                                                                                                |
| [:date:magna_origen_nacional.zip](../../file/data/ANLA/magna_origen_nacional.zip)                             | Geodatabase ANLA Magna Origen Nacional.                                                                              |
| [:date:diccionario_datos_geograficos_anla.xlsx](../../file/data/ANLA/diccionario_datos_geograficos_anla.xlsx) | Diccionario de datos geográficos ANLA.                                                                               |
| [:round_pushpin:qgis_basemaps.py](../../file/src/qgis_basemaps.py)                                            | Script en Python para inclusión de mapas base XYZ en QGIS por [opengeos](https://github.com/opengeos/qgis-basemaps). |
| [:construction_worker:Usuario USGS](https://ers.cr.usgs.gov/register/contact)                                 | Cuenta de usuario en el USGS - United States Geological Survey (Satellital images).                     |
| [:construction_worker:Usuario Copernicus](https://dataspace.copernicus.eu/)                                   | Cuenta de usuario en el European Union's Earth observation program (ERA5 data).                         |
| [:construction_worker:Usuario OpenTopography](https://portal.opentopography.org/newUser)                      | Cuenta de usuario en OpenTopography (high-resolution topographic data as LiDAR, radar, photogrammetry). |

</div>


## 0. Introducción general a sensores remotos y fotointerpretación [^1]

Los sensores remotos o Teledetección [^2] comprenden diversas técnicas para localización, captura y transmisión de datos de objetos y fenómenos a distancia, sin contacto físico con el elemento o fenómeno de interés. Algunas de sus aplicaciones más interesantes en la ingeniería civil y ambiental son: representación y análisis de modelos de terreno - elevación, elaboración de mapas de pendientes, composición de bandas de imágenes para la restitución masiva de cuerpos de agua, delimitación detallada de cuencas hidrográficas y morfometría, monitoreo de vegetación y evaluación de su calidad por medio de índices, monitoreo de contaminación atmosférica, seguir trayectoria de huracanes, medir fenómenos de remoción en masa, flujo por avalanchas, inundaciones y fenómenos de expansión urbana, entre otros.

### 0.1. Espectro electromagnético

Comprende el rango completo de longitudes de onda (frecuencias) por el que se extiende la radiación electromagnética.

<div align="center"><img src="graph/Graph_ElectromagneticSpectrum.png" alt="rcfdtools" width="90%" border="0" /><br><sub>Imagen tomada de learn.arcgis.com </sub></div>


### 0.2. Plataformas utilizadas en sensores remotos satelitales


#### 0.2.1. Landsat [^3]

Los Landsat son una serie de satélites construidos y puestos en órbita por Estados Unidos de América para la observación en alta resolución de la superficie terrestre. Los satélites Landsat orbitan alrededor de la Tierra en órbita circular heliosincrónica, a 705 km de altura, con una inclinación de 98.2º respecto del ecuador y un período de 99 minutos. La órbita de los satélites está diseñada de tal modo que cada vez que estos cruzan el ecuador de norte a sur lo hacen entre las 10:00 y las 10:15 de la mañana hora local. Los Landsat están equipados con instrumentos específicos para la teledetección multiespectral. El primer satélite Landsat (en principio denominado ERTS-1) fue lanzado el 23 de julio de 1972. Landsat 9 fue puesto en órbita el 27 de septiembre de 2021. La resolución de las imágenes capturadas es de 15 a 100 metros dependiendo de la banda espectral y el modo de captura. https://landsat.gsfc.nasa.gov/

<div align="center"><img src="graph/Graph_LandsatTimeLine.png" alt="rcfdtools" width="70%" border="0" /><br><sub>Imagen tomada de learn.arcgis.com </sub></div>

<div align="center"><br>Bandas y longitudes de onda

| Landsat 7<br>Banda                   | Landsat 7<br>Ancho (µm) | Landsat 7<br>Resolución (m) | Landsat 8/9<br>Banda                   | Landsat 8/9<br>Ancho (µm) | Landsat 8/9<br>Resolución (m) |
|--------------------------------------|:-----------------------:|:---------------------------:|----------------------------------------|:-------------------------:|:-----------------------------:|
|                                      |                         |                             | Band 1 Coastal Aerosol                 |        0.43 – 0.45        |              30               |
| Band 1 Blue                          |       0.45 – 0.52       |             30              | Band 2 Blue                            |        0.45 – 0.51        |              30               |
| Band 2 Green                         |       0.52 – 0.60       |             30              | Band 3 Green                           |        0.53 – 0.59        |              30               |
| Band 3 Red                           |       0.63 – 0.69       |             30              | Band 4 Red                             |        0.64 – 0.67        |              30               |
| Band 4 NIR<br>Near Infrared          |       0.77 – 0.90       |             30              | Band 5 NIR<br>Near Infrared            |        0.85 – 0.88        |              30               |
| Band 5 SWIR1<br>Shortwave Infrared 1 |       1.55 – 1.75       |             30              | Band 6 SWIR1<br>Shortwave Infrared 1   |        1.57 – 1.65        |              30               |
| Band 7 SWIR2<br>Shortwave Infrared 2 |       2.09 – 2.35       |             30              | Band 7 SWIR2<br>Shortwave Infrared 2   |        2.11 – 2.29        |              30               |
| Band 8 Panchromatic                  |       0.52 – 0.90       |             15              | Band 8 Panchromatic                    |        0.50 – 0.68        |              15               |
|                                      |                         |                             | Band 9 Cirrus [^7]                     |        1.36 – 1.38        |              30               |
| Band 6 TIR<br>Thermal Infrared       |      10.40 – 12.50      |            30/60            | Band 10 TIRS1 [^8]<br>Thermal Infrared |       10.6 – 11.19        |              100              |
|                                      |                         |                             | Band 11 TIRS2<br>Thermal Infrared      |       11.5 – 12.51        |              100              |

</div>


#### 0.2.2. SPOT [^4]

Los satélites Spot (Satellite Pour l’Observation de la Terre: Satélite Para la Observación de la Tierra) son una serie de satélites de teledetección civiles de observación del suelo terrestre que han sido desarrollado por el CNES (Centro Nacional de Estudios Espaciales francés) en colaboración con Bélgica y Suecia. La primera versión de SPOT fue lanzada el 22 de febrero de 1986 (Ariane 1). SPOT 7 fue lanzado el 30 de junio de 2014. La resolución de las imágenes capturadas es de 2.5 a 20 metros dependiendo de la banda espectral y el modo de captura. https://earth.esa.int/eogateway/missions/spot


#### 0.2.3. Sentinel [^5]

Sentinel es un proyecto multi-satélite que está siendo desarrollado por la ESA (European Space Agency) en el marco del Programa Copérnico. Las misiones Sentinel incluyen satélites de radar y satélites de imágenes super-espectrales para la vigilancia terrestre, oceánica y atmosférica de la Tierra. La primera versión fue lanzada el 3 de abril de 2014, la versión 6 que incluye radar altimétrico fue lanzada el 21 de noviembre de 2020. La resolución de las imágenes capturadas es de 5 a 300 metros dependiendo de la banda espectral, el modo de captura, y la polarización. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/The_Sentinel_missions


#### 0.2.4. Ikonos [^6]

Los satélites comerciales Ikonos para la observación de la tierra, capturaban colecciones de imágenes multiespectrales y pancromáticas. La primera versión fue lanzada el 24 de septiembre de 1999 y la versión 2 fue lanzada en enero del 2000 y suspendida el 31 de marzo de 2016.  La resolución de las imágenes capturadas es de 1 a 4 metros dependiendo de la banda espectral y el modo de captura. https://www.esa.int/SPECIALS/Eduspace_ES/SEM776E3GXF_0.html


## 1. Imagen satelital regional - Landsat

Corresponde al mosaico de imágenes de satélite con resolución espacial mayor o igual a 10 metros, ortocorregido y/o georeferenciado, modo pancromático, multiespectral o hiperespectral. Puede estar en uno de los siguientes formatos (geotiff, img, grid, ecw). En el modelo de datos ANLA, el archivo o imagen se debe identificar con el prefijo _ImaSatReg_ seguido de la fecha de toma (mes, día, año) a la que corresponde, p. ej., _ImaSatReg01012015_.

1. En QGIS, abra el mapa _/map/CaseStudy.qgz_ y guarde como  _/map/RemoteSensingDL.qgz_. Exporte la capa _AreaProyecto_ como un archivo shapefile en _/shp/AreaProyecto.shp_ para actualizar la extensión de esta capa.

<div align="center"><img src="graph/QGIS_Export.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. Con la herramienta _Layer Tools / Extract layer extent_, obtenga el polígono envolvente del área del proyecto, guarde como _/shp/LayerExtentAreaProyecto9377.shp_.

<div align="center"><img src="graph/QGIS_ExtractLayerExtent.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Con la herramienta _Vector General / Reproject layer_, reproyecte la capa al CRS 4326, guarde como _/shp/LayerExtentAreaProyecto4326.shp_.

<div align="center"><img src="graph/QGIS_Reproject.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. Desde el explorador de su sistema operativo, comprima el shapefile creado como _/shp/LayerExtentAreaProyecto4326.zip_.

<div align="center"><img src="graph/Windows_LayerExtentZip.jpg" alt="rcfdtools" width="100%" border="0" /></div>

5. Ingrese al portal https://earthexplorer.usgs.gov/ y realice el Login con su cuenta de usuario. En la pestaña _Search Criteria_, importe el comprimido del archivo shapefile que contiene el límite de la zona de estudio, defina el rango de fechas 02/27/2026 a 02/27/2026 y cobertura de nubes de hasta el 30%.

<div align="center"><img src="graph/Chrome_EarthExplorer1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

6. En la pestaña _Datasets_ seleccione _Landsat / Landsat Collection 2 Level-1 / Landsat 8-9 OLI-TIRS C2 L1_.

<div align="center"><img src="graph/Chrome_EarthExplorer2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

7. En la pestaña _Additional Criteria_ establezca el WRS Path 008, WRS Row 056 a 057 y el Satellite 9.

<div align="center"><img src="graph/Chrome_EarthExplorer3.jpg" alt="rcfdtools" width="100%" border="0" /></div>

8. En la pestaña _Results_, agregue los overlay para visualización de las imágenes.

<div align="center"><img src="graph/Chrome_EarthExplorer4.jpg" alt="rcfdtools" width="100%" border="0" /></div>

9. Descargue los paquetes completos de las dos imágenes encontradas. En [Releases](https://github.com/rcfdtools/R.IAMB/releases) del curso IAMB encontrará estas imágenes.

<div align="center"><img src="graph/Chrome_EarthExplorer5.jpg" alt="rcfdtools" width="100%" border="0" /></div>

10. En la carpeta _/data/Landsat9_ descomprima en dos subcarpetas los archivos contenidos en cada comprimido descargado.

<div align="center"><img src="graph/Windows_Landsat9Folder.jpg" alt="rcfdtools" width="100%" border="0" /></div>

11. En QGIS, y con la herramienta _Raster Miscellaneous / Build Virtual Raster_, cree una imagen compuesta en falso color a partir de las bandas espectrales 4,3,2. Este procedimiento se realiza independiente para las dos imágenes descargadas. Guarde como _/grid/LC09_L2SP_008056_20260227_B4B3B2.vrt_ y /grid/LC09_L2SP_008057_20260227_B4B3B2.vrt. Al finalizar, establezca desde las propiedades de visualización el brillo de las imágenes en 50%.

> En la pestaña _Parameters_, marque la casilla _Place each input file into a separate band_.
> En la opción _Input Layers_ de la herramienta _Buil Virtual Raster_, deberá ordenar las bandas en la secuencia B4, B3, B2.

<div align="center"><img src="graph/QGIS_BuildVirtualRaster1.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_BuildVirtualRaster2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

12. Con la herramienta _Raster Miscellaneous / Merge_, combine las dos imágenes multibanda en una única imagen multibanda. Guarde primero como una capa temporal y luego exporte en formato TIFF como _/grid/LC09_L2SP_20260227_B4B3B2.tif_ reproyectando al CRS 9377.

<div align="center"><img src="graph/QGIS_RasterMerge.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_RasterMerge1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

13. Utilizando la herramienta _Vector Geometry / Buffer_, cree un polígono con aferencia de 1000 metros alrededor del polígono _LayerExtentAreaProyecto9377_, guarde como _/shp/LayerExtentAreaProyecto9377Buffer100m.shp_.

<div align="center"><img src="graph/QGIS_Buffer.jpg" alt="rcfdtools" width="100%" border="0" /></div>

14. Utilizando la herramienta _Raster Extraction / Clip Raster by Extent_, recorte la imagen y guarde como _/grid/LC09_L2SP_20260227_B4B3B2_Clip.tif_.

<div align="center"><img src="graph/QGIS_ClipRasterByExtent.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_ClipRasterByExtent1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Opcionalmente, puede recortar la imagen hasta el límite de la zona de estudio.


## 2. Imagen satelital regional - Sentinel

1. En QGIS, instale el complemento o Plugin _Sentinel 2 Image Downloader_. 

<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. En la pestaña Download Footprints y a partir del _Layer Extent_ de la capa _AreaProyecto_ y para la fecha 26/02/2026, genere los límites o Foot Print de las imágenes Sentinel disponibles en Copernicus y agreguelas al mapa. 

<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader1.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Edite la capa _footprints_ eliminando los polígonos o límites de imágenes no requeridas.

<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader3.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. En la pestaña _Download Images_, ingrese sus credenciales de https://dataspace.copernicus.eu/, seleccione el archivo editado _Footprints_. En _OPTIONS_, seleccione TCI (10M) - RGB image e inicie la descarga.

<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader4.jpg" alt="rcfdtools" width="100%" border="0" /></div>

5. Copie el contenido descargado en la carpeta _/data/Sentinel2/20260226_ y agregue al mapa. Para crear una imagen extendida, también descargue y agregue _T18NXL_20260226T152651_TCI_10m_.

<div align="center"><img src="graph/QGIS_PluginSentinel2ImageDownloader5.jpg" alt="rcfdtools" width="100%" border="0" /></div>

6. Con la herramienta _Raster Miscellaneous / Merge_, combine las 4 imágenes multibanda en una única imagen multibanda. Guarde primero como una capa temporal y luego exporte en formato TIFF como _/grid/Sentinel2_20260226.tif_ reproyectando al CRS 9377.

<div align="center"><img src="graph/QGIS_RasterMerge2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

7. Utilizando la herramienta _Raster Extraction / Clip Raster by Extent_, recorte la imagen y guarde como _/grid/Sentinel2_20260226_Clip.tif_.

<div align="center"><img src="graph/QGIS_ClipRasterByExtent2.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_ClipRasterByExtent3.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Opcionalmente, puede recortar la imagen hasta el límite de la zona de estudio.


## 3. Modelo digital de superficie - DSM

Corresponde al Modelo Digital de Superficie (incluye elementos de la cobertura terrestre como por ejemplo cobertura vegetal, edificaciones, etc.), en escala de grises, donde cada celda o pixel contiene el valor de elevación en metros sobre el nivel del mar. Puede estar en uno de los siguientes formatos (geotiff, img, grid, ecw). En el modelo de datos ANLA, el archivo o modelo digital de superficie se debe identificar como _DSM_.

1. En QGIS, instale el complemento o _Plugin_ _Open Topography_.

<div align="center"><img src="graph/QGIS_PluginOpenTopography.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. Ingrese al portal https://opentopography.org y obtenga la API key de su cuenta de usuario.

<div align="center"><img src="graph/Chrome_OpenTopographyAPIKey.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. Ingrese la API key en el Plugin, defina como región de descarga el límite de la capa _LayerExtentAreaProyecto9377Buffer1000m_ y descargue el mapa Copernicus de 30 metros de resolución, guarde como _/dem/COP30.tif_.

<div align="center"><img src="graph/QGIS_PluginOpenTopography1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Exporte y reproyecte el DSM cómo _/dem/COP30_9377.tif_.

<div align="center"><img src="graph/QGIS_SaveRasterLayerAs.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. Cambie la representación del DSM como falso Hillshade aplicando un facto Z de 3.

<div align="center"><img src="graph/QGIS_FalseHillshade.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_FalseHillshade1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Descargue, procese y analice para el área de proyecto, los demás DEM disponibles en Open Topography.


## 4. Modelo digital de pendientes - MDPendiente

Corresponde a la superficie o Modelo Digital de Pendientes, en escala de grises, donde cada celda o pixel contiene el valor de pendiente en porcentaje. Puede estar en uno de los siguientes formatos (geotiff, img, grid, ecw). En el modelo de datos ANLA, el archivo o modelo se debe identificar como _Pendiente_.

1. 



:pencil2:**Tarea:** Descargue, procese y analice este mapa para el área de proyecto.


## Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/composite-bands.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/clip.htm
* [Download Satellite Data using QGIS | SCP Plugin | Landsat | Sentinel | MODIS](https://www.youtube.com/watch?v=S8nyq_GMpfA)



## Control de versiones

| Versión    | Descripción                                 | Autor                                      | Horas |
|------------|:--------------------------------------------|--------------------------------------------|:-----:|
| 2026.03.05 | Versión inicial con alcance de la actividad | [rcfdtools](https://github.com/rcfdtools)  |   6   |



##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../LandSoil/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../XXXX/Readme.md) |
|-------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|----------------------------------|

[^1]: https://learn.arcgis.com/es/arcgis-imagery-book/chapter2/
[^2]: http://mappinggis.com/2015/05/como-descargar-imagenes-landsat/
[^3]: https://es.wikipedia.org/wiki/Landsat
[^4]: https://es.wikipedia.org/wiki/SPOT
[^5]: https://es.wikipedia.org/wiki/Sentinel_(sat%C3%A9lite)
[^6]: https://en.wikipedia.org/wiki/Ikonos 

