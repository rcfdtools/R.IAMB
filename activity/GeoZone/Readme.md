<div align="center"><img alt="rcfdtools" src="../../file/graph/R.IAMB.svg" height="46px"></div>

# 2.5. Medio socioeconómico - División geopolítica
Keywords: `state` `county` `remote-sensing` `clip-raster`

Descargue, cree un mosaico y recorte imágenes satelitales hasta el límite de la zona de estudio.

<div align="center"><img src="graph/RemoteSensingDL.jpg" alt="rcfdtools" width="70%" border="0" /></div>


## Objetivos

* 


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


## 1. Departamentos

Caracterización de los componentes socioeconómicos a escala departamental. En los casos en que la información que se requiere en detalle deba ser levantada según el tipo de estudio y términos de referencia, y que por algún motivo no pueda ser presentada, los campos numéricos se deben diligenciar con el número 999 y la justificación de la no presentación de la información se debe diligenciar en el campo de observaciones. En los campos alfanuméricos se debe presentar la justificación en el mismo campo.

La capa _Departamento_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene varios dominios asociados:

<div align="center"><img src="graph/ANLA_Departamento.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Dominios: Dom_Departamento, Dom_MediosComu, Dom_MediosComu, Dom_MediosComu, Dom_Activ_Econo, Dom_Activ_Econo, Dom_Activ_Econo

> Consulte todas las propiedades requeridas en el diccionario de datos del ANLA.

1. Ingrese al portal de https://www.colombiaenmapas.gov.co/ y descargue la capa Shapefile de Departamentos de Colombia.

* Recurso: https://www.colombiaenmapas.gov.co/?u=0&t=29&servicio=609
* Entidad: Instituto Geográfico Agustín Codazzi - IGAC
* Resumen: Son entidades territoriales de la división política - administrativa del Estado, que agrupan municipios, distritos y áreas no municipalizadas; su definición no incluye las fronteras internacionales con otros países, tienen autonomía para la administración de los asuntos seccionales, planificación, promoción del desarrollo económico y social dentro de su territorio, en los términos establecidos por la Constitución y las leyes. Se representan sobre cartografía del IGAC acorde a lo establecido en la Ley 1447 de 2011 y su Decreto Reglamentario 1170 de 2015. Ahora bien, es de anotar que la información sobre límites departamentales está sujeta a las actualizaciones de los resultados de las operaciones administrativas de deslinde y las decisiones tomadas por los competentes (Asambleas departamentales y Congreso de la República).

<div align="center"><img src="graph/ColombiaMapas_Departamento.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS, abra el mapa _/map/CaseStudy.qgz_ y guarde como  _/map/GeoZone.qgz_. Cargue y rotule la capa [/data/IGAC/DepartamentosColombia20260306.shp](../../file/data/IGAC/DepartamentosColombia20260306.zip). Podrá observar que la zona de estudio se encuentra dentro del Departamento de Cundinamarca y que en los extremos nor-este y sur-oeste, los límites no son completamente coincidentes.

3. Para la generación del polígono requerido por el ANLA, utilice el polígono completo de la zona de estudio agregando los atributos requeridos.

<div align="center"><img src="graph/QGIS_Departamento.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_Departamento1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

:pencil2:**Tarea:** Homologue y cargue el análisis realizado en la capa correspondiente del modelo ANLA.


## 2. Municipios

Caracterización de los componentes socioeconómicos a escala municipal. En los casos en que la información que se requiere en detalle deba ser levantada según el tipo de estudio y términos de referencia, y que por algún motivo no pueda ser presentada, los campos numéricos se deben diligenciar con el número 999 y la justificación de la no presentación de la información se debe diligenciar en el campo de observaciones. En los campos alfanuméricos se debe presentar la justificación en el mismo campo.

La capa _Municipio_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene varios dominios asociados:

<div align="center"><img src="graph/ANLA_Municipio.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Dominios: Dom_Municipio, Dom_Departamento, Dom_MediosComu, Dom_MediosComu, Dom_MediosComu, Dom_Activ_Econo, Dom_Activ_Econo, Dom_Activ_Econo.

> Consulte todas las propiedades requeridas en el diccionario de datos del ANLA.

1. Ingrese al portal de https://www.colombiaenmapas.gov.co/ y descargue la capa Shapefile de Municipios, Distritos y Áreas no municipalizadas de Colombia.

