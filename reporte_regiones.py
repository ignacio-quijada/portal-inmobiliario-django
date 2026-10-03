import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inmuebles_app.models import Inmueble, Region

def exportar_inmuebles_por_region():
    with open('reporte_regiones.txt', 'w', encoding='utf-8') as archivo:
        regiones = Region.objects.all()
        
        for region in regiones:
            archivo.write(f"\n{'='*40}\n")
            archivo.write(f"REGIÓN: {region.nombre}\n")
            archivo.write(f"{'='*40}\n")
            
            inmuebles = Inmueble.objects.filter(
                comuna__region=region, 
                disponible=True
            )
            
            if not inmuebles:
                archivo.write("  No hay inmuebles disponibles en esta región.\n")
            else:
                for inm in inmuebles:
                    archivo.write(f"  - {inm.direccion} (Ubicado en: {inm.comuna.nombre}) - Valor: ${inm.valor_arriendo}\n")
                    
    print("Éxito: Se ha generado 'reporte_regiones.txt'")

if __name__ == '__main__':
    exportar_inmuebles_por_region()