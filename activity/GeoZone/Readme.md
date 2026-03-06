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

<div align="center"><img src="graph/ColombiaMapas_Departamento.png" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS, abra el mapa _/map/CaseStudy.qgz_ y guarde como  _/map/GeoZone.qgz_. Cargue y rotule la capa [/data/IGAC/DepartamentosColombia20260306.shp](../../file/data/IGAC/DepartamentosColombia20260306.zip). Podrá observar que la zona de estudio se encuentra dentro del Departamento de Cundinamarca y que en los extremos nor-este y sur-oeste, los límites no son completamente coincidentes.

3. Para la generación del polígono requerido por el ANLA, utilice el polígono completo de la zona de estudio agregando los atributos requeridos.

<div align="center"><img src="graph/QGIS_Departamento.png" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_Departamento1.png" alt="rcfdtools" width="100%" border="0" /></div>

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

<div align="center"><img src="graph/ColombiaMapas_Municipio.png" alt="rcfdtools" width="100%" border="0" /></div>

2. En QGIS cargue y rotule la capa [/data/IGAC/MunicipiosColombia20260306.shp](../../file/data/IGAC/MunicipiosColombia20260306.zip). Podrá observar que la zona de estudio interseca o contiene múltiples municipios.

<div align="center"><img src="graph/QGIS_Municipio.png" alt="rcfdtools" width="100%" border="0" /></div>

3. Utilizando la herramienta _Vector Selection / Select by location_, seleccione todos los municipios que intersecan el área de estudio. Podrá observar que se han seleccionado 69 municipios.

<div align="center"><img src="graph/QGIS_SelectByLocation.png" alt="rcfdtools" width="100%" border="0" /></div>

4. Exporte y re-proyecte los municipios seleccionados, guarde como /shp/MunicipiosAreaProyecto.shp.

<div align="center"><img src="graph/QGIS_SaveVectorLayerAs.png" alt="rcfdtools" width="100%" border="0" /></div>
<div align="center"><img src="graph/QGIS_SaveVectorLayerAs1.png" alt="rcfdtools" width="100%" border="0" /></div>

5. Calcule el área total en hectáreas de cada municipio. Nombre el campo como `ATotalha`.

Expresión: `area(@geometry)/10000`

<div align="center"><img src="graph/QGIS_FieldCalculator.png" alt="rcfdtools" width="100%" border="0" /></div>

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
