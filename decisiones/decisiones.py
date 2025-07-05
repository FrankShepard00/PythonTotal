import datetime
import os

class DecisionHelper:
    def __init__(self):
        self.decision_name = ""
        self.pros = []
        self.contras = []
        self.scale_options = {
            1: "Muy poco relevante",
            2: "Relevante", 
            3: "Significativamente relevante",
            4: "Muy relevante",
            5: "Extremadamente relevante"
        }
    
    def show_scale(self):
        print("\n📊 Escala de relevancia:")
        for key, value in self.scale_options.items():
            print(f"  {key} - {value}")
        print()
    
    def get_relevance_score(self):
        while True:
            try:
                self.show_scale()
                score = int(input("Selecciona el nivel de relevancia (1-5): "))
                if 1 <= score <= 5:
                    return score
                else:
                    print("❌ Por favor ingresa un número entre 1 y 5")
            except ValueError:
                print("❌ Por favor ingresa un número válido")
    
    def add_item(self):
        while True:
            item_type = input("\n¿Es un PRO o un CONTRA? (p/c): ").lower().strip()
            if item_type in ['p', 'pro', 'pros']:
                description = input("Describe el PRO: ").strip()
                if description:
                    score = self.get_relevance_score()
                    self.pros.append((description, score))
                    print(f"✅ PRO agregado: '{description}' - Relevancia: {score} ({self.scale_options[score]})")
                break
            elif item_type in ['c', 'contra', 'contras']:
                description = input("Describe el CONTRA: ").strip()
                if description:
                    score = self.get_relevance_score()
                    self.contras.append((description, score))
                    print(f"✅ CONTRA agregado: '{description}' - Relevancia: {score} ({self.scale_options[score]})")
                break
            else:
                print("❌ Por favor responde 'p' para PRO o 'c' para CONTRA")
    
    def show_current_status(self):
        print(f"\n📋 Estado actual de la decisión: '{self.decision_name}'")
        
        print(f"\n✅ PROS ({len(self.pros)}):")
        pros_total = 0
        for i, (desc, score) in enumerate(self.pros, 1):
            print(f"  {i}. {desc} - {score} ({self.scale_options[score]})")
            pros_total += score
        
        print(f"\n❌ CONTRAS ({len(self.contras)}):")
        contras_total = 0
        for i, (desc, score) in enumerate(self.contras, 1):
            print(f"  {i}. {desc} - {score} ({self.scale_options[score]})")
            contras_total += score
        
        print(f"\n📊 PUNTUACIONES:")
        print(f"  Total PROS: {pros_total}")
        print(f"  Total CONTRAS: {contras_total}")
        
        final_score = pros_total - contras_total
        print(f"  PUNTUACIÓN FINAL: {final_score}")
        
        if final_score > 0:
            print(f"  🎯 RECOMENDACIÓN: ¡Adelante! La decisión tiene una puntuación positiva.")
        elif final_score < 0:
            print(f"  ⚠️  RECOMENDACIÓN: Considera con cuidado. La decisión tiene una puntuación negativa.")
        else:
            print(f"  🤔 RECOMENDACIÓN: Decisión equilibrada. Podrías necesitar más análisis.")
        
        return final_score, pros_total, contras_total
    
    def save_to_file(self, final_score, pros_total, contras_total):
        timestamp = datetime.datetime.now()
        filename = f"decision_{timestamp.strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"ANÁLISIS DE DECISIÓN\n")
            file.write(f"=" * 50 + "\n")
            file.write(f"Decisión: {self.decision_name}\n")
            file.write(f"Fecha y hora: {timestamp.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            
            file.write(f"PROS ({len(self.pros)}):\n")
            file.write("-" * 20 + "\n")
            for i, (desc, score) in enumerate(self.pros, 1):
                file.write(f"{i}. {desc} - {score} ({self.scale_options[score]})\n")
            
            file.write(f"\nCONTRAS ({len(self.contras)}):\n")
            file.write("-" * 20 + "\n")
            for i, (desc, score) in enumerate(self.contras, 1):
                file.write(f"{i}. {desc} - {score} ({self.scale_options[score]})\n")
            
            file.write(f"\nRESUMEN:\n")
            file.write("-" * 20 + "\n")
            file.write(f"Total PROS: {pros_total}\n")
            file.write(f"Total CONTRAS: {contras_total}\n")
            file.write(f"PUNTUACIÓN FINAL: {final_score}\n")
            
            if final_score > 0:
                file.write(f"RECOMENDACIÓN: ¡Adelante! La decisión tiene una puntuación positiva.\n")
            elif final_score < 0:
                file.write(f"RECOMENDACIÓN: Considera con cuidado. La decisión tiene una puntuación negativa.\n")
            else:
                file.write(f"RECOMENDACIÓN: Decisión equilibrada. Podrías necesitar más análisis.\n")
        
        print(f"\n💾 Decisión guardada en: {filename}")
    
    def run(self):
        print("🎯 ¡Bienvenido al Asistente de Toma de Decisiones!")
        print("=" * 50)
        
        self.decision_name = input("¿Cuál es la decisión que estás considerando? (ej: 'Mudarme a X lugar'): ").strip()
        
        while True:
            self.add_item()
            
            if self.pros or self.contras:
                self.show_current_status()
            
            continue_adding = input("\n¿Quieres agregar otro elemento? (s/n): ").lower().strip()
            if continue_adding not in ['s', 'si', 'sí', 'y', 'yes']:
                break
        
        print("\n" + "=" * 50)
        print("📋 ANÁLISIS FINAL")
        print("=" * 50)
        
        final_score, pros_total, contras_total = self.show_current_status()
        
        save_file = input("\n¿Quieres guardar esta decisión en un archivo? (s/n): ").lower().strip()
        if save_file in ['s', 'si', 'sí', 'y', 'yes']:
            self.save_to_file(final_score, pros_total, contras_total)
        
        print("\n🎯 ¡Gracias por usar el Asistente de Toma de Decisiones!")

if __name__ == "__main__":
    decision_helper = DecisionHelper()
    decision_helper.run()