* Recurso: https://www.colombiaenmapas.gov.co/?u=0&t=29&servicio=610
* Entidad: Instituto Geográfico Agustín Codazzi - IGAC
* Resumen: Entidades territoriales fundamentales de la división político y administrativa del Estado, integran los departamentos y su definición, no involucra las fronteras internacionales con otros países. Tienen autonomía política, fiscal y administrativa dentro de los límites que, señalados en la Constitución y las leyes, cuya finalidad es el bienestar general y el mejoramiento de la calidad de vida de la población en su respectivo territorio. Se representan sobre cartografía del IGAC, acorde a lo establecido en la Ley 1447 de 2011 y su Decreto Reglamentario 1170 de 2015. Para el caso de los Distritos, la definición y modificación de sus límites está estipulado en la Ley 1617 de 2013. Las áreas No Municipalizadas, hacen parte de la división territorial, pero no son entidades territoriales (artículo 285 y 286 de la Constitución Política de Colombia, 1991); la categorización de cada municipio se establece de conformidad con la Ley 617 de 2000. La información sobre los límites municipales, está sujeta a las actualizaciones de los resultados de las operaciones administrativas de deslinde y las decisiones tomadas por los competentes (Asambleas departamentales y Congreso de la República).

<div align="center"><img src="graph/ColombiaMapas_Municipio.jpg" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS cargue y rotule la capa [/data/IGAC/MunicipiosColombia20260306.shp](../../file/data/IGAC/MunicipiosColombia20260306.zip). Podrá observar que la zona de estudio interseca o contiene múltiples municipios.

<div align="center"><img src="graph/QGIS_Municipio.jpg" alt="rcfdtools" width="100%" border="0" /></div>

3. Utilizando la herramienta _Vector Selection / Select by location_, seleccione todos los municipios que intersecan el área de estudio. Podrá observar que se han seleccionado 69 municipios.

<div align="center"><img src="graph/QGIS_SelectByLocation.jpg" alt="rcfdtools" width="100%" border="0" /></div>

4. Exporte y re-proyecte los municipios seleccionados, guarde como /shp/MunicipiosAreaProyecto.shp.

<div align="center"><img src="graph/QGIS_SaveVectorLayerAs.jpg" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_SaveVectorLayerAs1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

5. Calcule el área total en hectáreas de cada municipio. Nombre el campo como `ATotalha`.

Expresión: `area(@geometry)/10000`

<div align="center"><img src="graph/QGIS_FieldCalculator.jpg" alt="rcfdtools" width="100%" border="0" /></div>

6. Utilizando el script de Python [qgis_clip_dissolve_reproject_adp.py](../../file/src/qgis_clip_dissolve_reproject_adp.py), recorte, disuelva, reproyecte y calcule la distribución porcentual de los municipios contenidos dentro de la zona de estudio. Podrá observar que dentro del área del proyecto existen 69 municipios contenidos o intersecadps. En la tabla de atributos de la capa disuelta y reproyectada, elimine los atributos `AREA`, `SHAPE_Leng` y `SHAPE_Area`.

> Antes de ejecutar el script, establezca en Settings / Options / Processing / General / Invalid features filtering / Do not filter.

Parámetros generales
```
input_layer_path = 'C:/IAMB/shp/MunicipiosAreaProyecto.shp'
overlay_layer_path = 'C:/IAMB/gdb/BD_ANLA_MAGNA_NACIONAL.gdb|layername=AreaProyecto'
output_file_clip_name = 'MunicipiosAreaProyectoClip'
dissolve_field = 'MpCodigo'
```

<div align="center"><img src="graph/QGIS_Clip1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Abra la tabla de atributos y ordene descendentemente por el campo `Aha`, podrá observar que 23 fracciones de municipios perimetrales al área del proyecto han sido incluídos como parte del análisis. Debido a las versiones y escala de digitalización, los municipios con áreas pequeñas `"Aha" <= 1100` no deberían ser incorporados a la base de datos ANLA.

<div align="center"><img src="graph/QGIS_Clip2.jpg" alt="rcfdtools" width="100%" border="0" /></div>

7. Calcule el % de área contenida de cada municipio dentro del área de estudio con respecto al total de su propia área. Nombre el campo de atributos como `APP`.

Expresión: `("Aha" / "ATotalha") * 100`

<div align="center"><img src="graph/QGIS_FieldCalculator1.jpg" alt="rcfdtools" width="100%" border="0" /></div>

<div align="center">

