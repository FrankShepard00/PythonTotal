from datetime import datetime, timedelta
from math import ceil

class CursoPlanner:
    def __init__(self):
        # Valores predefinidos
        self.total_videos = 246
        self.fecha_inicio = datetime(2025, 6, 16)
        # Ajustamos la hora actual a CDMX (UTC-6)
        self.fecha_actual = datetime.now()
        self.fecha_fin = datetime(2025, 8, 31)
        self.dias_libres = {
            # Junio 2025
            datetime(2025, 6, 21).date(),   # sábado
            datetime(2025, 6, 22).date(),   # domingo
            datetime(2025, 6, 28).date(),   # sábado
            datetime(2025, 6, 29).date(),   # domingo
            # Julio 2025
            datetime(2025, 7, 5).date(),    # sábado
            datetime(2025, 7, 6).date(),    # domingo
            datetime(2025, 7, 12).date(),   # sábado
            datetime(2025, 7, 13).date(),   # domingo
            datetime(2025, 7, 19).date(),   # sábado
            datetime(2025, 7, 20).date(),   # domingo
            datetime(2025, 7, 26).date(),   # sábado
            datetime(2025, 7, 27).date(),   # domingo
            # Agosto 2025
            datetime(2025, 8, 2).date(),    # sábado
            datetime(2025, 8, 3).date(),    # domingo
            datetime(2025, 8, 9).date(),    # sábado
            datetime(2025, 8, 10).date(),   # domingo
            datetime(2025, 8, 16).date(),   # sábado
            datetime(2025, 8, 17).date(),   # domingo
            datetime(2025, 8, 23).date(),   # sábado
            datetime(2025, 8, 24).date(),   # domingo
            datetime(2025, 8, 30).date(),   # sábado
            datetime(2025, 8, 31).date(),   # domingo
        }

    def calcular_dias_transcurridos(self):
        """Calcula los días disponibles desde el inicio hasta hoy"""
        dias = 0
        dia_actual = self.fecha_inicio
        while dia_actual.date() <= self.fecha_actual.date():
            if dia_actual.date() not in self.dias_libres:
                dias += 1
            dia_actual += timedelta(days=1)
        return dias

    def calcular_dias_restantes(self):
        """Calcula los días disponibles hasta el final"""
        dias = 0
        dia_actual = self.fecha_actual
        while dia_actual <= self.fecha_fin:
            if dia_actual.date() not in self.dias_libres:
                dias += 1
            dia_actual += timedelta(days=1)
        return dias

    def analizar_progreso(self, videos_completados):
        """Analiza el progreso y muestra el estado actual"""
        dias_transcurridos = self.calcular_dias_transcurridos()
        dias_restantes = self.calcular_dias_restantes()
        videos_restantes = self.total_videos - videos_completados
        
        # Calcular videos esperados según el plan original
        videos_por_dia_original = self.total_videos / (dias_transcurridos + dias_restantes)
        videos_esperados = ceil(videos_por_dia_original * dias_transcurridos)
        
        # Calcular nuevos videos por día necesarios
        videos_por_dia_ajustado = videos_restantes / dias_restantes if dias_restantes > 0 else 0
        videos_por_dia_ajustado = ceil(videos_por_dia_ajustado)

        print("\n=== PROGRESO DEL CURSO Python Total ===")
        print(f"Fecha actual: {self.fecha_actual.strftime('%Y-%m-%d %H:%M')} (CDMX)")
        print(f"Fecha final : {self.fecha_fin.strftime('%Y-%m-%d %H:%M')}")
        print(f"\nEstado:")
        print(f"- Has completado el video número: {videos_completados}")
        print(f"- Deberías ir en el video número: {videos_esperados}")
        
        if videos_completados < videos_esperados:
            diferencia = videos_esperados - videos_completados
            print(f"¡Vas atrasado por {diferencia} videos!")
        elif videos_completados > videos_esperados:
            diferencia = videos_completados - videos_esperados
            print(f"¡Vas adelantado por {diferencia} videos!")
        else:
            print("¡Vas al día!")
            
        print(f"\nPlan ajustado:")
        print(f"- Te faltan {videos_restantes} videos")
        print(f"- Tienes {dias_restantes} días disponibles")
        print(f"- Necesitas completar {videos_por_dia_ajustado} videos por día para terminar a tiempo")

def main():
    planner = CursoPlanner()
    videos_completados = int(input("¿Cuántos videos has completado hasta ahora? "))
    planner.analizar_progreso(videos_completados)

if __name__ == "__main__":
    main()