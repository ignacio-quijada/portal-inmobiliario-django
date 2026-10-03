import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inmuebles_app.models import Inmueble, Comuna

def exportar_inmuebles_por_comuna():
    with open('reporte_comunas.txt', 'w', encoding='utf-8') as archivo:
        comunas = Comuna.objects.all()
        
        for comuna in comunas:
            archivo.write(f"\n{'='*40}\n")
            archivo.write(f"COMUNA: {comuna.nombre}\n")
            archivo.write(f"{'='*40}\n")
            
            inmuebles = Inmueble.objects.filter(
                comuna=comuna, 
                disponible=True
            ).values('direccion', 'descripcion')
            
            if not inmuebles:
                archivo.write("  No hay inmuebles disponibles.\n")
            else:
                for inm in inmuebles:
                    archivo.write(f"  - Dirección: {inm['direccion']}\n")
                    archivo.write(f"    Descripción: {inm['descripcion']}\n\n")
                    
    print("Éxito: Se ha generado 'reporte_comunas.txt'")

if __name__ == '__main__':
    exportar_inmuebles_por_comuna()