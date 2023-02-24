"""
Messages templates to send acording to the schemas parameters specified in the schemas.py
"""

class TextMessages:
    """Class for WhatsApp text templates messages"""
    def __init__(self, to: int):
        """
        Parameters:
        to (int): The phone number of the recipient.
        body (str): The body text of the message.
        """
        self.to = to
        self.warning = "Este numero es solo para confirmacion de turnos. *NO ENVIE MENSAJES*. Por consultas comuniquese al 1135723096"

    def reschedule_bye(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"A la brevedad nos contactaremos con usted. Le deseamos un buen dia. {self.warning}"
        }
    def canlation_bye(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"Agradecemos su respuesta. Le deseamos un buen dia. {self.warning}"
        }

class ButtonMessages:
    """Class for WhatsApp Intetactive Button templates messages"""
    def __init__(self, to: int):
        """
        Parameters:
        to (int): The phone number of the recipient.
        body (str): The body text of the message.
        """
        self.to = to
        self.warning = "Este numero es solo para confirmacion de turnos. *NO ENVIE MENSAJES*. Por consultas comuniquese al 1135723096"

    def confirmation_message(self, date, time) -> dict:
        return {
            "header_text": "Confirmación de turno | Cardiologia",
            "body_text": f"Estimado/a paciente es un placer confirmar su turno médico programado para el día *{date}* a las *{time}hs*. Le recomendamos llegar con 10 minutos de anticipación. Este mensaje es para confirmar su asistencia. Por favor, háganos saber si necesita cancelar o reprogramar su turno.",
            "footer_text": "IAF | Instituto Alexander Fleming",
            "reply_buttons": {
                "button_1": "Confirmar turno",
                "button_2": "Cancelar turno",
                "button_3":"Reprogramar turno"
            }
        }