|   MpCodigo | MpNombre                   |   ATotalha |          Aha |          APD |           APP |
|-----------:|:---------------------------|-----------:|-------------:|-------------:|--------------:|
|      11001 | Bogotá, D.C.               |  161815    | 84497.1      | 14.2702      |  52.2183      |
|      15835 | Turmequé                   |    7957.76 |     0.563379 |  9.5146e-05  |   0.00707962  |
|      15842 | Úmbita                     |   14584.5  |     4.98134  |  0.000841272 |   0.0341552   |
|      25001 | Agua De Dios               |    8588.51 |  7103.71     |  1.19971     |  82.7118      |
|      25019 | Albán                      |    5075.1  |    46.442    |  0.00784333  |   0.915095    |
|      25035 | Anapoima                   |   12383.7  | 12372.5      |  2.08953     |  99.9093      |
|      25040 | Anolaima                   |   12083.1  | 11008.8      |  1.85921     |  91.1086      |
|      25095 | Bituima                    |    6101.69 |    77.7694   |  0.0131341   |   1.27455     |
|      25099 | Bojacá                     |   10220.7  | 10220.7      |  1.72613     | 100           |
|      25123 | Cachipay                   |    5339.58 |  5339.58     |  0.901773    | 100           |
|      25126 | Cajicá                     |    5125.63 |  5125.63     |  0.86564     | 100           |
|      25154 | Carmen De Carupa           |   29814.8  |    25.6659   |  0.00433457  |   0.0860844   |
|      25175 | Chía                       |    8005.16 |  8005.16     |  1.35195     | 100           |
|      25178 | Chipaque                   |   15036    |   501.698    |  0.0847291   |   3.33664     |
|      25181 | Choachí                    |   21213.2  |   123.909    |  0.0209264   |   0.584113    |
|      25183 | Chocontá                   |   29965.6  | 25475.2      |  4.30236     |  85.0147      |
|      25200 | Cogua                      |   13270.1  | 13263.1      |  2.23993     |  99.9469      |
|      25214 | Cota                       |    5367.95 |  5367.95     |  0.906564    | 100           |
|      25224 | Cucunubá                   |   10964.7  |  2451.58     |  0.414034    |  22.359       |
|      25245 | El Colegio                 |   11815.6  | 11810.2      |  1.99455     |  99.9539      |
|      25260 | El Rosal                   |    8712.01 |  7078.98     |  1.19553     |  81.2554      |
|      25269 | Facatativá                 |   15787.9  | 15527.4      |  2.62233     |  98.3496      |
|      25286 | Funza                      |    6997.26 |  6997.26     |  1.18173     | 100           |
|      25295 | Gachancipá                 |    4286.54 |  4286.54     |  0.723931    | 100           |
|      25307 | Girardot                   |   13025.3  |  7605.94     |  1.28453     |  58.3937      |
|      25312 | Granada                    |    6064.06 |  1121.48     |  0.189401    |  18.4939      |
|      25322 | Guasca                     |   36008.4  | 20880.9      |  3.52646     |  57.989       |
|      25326 | Guatavita                  |   25199.8  | 15388.1      |  2.5988      |  61.0642      |
|      25328 | Guayabal De Síquima        |    6183.97 |     0.017005 |  2.87188e-06 |   0.000274985 |
|      25368 | Jerusalén                  |   22167.3  |    63.5232   |  0.0107281   |   0.286563    |
|      25377 | La Calera                  |   32608    | 18919.9      |  3.19528     |  58.0222      |
|      25386 | La Mesa                    |   14812.9  | 14805.5      |  2.50041     |  99.9496      |
|      25402 | La Vega                    |   15527    |     4.06902  |  0.000687195 |   0.026206    |
|      25407 | Lenguazaque                |   15539.6  |     5.23275  |  0.00088373  |   0.0336736   |
|      25426 | Machetá                    |   22883.7  |    60.6109   |  0.0102362   |   0.264865    |
|      25430 | Madrid                     |   11944.5  | 11944.5      |  2.01724     | 100           |
|      25473 | Mosquera                   |   10601    | 10601        |  1.79035     | 100           |
|      25483 | Nariño                     |    5508.9  |    39.7      |  0.00670471  |   0.720652    |
|      25486 | Nemocón                    |    9822.99 |  9822.99     |  1.65895     | 100           |
|      25488 | Nilo                       |   22445.3  |    37.6378   |  0.00635645  |   0.167687    |
|      25513 | Pacho                      |   40214.7  |    28.5494   |  0.00482156  |   0.0709925   |
|      25535 | Pasca                      |   27137.7  |   220.332    |  0.0372107   |   0.811904    |
|      25596 | Quipile                    |   12759    |  3105.03     |  0.524392    |  24.3361      |
|      25599 | Apulo                      |   12187.2  | 12187.2      |  2.05823     | 100           |
|      25612 | Ricaurte                   |   12791.8  |  8506.34     |  1.43659     |  66.4982      |
|      25645 | San Antonio Del Tequendama |    8847.41 |  8827.72     |  1.49087     |  99.7775      |
|      25658 | San Francisco              |   11861.6  |    33.7277   |  0.00569609  |   0.284345    |
|      25718 | Sasaima                    |   11150.7  |    10.0266   |  0.00169334  |   0.0899194   |
|      25736 | Sesquilé                   |   14098.7  | 14086.5      |  2.37899     |  99.9131      |
|      25740 | Sibaté                     |   12585.9  |  9856.33     |  1.66458     |  78.3127      |
|      25743 | Silvania                   |   16278.5  |   129.19     |  0.0218181   |   0.79362     |
|      25754 | Soacha                     |   18330.6  | 17221.6      |  2.90846     |  93.9502      |
|      25758 | Sopó                       |   11115    | 11115        |  1.87715     | 100           |
|      25769 | Subachoque                 |   20896.7  | 18942.6      |  3.19912     |  90.6488      |
|      25772 | Suesca                     |   17301.9  | 13592.3      |  2.29553     |  78.5596      |
|      25777 | Supatá                     |   13023.8  |    10.4672   |  0.00176775  |   0.0803699   |
|      25785 | Tabio                      |    7512.98 |  7512.98     |  1.26883     | 100           |
|      25793 | Tausa                      |   20191.6  | 13727.1      |  2.31829     |  67.984       |
|      25797 | Tena                       |    5138.37 |  5138.37     |  0.86779     | 100           |
|      25799 | Tenjo                      |   11401    | 11401        |  1.92545     | 100           |
|      25805 | Tibacuy                    |    8464.38 |    14.684    |  0.0024799   |   0.17348     |
|      25815 | Tocaima                    |   24558.1  | 24428.2      |  4.12555     |  99.4712      |
|      25817 | Tocancipá                  |    7314.81 |  7314.81     |  1.23536     | 100           |
|      25841 | Ubaque                     |   10695    |    52.738    |  0.00890663  |   0.493108    |
|      25873 | Villapinzón                |   22580.4  | 12968.3      |  2.19014     |  57.4316      |
|      25878 | Viotá                      |   20110.4  | 20092.3      |  3.39327     |  99.91        |
|      25898 | Zipacón                    |    5414.08 |  5414.08     |  0.914354    | 100           |
|      25899 | Zipaquirá                  |   19458.1  | 18167.8      |  3.06826     |  93.3687      |
|      73275 | Flandes                    |    9674.43 |     1.94023  |  0.000327675 |   0.0200553   |

