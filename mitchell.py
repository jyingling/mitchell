import qgis.core
import simplekml

x = 0

fplist = ['01','02','04','05','06','08','09','10','11','12','13','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','44','45','46','47','48','49','50','51'] #fill in with stateFPs

while x < (number of states):
    
    layer = iface.activeLayer()
    
    statefp = fplist[x]
    
    selection = layer.selectByExpression(f"STATEFP = \"{statefp}\"")
    
    filename = f"C:/Users/Julia/Documents/upwork/mitchell/states/tracts_{statefp}_pov.kml"
    
	writer = QgsVectorFileWriter.writeAsVectorFormat(i,filename,"utf-8",None,"ESRI Shapefile", True)
    
    x = x + 1