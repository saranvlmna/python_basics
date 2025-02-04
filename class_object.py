class Phone:
    def __init__(self, camera, speaker):
        self.camera = camera
        self.speaker = speaker

    def details(self):
        return f'Phone with {self.camera} and {self.speaker}'  # Fixed f-string formatting

