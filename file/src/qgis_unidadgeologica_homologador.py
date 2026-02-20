# https://github.com/rcfdtools
# Geology homologation from AGC to ANLA model
# This script has to be run in the QGIS Python console
# Stop editing before run the script
# Make sure the UC layer is selected in the Layers panel
# Tested in QGIS 3.44.6

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils


# Get the active layer from Layer panel
layer = iface.activeLayer()

# General parameters
eon_field = ['EON', QVariant.Double]
era_field = ['ERA', QVariant.Double]
periodo_field = ['PERIODO', QVariant.Double]
epoca_field = ['EPOCA', QVariant.Double]
edad_field = ['EDAD', QVariant.Double]
nombre_field = ['NOMBRE', QVariant.String]
nomenclat_field = ['NOMENCLAT', QVariant.String]
old_edad_name = 'Edad'  # Current edad name in UC layer
new_edad_name = 'EdadTxt'  # New edad txt name in UC layer    


# Add fields and do calculations
new_field_list = [eon_field, era_field, periodo_field, epoca_field, edad_field, nombre_field, nomenclat_field]
if layer and layer.dataProvider().capabilities() & QgsVectorDataProvider.AddAttributes:
    # Rename current UC Edad name
    field_index = layer.fields().indexFromName(old_edad_name)
    if field_index != -1:
        layer.startEditing()
        try:
            layer.renameAttribute(field_index, new_edad_name)
            layer.commitChanges()
            print(f"Field '{old_edad_name}' successfully renamed to '{new_edad_name}'.")
        except:
            layer.rollbackChanges()
            print("Error renaming field. Changes rolled back.")
    else:
        print(f"Field '{old_edad_name}' not found.")        
    
    # Fields creation
    for field in new_field_list:
        # Check and delete existind required fields
        field_index = layer.fields().indexFromName(field[0])
        if field_index != -1:
            with edit(layer):
                 layer.dataProvider().deleteAttributes([field_index])
        layer.updateFields()
        
        # New Field, parameters are: field name, data type, field length, precision
        if field[1] == QVariant.Date:
            new_field = QgsField(field[0], field[1])
        else:
            new_field = QgsField(field[0], field[1], len=20, prec=10)
            
        # Use an editing buffer to add the field and commit changes automatically
        with edit(layer):
            layer.dataProvider().addAttributes([new_field])
            layer.updateFields() # Update the layer's fields after adding
        
        print(f'Field "{field[0]}" added to layer "{layer.name()}"')
    layer.commitChanges()
    
   
else:
    print('Error: No active layer found, or the layer does not support adding or calculate fields.')


