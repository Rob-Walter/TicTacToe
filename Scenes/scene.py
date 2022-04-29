class Scene(object):
    def __init__(self) -> None:
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handleEvents(self, events):
        raise NotImplementedError