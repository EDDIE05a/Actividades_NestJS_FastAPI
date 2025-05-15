def validar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario.strip().lower() == respuesta_correcta.strip().lower()
