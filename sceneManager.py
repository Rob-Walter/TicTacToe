from Scenes.gameScene import GameScene
from Scenes.login_scene import LoginScene
from Scenes.registration_scene import RegistrationScene
from Scenes.mainmenue_scene import MainMenueScene

class SceneManager(object):
    def __init__(self) -> None:
        self.goTo(GameScene())

    def goTo(self,scene):
        self.scene = scene
        self.scene.manager = self