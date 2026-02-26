<div align="center"><img alt="rcfdtools" src="../../file/graph/R.IAMB.svg" height="46px"></div>

# 2.3. Vectores - Medio abiótico - Suelos
Keywords: `land-soil` `land-conflict` `land-potential-use`

Descargue el Mapa de Suelos, vocación de uso y conflictos de uso de Colombia del IGAC y recorte hasta el límite del área del proyecto. Describa y explique los tipos de suelos presentes en la zona de estudio. Utilizando la herramienta de geoprocesamiento Intersect, combine el modelo de ocupación territorial MOT con las capas de suelos. A través de un resumen estadístico, obtenga por cada categoría del MOT, los tipos de suelos presentes, usos potenciales, conflictos de uso y sus áreas.  

<div align="center"><img src="graph/LandSoil.jpg" alt="rcfdtools" width="70%" border="0" /></div>


## Objetivos

* Estudiar los tipos de suelos presentes en la zona de estudio, sus vocaciones principales y los conflictos identificados por la autoridad catastral nacional.
* Calcular la distribución porcentual de los diferentes suelos identificados en la zona de estudio.


## Requerimientos

Archivos, actividades previas, lecturas y herramientas requeridas para el desarrollo de esta actividad:

<div align="center">

| Requerimiento                                                                                                 | Descripción                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [:toolbox:Herramienta](https://qgis.org/)                                                                     | QGIS 3.44 o superior.                                                                                                |
| [:date:magna_origen_nacional.zip](../../file/data/ANLA/magna_origen_nacional.zip)                             | Geodatabase ANLA Magna Origen Nacional.                                                                              |
| [:date:diccionario_datos_geograficos_anla.xlsx](../../file/data/ANLA/diccionario_datos_geograficos_anla.xlsx) | Diccionario de datos geográficos ANLA.                                                                               |
| [:round_pushpin:qgis_basemaps.py](../../file/src/qgis_basemaps.py)                                            | Script en Python para inclusión de mapas base XYZ en QGIS por [opengeos](https://github.com/opengeos/qgis-basemaps). |
| [:round_pushpin:qgis_clip_dissolve_reproject_adp.py](../../file/src/qgis_clip_dissolve_reproject_adp.py)      | Script en Python recortar, disolver, reproyectar y calcular distribuciones porcentuales de área.                     |

</div>


## 1. Mapa de suelos de la zona de estudio

El mapa de suelos del Departamento de Cundinamarca, ha sido creado por el [Instituto Geográfico Agustín Codazzi](https://www.igac.gov.co/) - Subdirección de Agrología - Grupo Interno de Trabajo Geomática - Carrera 30 # 48 - 51 – Sede Central, Bogotá D.C, Departamento de Cundinamarca, 111321, República de Colombia. Autor: german.alvarez@igac.gov.co (Subdirector de Agrología), +57 1 3694100 Ext. 91007

Este mapa temático representa la distribución de las características del suelo, determinadas mediante el levantamiento general de suelos del departamento de Cundinamarca a escala 1:100.000, publicado en el año 2000. Suministra información importante acerca del recurso suelo, a través de la descripción e interpretación de sus ambientes edafogenéticos, sus características físicas, químicas, mineralógicas y morfológicas, su taxonomía y distribución espacial, como base para la determinación de sus potenciales productivos, describiendo las limitantes de uso.

Los Levantamientos Generales de Suelos de los departamentos del Territorio Colombiano suministran información importante acerca del recurso suelo; a través de la descripción e interpretación de su génesis, características físicas, químicas, mineralógicas, morfológicas, taxonomía y distribución, como base para la determinación de sus potencialidades y limitaciones de uso.

**Estirpe**: la generación del Mapa Digital de Suelos, para el levantamiento general de suelos, escala 1:100.000, se realizó a partir de los parámetros definidos por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi, para el objeto: Suelos. Para la elaboración del levantamiento, el GIT de Levantamientos de Suelos y Aplicaciones Agrológicas, en la etapa de precampo recopiló información secundaria proveniente de estudios de suelos anteriores, e investigaciones sobre los factores formadores del suelo, tales como clima, geología y geomorfología, los cuales se interpretan con el apoyo de insumos de cartografía, sensores remotos y fotointerpretación. Posteriormente, en la etapa de campo se realiza la descripción de las observaciones tipo cajuelas o barrenaje, y calicatas, ajuste a las líneas de interpretación y recolección de muestras que serán analizadas por el Laboratorio Nacional de Suelos. La sistematización y georreferenciación de esta información sirve de apoyo fundamental para el trazo de las líneas de suelos, que son digitalizadas sobre cartografía base, imágenes de sensores remotos, modelos digitales de elevación, entre otros. Finalmente en la etapa de poscampo se consolidó la leyenda de suelos del estudio, la cartografía temática con sus diferentes atributos y la memoria técnica respectiva. 

* Fuente: https://www.colombiaenmapas.gov.co/, buscar como _Suelos Cundinamarca_
* Extensión espacial: Departamento de Cundinamarca - Colombia - Suramérica
* Escala: 1:100000
* Sistema de referencia de coordenadas: 3116
* Licencia: este producto adopta la licencia pública internacional de Reconocimiento-CompartirIgual 4.0 de Creative Commons, Creative Commons attribution – ShareAlike 4.0 Internacional. Por tal razón, nuevos productos y servicios derivados de su reutilización deben ser también licenciados bajo las mismas condiciones de uso y disponibilidad que habilitó la licencia antes mencionada. Lo anterior, sin perjuicio de los derechos de autor y propiedad intelectual del Instituto Geográfico Agustín Codazzi, con base en la Ley 23 de 1982 y demás normas concordantes. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es)

1. Desde el portal de https://www.colombiaenmapas.gov.co/, busque y descargue en formato GDB, el mapa de suelos del Departamento de Cundinamarca, guarde y descomprima en la ruta `/data/IGAC/SUELOS_CUNDINAMARCA_100K.gdb`.

<div align="center"><img src="graph/ColombiaMapas_Suelos100K.png" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS, abra el mapa de proyecto _CaseStudy.qgz_, creado previamente y guarde como _/map/LandSoil.qgz_ y establezca el CRS 9377. Agregue al mapa la capa _SUELOS_CUNDINAMARCA_VF_, ajuste la simbología a valores únicos representando el campo de atributos `UCS_F` y rotule a partir del mismo campo.  

<div align="center"><img src="graph/QGIS_AddLayer1.png" alt="rcfdtools" width="100%" border="0" /></div>

3. Utilizando el script de Python [qgis_clip_dissolve_reproject_adp.py](../../file/src/qgis_clip_dissolve_reproject_adp.py), recorte, disuelva, reproyecte y calcule la distribución porcentual de los suelos contenidos dentro de la zona de estudio. Podrá observar que dentro del área del proyecto existen 97 tipos de suelos diferentes. En la tabla de atributos de la capa disuelta y reproyectada, elimine los atributos `AREA`, `SHAPE_Leng` y `SHAPE_Area`.

> Antes de ejecutar el script, establezca en Settings / Options / Processing / General / Invalid features filtering / Do not filter.

Parámetros generales
```
input_layer_path = 'C:/IAMB/data/IGAC/SUELOS_CUNDINAMARCA_100K.gdb|layername=SUELOS_CUNDINAMARCA_VF'
overlay_layer_path = 'C:/IAMB/gdb/BD_ANLA_MAGNA_NACIONAL.gdb|layername=AreaProyecto'
output_file_clip_name = 'SuelosVFAreaProyecto'
dissolve_field = 'UCS_F'
```

<div align="center"><img src="graph/QGIS_Clip1.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_Clip2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

> Tenga en cuenta que debido a las escalas de digitalización y versión, el límite espacial del mapa de suelos de Cundinamarca puede no cubrir completamente el área del proyecto.

Cree una gráfica de barras representando las diferentes unidades de suelo, podrá observar que _RLQa_ correspondiente a _Mantos de ceniza volcánica sobre depósitos clásticos hidrogénicos_, es la mayor clase con un área de 41043.27 ha, correspondiente al 6.93 % de la superficie de toda la cuenca en estudio.  

<div align="center"><img src="graph/QGIS_Clip3.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. Con la herramienta de estadísticas por categorías, cree tablas y gráficos de barras representando las diferentes variables categóricas presentes en la capa de suelos dentro de la zona de estudio. 

Por paisaje, montaña presenta la mayor área.  
<div align="center"><img src="graph/QGIS_Chart1.jpg" alt="rcfdtools" width="100%" border="0" /></div><br>
<div align="center"><img src="graph/QGIS_Chart2.jpg" alt="rcfdtools" width="100%" border="0" /></div><br>

:pencil2:**Tarea:** Homologue y cargue el análisis realizado en la capa _Suelo_ del modelo ANLA.

<div align="center"><img src="graph/ANLA_Suelo.jpg" alt="rcfdtools" width="100%" border="0" /></div>


## 2. Vocación de uso

El mapa de Vocación de Uso de las tierras del IGAC del año 2013, se determina mediante matrices de decisión que incluyen indicadores e índices de su estado. En los atributos geográficos considerados se encuentra el clima y la pendiente. Entre los de los suelos sobresalen la erosión, humedad, granulometría, pedregosidad, profundidad efectiva, fertilidad y salinidad. Esta clasificación comprende 5 clases: agrícola, ganadera, agroforestal, forestal y de conservación/recuperación. En cada una se establece el uso principal que debe tener. Este producto es generado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi - IGAC, para el territorio nacional, el cual fue publicado en la obra Suelos y Tierras de Colombia 2016 a escala 1:100.000.

El objetivo principal de la vocación es la determinación del uso más apropiado que puede soportar cada uno de los suelos del país, propendiendo por una producción sostenible y sin deterioro de los recursos naturales. Son dos niveles categóricos los tenidos en cuenta en el presente estudio; el primero corresponde a la vocación general de uso de la tierra y, el segundo, como subdivisión del primero, hace referencia a los usos principales recomendados.

**Estirpe**: con la finalidad de establecer el mejor uso de las tierras, se analizan y evalúan una serie de características biofísicas estables en el tiempo y en el espacio; que influyen en la selección y desempeño de los usos agropecuarios y forestales, principalmente, con requerimientos implícitos de protección y conservación de los recursos naturales. Por tanto, para la determinación del uso más apropiado que puede soportar cada uno de los suelos, se tienen en cuenta algunas de sus propiedades, difícilmente modificables por el hombre en un corto y mediano plazo que ejercen fuerte influencia en las actividades productivas antrópicas; estos criterios de determinación del uso principal para cada uno de los suelos hacen referencia a factores climáticos, pendiente, erosión, factores de humedad, pedregosidad y factores intrínsecos al suelo como la profundidad efectiva, grupo textural, fertilidad, salinidad, porcentaje de saturación de sodio, aluminio y carbono orgánico. A partir de la anterior información y estableciendo combinación de indicadores; se generan los índices del estado de las tierras, los cuales permiten tipificar como están conformadas y cuáles son sus calidades, obteniendo así, los índices de impacto con los cuales se puede medir el grado de deterioro que presenta cada una de las unidades de tierra. Los indicadores e índices a tener en cuenta en el proceso de evaluación están referidos a factores climáticos (precipitación, temperatura, distribución de las lluvias), factores del relieve como la pendiente y geomorfología, factores externos a los suelos como la erosión, la humedad (drenaje natural e inundaciones y encharcamientos) y la pedregosidad (porcentaje de fragmentos en superficie) y factores intrínsecos al suelo (profundidad efectiva, grupo textural, fertilidad, salinidad, porcentaje de saturación de sodio, de aluminio, de carbono orgánico y fragmentos de roca en el suelo); obteniendo como resultado la vocación subdividida en cinco (5) clases las cuales se dividen a su vez en treinta y cinco (35) subclases: (Agrícola: Cultivos transitorios intensivos de clima cálido, Cultivos transitorios intensivos de clima medio, Cultivos transitorios intensivos de clima frío, Cultivos transitorios semi intensivos de clima cálido, Cultivos transitorios semi intensivos de clima medio, Cultivos transitorios semi intensivos de clima frío, Cultivos permanentes intensivos de clima cálido, Cultivos permanentes intensivos de clima medio, Cultivos permanentes intensivos de clima frío, Cultivos permanentes semi intensivos de clima cálido, Cultivos permanentes semi intensivos de clima medio, Cultivos permanentes semi intensivos de clima frío); (Ganadera: Pastoreo intensivo de clima cálido, Pastoreo intensivo de clima medio, Pastoreo intensivo de clima frío, Pastoreo semi intensivo de clima cálido, Pastoreo semi intensivo de clima medio, Pastoreo semi intensivo de clima frío, Pastoreo extensivo de clima cálido, Pastoreo extensivo de clima medio, Pastoreo extensivo de clima frío, Pastoreo extensivo de clima muy frío); (Agroforestal: Agrosilvícola con cultivos transitorios, Agrosilvícola con cultivos permanentes, Agrosilvopastoril con cultivos transitorios, Agrosilvopastoril con cultivos permanentes, Silvopastoril); (Forestal: Producción de clima cálido, Producción de clima medio, Producción de clima frío, Producción de clima muy frío, Protección – producción); (Conservación: Protección, Humedales, Conservación y recuperación).

Este mapa puede ser obtenido de https://www.colombiaenmapas.gov.co/ ingresando la cadena de búsqueda _Vocación de Uso. Territorio Nacional_.

<div align="center"><img src="graph/ColombiaMapas_VocacionUso100K.png" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Descargue, procese y analice este mapa para el área de proyecto.


## 3. Conflictos de uso

El mapa de conflictos de uso de las tierras del IGAC del año 2016, resulta de las discrepancias entre el uso que hace la población del medio natural y el que debería tener, de acuerdo con sus potencialidades y restricciones ambientales. El IGAC, a través de la Subdirección de Agrología, ha venido investigando durante los últimos 25 años, los criterios y metodologías tendientes a establecer el uso y las prácticas de manejo que deben tener los suelos y tierras del país, buscando su productividad sostenible en función de la oferta y demanda ambientales. Su mayor dedicación se ha concentrado en aspectos agrícolas, ganaderos, agroforestales, forestales y de conservación/recuperación de suelos y aguas. Este producto es generado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi - IGAC, para el territorio nacional, el cual fue publicado en la obra Suelos y Tierras de Colombia 2016 a escala 1:100.000.

Este mapa puede ser obtenido de https://www.colombiaenmapas.gov.co/ ingresando la cadena de búsqueda _Conflictos de uso de la tierra año 2012. Territorio nacional_.

<div align="center"><img src="graph/ColombiaMapas_ConflictosUso100K.png" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Descargue, procese, homologue y cargue el análisis requerido en la capa _ConflictoUsoSuelo_ del modelo ANLA.

<div align="center"><img src="graph/ANLA_ConflictoUsoSuelo.jpg" alt="rcfdtools" width="100%" border="0" /></div>


## 4. Uso actual del suelo

Corresponde al uso que se le está dando actualmente al suelo y está directamente relacionado con la cobertura de la tierra. Este análisis puede ser realizado a partir de unidades prediales combinando con la información del registro 1 de catastro, en los que se encuentra la destinación económica.

* Clase complementaria: [Análisis de destinaciones económicas IGAC (creación de dominios)](https://github.com/rcfdtools/R.SIGE/blob/main/activity/LandUseIGAC/Readme.md)
* Predios nacionales año 2020: https://github.com/rcfdtools/R.GISMobile
* [Registro 1 catastral Cundinamarca a 20231231](../../file/data/IGAC/25_Cundinamarca_Registro1_20231231.zip).

:pencil2:**Tarea:** Descargue, procese, homologue y cargue el análisis requerido en la capa _UsoActualSuelo_ del modelo ANLA.

<div align="center"><img src="graph/ANLA_UsoActualSuelo.jpg" alt="rcfdtools" width="100%" border="0" /></div>


## 5. Capacidad de uso de tierra

El mapa de _Capacidad de uso de las tierras de la República de Colombia a escala 1:100.000_ del Instituto Geográfico Agustín Codazzi - IGAC, contiene la Clasificación por Capacidad de Uso está basada en la interpretación de las Unidades Cartográficas que integran el mapa de suelos del país (escala 1:100.000). La interpretación busca establecer las restricciones y potencialidades biofísicas de las tierras. Los criterios para evaluarlas y sus rangos de variación se adaptaron al país; a partir de la clasificación originada en los Estados Unidos; a través de la experiencia proporcionada durante más de cinco décadas de aplicación. La clasificación propende por la utilización correcta de las tierras del país y; al estar espacializada; constituye un criterio imprescindible en los planes de ordenamiento territorial; en la toma de decisiones con el fin de reducir su uso irracional y en la planificación de sus recursos naturales. Dado que el producto integra varios insumos, se visualiza la fecha de insumo correspondiente al más reciente utilizado durante su elaboración.

Servicio: https://www.colombiaenmapas.gov.co/?u=0&t=43&servicio=1776

<div align="center"><img src="graph/ColombiaMapas_CapacidadUsoTierra100K.jpg" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Descargue, procese, homologue y cargue el análisis requerido en la capa _CapacidadUsoTierra_ del modelo ANLA.

<div align="center"><img src="graph/ANLA_CapacidadUsoTierra.jpg" alt="rcfdtools" width="100%" border="0" /></div>


## 6. Suelos en las áreas de influencia de los humedales de Colombia, región Andina

Este producto es resultado de la ejecución del contrato 13-13-014-091PS, firmado entre el Instituto Geográfico Agustín Codazzi (IGAC) y el Instituto Humboldt, en el marco del convenio 005 (13-014) entre el Instituto Humboldt y el Fondo Adaptación. Muestra las unidades de capacidad de uso de tierras generadas para los suelos de los humedales de la región Andina, mediante el levantamiento semidetallado del suelo en las áreas de influencia de los humedales de Colombia en 2015.

* Servicio: https://www.colombiaenmapas.gov.co/?u=0&t=43&servicio=805
* Entidad: Instituto de Investigación de Recursos Biológicos Alexander von Humboldt - IvAH
* Nivel de detalle: 1:25.000
* Fecha de Elaboración: 29-11-2016
* Fecha de Insumos: 30-12-2015
* Licencia: CC BY 4.0

<div align="center"><img src="graph/ColombiaMapas_SuelosHumedales25K.jpg" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Descargue, procese y analice este mapa para el área de proyecto.


## Referencias

* [Mapa Digital de Suelos del Departamento de Cundinamarca, República de Colombia. Escala 1:100.000. Año 2001.](https://metadatos.icde.gov.co/geonetwork/srv/api/records/f7c184ea-8abb-45a5-9cf2-1f88981760b6)
* https://www.colombiaenmapas.gov.co/
* https://geoportal.igac.gov.co/contenido/datos-abiertos-agrologia
* https://www.datos.gov.co/dataset/vocaciondeusoterritorionacional/ip25-k55k/about_data


## Control de versiones

| Versión     | Descripción                                                | Autor                                      | Horas |
|-------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2026.02.26 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   6   |



##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../Geology/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../XXXX/Readme.md) |
|------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|----------------------------------|

[^1]: Cohen, K.M., Finney, S.C., Gibbard, P.L. y Fan, J.-X. (2013; actualizado) The ICS International Chronostratigraphic Chart. Episodes 36: 199-204. 
[^2]: 

