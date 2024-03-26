def preguntar_respuesta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    print("Responda las siguientes preguntas para el análisis rápido:")
    while respuesta not in ['s', 'n']:
        print("Error de lectura, s para Sí y n para No")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == 's'

def evaluar_sintomas():
    print("Por favor, responde las siguientes preguntas con respecto a tus síntomas y antecedentes:")
    a = preguntar_respuesta("¿Se confunde con frecuencia en lugares familiares?")
    b = preguntar_respuesta("Tiene dificultad para recordar nombres o eventos recientes?")
    c = preguntar_respuesta("¿Ha experimentado cambios en su capacidad para planificar o resolver problemas?")
    d = preguntar_respuesta("¿Tiene dificultad para seguir conversaciones o hilos de pensamiento?")
    e = preguntar_respuesta("¿Ha notado cambios en su capacidad para realizar tareas cotidianas, como cocinar o vestirse?")
    f = preguntar_respuesta("¿Se siente desorientado en cuanto a la fecha o la hora?")
    g = preguntar_respuesta("¿Ha perdido objetos personales con más frecuencia de lo normal?")
    h = preguntar_respuesta("¿Tiene dificultad para encontrar las palabras adecuadas al hablar o escribir?")
    i = preguntar_respuesta("¿Ha experimentado cambios en su juicio o toma de decisiones?")
    j = preguntar_respuesta("¿Ha mostrado una disminución en su interés por actividades sociales o pasatiempos?")
    
    sintomas_pesos = [3, 2, 1, 1, 1, 1, 1, 1]  # Pesos asignados a cada síntoma
    factores_pesos = [4, 4]  # Pesos asignados a los factores de riesgo
    
    sintomas = [c, d, e, f, g, h, i, j]
    factores = [a, b]
    
    puntaje_sintomas = sum(peso * int(sintoma) for peso, sintoma in zip(sintomas_pesos, sintomas))
    puntaje_factores = sum(peso * int(factor) for peso, factor in zip(factores_pesos, factores))
    
    puntaje_total = puntaje_sintomas + puntaje_factores
    
    umbral_probabilidad_alta = 15  #puntaje para determinar alta probabilidad
    
    print('')
    print(puntaje_total)
    
    if puntaje_total >= umbral_probabilidad_alta:
        
      print("La probabilidad es alta, para un mejor análisis acuda a su médico")
    else:
        print("La probabilidad es baja, de igual manera se recomienda acudir a su médico para más certeza")
        
if __name__ == "__main__":
    evaluar_sintomas()