</div>


:pencil2:**Tarea:** Homologue y cargue el análisis realizado en la capa correspondiente del modelo ANLA.






## 3. Veredas

Caracterización de los componentes socioeconómicos a nivel de la(s) unidad(es) territorial(es) que está(n) dentro de un municipio pero que son más grandes que un asentamiento o que pueden contener más de un asentamiento, como son la Vereda, el Sector de Vereda o el Corregimiento (incluye el área rural). Se debe diligenciar la información para cada unidad territorial. Para la caracterización de los asentamientos se deberá diligenciar la capa geográfica "Asentamiento". En los casos en que la información que se requiere en detalle deba ser levantada según el tipo de estudio y términos de referencia, y que por algún motivo no pueda ser presentada, los campos numéricos se deben diligenciar con el número 999 y la justificación de la no presentación de la información se debe diligenciar en el campo de observaciones. En los campos alfanuméricos se debe presentar la justificación en el mismo campo.

La capa _UnidadTerritorial_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene varios dominios asociados:

<div align="center"><img src="graph/ANLA_UnidadTerritorial.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Dominios: Dom_UnidTerr, Dom_Municipio, Dom_Departamento, Dom_PoblaDesplaz, Dom_TransPublico, Dom_MediosComu, Dom_MediosComu, Dom_MediosComu, Dom_MediosComu, Dom_Activ_Econo, Dom_Activ_Econo, Dom_Activ_Econo, Dom_DesEconom, Dom_DesEconom, Dom_DesEconom, Dom_DesEconom, Dom_Boolean.

> Consulte todas las propiedades requeridas en el diccionario de datos del ANLA.


:pencil2:**Tarea:** Homologue y cargue el análisis realizado en la capa correspondiente del modelo ANLA.



## 4. Predios

Presenta los predios identificados en el área de influencia del proyecto y su caracterización, necesarios para el desarrollo de las diferentes actividades y de los objetivos del proyecto. 

La capa _Predios_ del modelo de datos ANLA, requiere de los siguientes atributos y contiene varios dominios asociados:

<div align="center"><img src="graph/ANLA_Predios.jpg" alt="rcfdtools" width="100%" border="0" /></div>

Dominios: Dom_Municipio, Dom_Departamento, Dom_Tenencia.

 

:pencil2:**Tarea:** Homologue y cargue el análisis realizado en la capa correspondiente del modelo ANLA.




## Referencias

*



## Control de versiones

| Versión     | Descripción                                 | Autor                                      | Horas |
|-------------|:--------------------------------------------|--------------------------------------------|:-----:|
| 2026.03.06 | Versión inicial con alcance de la actividad | [rcfdtools](https://github.com/rcfdtools)  |   9   |



##

_R.IAMB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._


| [◄ Anterior](../RemoteSensingDL/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.IAMB/discussions/1) | [Siguiente ►](../XXXX/Readme.md) |
|-------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|----------------------------------|

[^1]: https://learn.arcgis.com/es/arcgis-imagery-book/chapter2/
