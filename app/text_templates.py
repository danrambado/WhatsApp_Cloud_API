# This file contains the text templates to be used. They will be classified 
# by the type of message in which they will be used. To know more about 
# the message types, check the file template_message.py, there you will find the message types.


# Confirmation message:
confirmation_message = {
    "header_text": "Confirmación de turno médico | Cardiologia",
    "body_text": "Estimado/a paciente es un placer confirmar su turno médico programado para el día *{}* a las *{}hs*. Le recomendamos llegar con 10 minutos de anticipación. Este mensaje es para confirmar su asistencia. Por favor, háganos saber si necesita cancelar o reprogramar su turno.",
    "footer_text": "IAF | Instituto Alexander Fleming",
    "button_1": {
        "id": "confirmation_button",
        "title": "Confirmar turno"
    },
    "button_2": {
        "id": "cancelation_button",
        "title": "Cancelar turno"
    },
    "button_3": {
        "id": "reschedule_button",
        "title": "Reprogramar turno"
    }
}
