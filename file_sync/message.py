class Message:
    def __init__(self, msg_type: str=None, data: tuple=None):
        self.msg_type = msg_type
        self.data = data
