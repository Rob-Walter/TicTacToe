from Scenes.game_Scene import GameScene
from Scenes.login_scene import LoginScene
from Scenes.registration_scene import RegistrationScene
from Scenes.mainmenue_scene import MainMenueScene
from Scenes.leaderboard_scene import LeaderboardScene
from Scenes.start_scene import StartScene

class SceneManager(object):
    def __init__(self) -> None:
        self.goTo(StartScene())

    def goTo(self,scene):
        self.scene = scene
        self.scene.manager = self