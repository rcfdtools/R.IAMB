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

Área del proyecto objeto de solicitud de licencia. Ej.: Campo, Bloque, Área de Interés, Estación o Refinería (sector de hidrocarburos), Puerto, Aeropuerto, Infraestructura Marina y Costera, Infraestructura Fluvial, Planta de Tratamiento, Relleno Sanitario (sector infraestructura), Hidroeléctricas, Termoeléctricas, Subestaciones, Presas, Represas o Embalses (sector energía), Explotación Minera (sector minería), Plantas de Formulación y/o Producción, Laboratorios, Centros Experimentales (sector agroquímicos).

La capa _AreaProyecto_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene un dominio asociado:

<div align="center"><img src="graph/ANLA_AreaProyecto.jpg" alt="rcfdtools" width="100%" border="0" /></div>

El dominio _Dom_Sector_, contiene los siguientes códigos:

<div align="center"><img src="graph/ANLA_Dom_Sector.jpg" alt="rcfdtools" width="25%" border="0" /></div>

1. En la carpeta [/gdb](../../file/gdb) descomprima la geodatabase [BD_ANLA_MAGNA_NACIONAL.gdb](../../file/data/ANLA/magna_origen_nacional.zip) y cargue al mapa la capa /T_33_Proyecto/AreaProyecto. Active el modo de edición, copie y pegue el polígono correspondiente a la SZH 2120.

<div align="center"><img src="graph/QGIS_AreaProyecto1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. Como observa, luego de copiar el polígono, no se homologan automáticamente los campos requeridos por la capa _AreaProyecto_ del ANLA, incluya manualmente los siguientes atributos:

<div align="center"><img src="graph/QGIS_AreaProyecto2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Para la rotulación establezca la siguiente configuración de saltos de línea:

<div align="center"><img src="graph/QGIS_AreaProyecto3.jpg" alt="rcfdtools" width="70%" border="0" /></div>

3. En el campo `AREA_HA`, calcule el área geodésica en hectáreas, obtendrá que el área de estudio corresponde a 592810.46 ha.

Expresión: `$area/10000`

Incluya en el rótulo el área calculada.

Expresión: `"PROYECTO"  ||  '\n'  ||  'A (ha): ' || round( "AREA_HA", 2)`

> Debido al tamaño espacial del polígono del área de estudio, realizaremos los cálculos de área geodésica y no los de área planar `area($geometry)`.

<div align="center"><img src="graph/QGIS_FieldCalculator.jpg" alt="rcfdtools" width="70%" border="0" /></div>

Guarde y detenga el modo de edición de esta capa.


## 3. Incorporación a capa ANLA: AreaInfluencia

Luego de definida el Área de Proyecto, es necesario establecer el Área de Influencia que para el caso de estudio corresponderá a todos los polígonos perimetrales o próximos al área de proyecto y su propia área.

El Área o Áreas de Influencia del Proyecto, comprende la definición del área o de las áreas de influencia, de acuerdo con los impactos identificados en cada una de las etapas del proyecto y las características del espacio geográfico. Pueden presentarse áreas de influencia por "Medio", "Componente" o "Grupo de Componentes".

La capa _AreaProyecto_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene un dominio asociado:

<div align="center"><img src="graph/ANLA_AreaInfluencia.jpg" alt="rcfdtools" width="100%" border="0" /></div>

El dominio _Dom_Sector_, contiene los siguientes códigos:

<div align="center"><img src="graph/ANLA_Dom_AreaInfluencia.jpg" alt="rcfdtools" width="25%" border="0" /></div>

1. Cargue al mapa la capa /T_33_Proyecto/AreaInfluencia. Desactive el filtro realizado en la capa _h_znhd_2022_100K_. Podrá observar que existen múltiples sub-zonas hidrográficas alrededor del polígono de la zona de estudio. 

<div align="center"><img src="graph/ANLA_AreaInfluencia1.jpg" alt="rcfdtools" width="80%" border="0" /></div>

2. Utilizando la herramienta _Select By Location_, seleccione todos los polígonos de las SZH que se intersecan con el polígono del área de estudio. Podrá observar que de los 316 polígonos han sido seleccionados 10 polígonos.

<div align="center"><img src="graph/ANLA_SelectByLocation.jpg" alt="rcfdtools" width="80%" border="0" /></div>

