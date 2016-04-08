class Message:
    """Classe de transporte"""

    def __init__(self, msg_type, data):
        self.msg_type = msg_type
        self.data = data
