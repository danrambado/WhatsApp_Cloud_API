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
        self.warning = "\u26a0\ufe0f Este número es solo para confirmación de turnos.\n\n\u26d4\ufe0f *NO ENVÍE MENSAJES*.\n\n _Por consultas, comuníquese al siguiente número:_ \n\uD83D\uDCDE wa.me/+541163814684"
    
    def confirmation_bye(self):
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"\ud83d\udc4f Gracias por confirmar su turno. \n\n *¡Le deseamos que tenga un buen día!* \uD83D\uDE0A \n\n {self.warning}"
        }

    def reschedule_bye(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"\u231b️ A la brevedad nos contactaremos con usted para reprogramar su turno. \n\n *¡Le deseamos que tenga un buen día!* \uD83D\uDE0A \n\n {self.warning}"
        }
    def cancellation_bye(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"\ud83d\udc4f Agradecemos su respuesta. \n\n *¡Le deseamos que tenga un buen día!* \uD83D\uDE0A \n\n {self.warning}"
        }
    def form(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "to": self.to,
            "body": f"Antes de su cita médica \uD83C\uDFE5\n\n *¡Le solicitamos que actualice la información de su estado de salud!* \uD83D\uDC68\u200D\u2695\uFE0F\uD83C\uDF21\n\n Por favor, complete el siguiente formulario \uD83D\uDD3D\n\n\uD83D\uDCDD https://forms.gle/QLbL4Zjk7uHi8J2W8\n\n _¡Gracias!_"
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
            "to": self.to,
            "header_text": "Confirmación de turno | Cardiología",
            "body_text": f"Estimado/a paciente este mensaje _automático_ un es para confirmar su turno médico programado para el día *{date}* a las *{time}hs*. Le recomendamos llegar con 10 minutos de anticipación. Por favor seleccione la opcion deseada.",
            "footer_text": "Cardiología IAF",
            "reply_buttons": {
                "button_1": "Confirmar turno",
                "button_2": "Cancelar turno",
                "button_3": "Reprogramar turno"
            }
        }