3. Active el modo de edición de la capa _AreaInfluencia_, copie y pegue los polígonos seleccionados.

<div align="center"><img src="graph/ANLA_AreaInfluencia2.jpg" alt="rcfdtools" width="80%" border="0" /></div>

4. Utilizando la herramienta _Merge Selected Features_, disponible en la barra de herramientas _Advanced Digitizing Toolbar_, combine los 10 polígonos en un único polígono.

<div align="center"><img src="graph/ANLA_MergeSelectedFeatures.jpg" alt="rcfdtools" width="80%" border="0" /></div>

5. Asigne y/o calcule los atributos requeridos.

<div align="center"><img src="graph/ANLA_AreaInfluencia3.jpg" alt="rcfdtools" width="80%" border="0" /></div>


## 3. Límites de autoridades ambientales

Las Corporaciones Autónomas Regionales y de Desarrollo Sostenible, son entes corporativos de carácter público, creados por la ley, integrados por las entidades territoriales que por sus características constituyen geográficamente un mismo ecosistema o conforman una unidad geopolítica, biogeográfica o hidrogeográfica, dotados de autonomía administrativa y financiera, patrimonio propio y personería jurídica, encargados por la ley de administrar, dentro del área de su jurisdicción el medio ambiente y los recursos naturales renovables y propender por su desarrollo sostenible, de conformidad con las disposiciones legales y las políticas del Ministerio del Medio Ambiente. [^2]

Enlaces para descarga:

* https://datos.icde.gov.co/datasets/0fd08ce937034387b33699e8165ffc84
* https://siac-datosabiertos-mads.hub.arcgis.com/datasets/0fd08ce937034387b33699e8165ffc84

1. Cargue al proyecto la capa de [Límites autoridades ambientales de Colombia (versión 2022)](../../file/data/MADS/Lim_AA_25k_2022.zip) del Ministerio de Ambiente y Desarrollo Sostenible.

> La capa contiene de los límites de las Corporaciones Autónomas Regionales, construidos con base en la capa de límites municipales a escala 1:25000 publicados por el Instituto Geográfico Agustí Codazzi – IGAC del año 2018 y de la sinergia con la propuesta de los límites de las corporaciones Autónomas Regionales construido por el IDEAM. Cubre toda la extensión continental del territorio colombiano, además del archipiélago de San Andrés y Providencia.

<div align="center"><img src="graph/MADS_AutoridadAmbiental.jpg" alt="rcfdtools" width="80%" border="0" /></div>




Tomando como referencia el límite de la subzona hidrográfica 2120 del IDEAM, las 3 autoridades ambientales con influencia geográfica directa sobre la cuenca del Río Bogotá son:

<div align="center"><img src="file/graph/ArcGISPro_Layer_AutoridadAmbiental2.png" alt="R.SIGE" width="90%" border="0" /><br><sub>Autoridades ambientales con influencia geográfica sobre la cuenca del Río Bogotá (norte hacia arriba).</sub></div><br><br>

<div align="center">

| Autoridad ambiental - AA | Nombre                                        | Área en cuenca (km²) | % en cuenca |  Área AA. (km²)  |   % AA.   |
|:-------------------------|:----------------------------------------------|:--------------------:|:-----------:|:----------------:|:---------:|
| (n/a)                    | (área no coincidente)                         |         7.29         |    0.12     |       7.29       |    100    |
| CAR                      | Corporación Autónoma Regional de Cundinamarca |       5331.94        |    89.87    |      18289       |   29.15   |
| CORPOGUAVIO              | Corporación Autónoma Regional del Guavio      |        209.56        |    3.53     |     3635.01      |   5.77    |
| SDA                      | Secretaria Distrital de Ambiente Bogotá       |        383.99        |    6.47     |      383.99      |    100    |
|                          | Σ                                             |       5932.79        |     100     |     22315.3      |     0     |

</div>

> _**% en cuenca**_: corresponde al porcentaje del área geodésica del límite de la autoridad ambiental, con respecto a toda la cuenca del Río Bogotá.   
> _**% AA.**_: corresponde al porcentaje del área geodésica del límite de la AA dentro de la cuenca del Río Bogotá, con respecto al área total de la AA.










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
[^2]: https://archivo.minambiente.gov.co/index.php/noticias/2067