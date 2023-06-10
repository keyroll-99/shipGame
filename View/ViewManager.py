from View.Exceptions.ViewNotFoundException import ViewNotFoundException
from View.BaseView import BaseView
from View import ViewNames
from View.FinishGame.FinishGameView import FinishGame
from View.MainMenu.MainMenuView import MainMenuView
from View.PrepareGame.PrepareGameView import PrepareGameView
from View.SearchGame.SearchGameView import SearchGameView
from View.GameLobby.GameLobbyView import GameLobbyView
from View.Game.GameView import GameView


class ViewManager:
    currentView: str = ""
    viewList: dict[str, BaseView] = {}

    @staticmethod
    def init():
        ViewManager.viewList = {
            ViewNames.SEARCH_GAME: SearchGameView(),
            ViewNames.GAME_LOBBY: GameLobbyView(),
            ViewNames.GAME: GameView(),
            ViewNames.PREPARE_GAME: PrepareGameView(),
            ViewNames.MAIN_MENU: MainMenuView(),
            ViewNames.FINISH_GAME: FinishGame()
        }

    @staticmethod
    def load_view(viewName: str):
        if viewName not in ViewManager.viewList:
            raise ViewNotFoundException(viewName)

        if ViewManager.currentView != viewName:
            if ViewManager.currentView in ViewManager.viewList:
                ViewManager.viewList[ViewManager.currentView].unload()
            ViewManager.viewList[viewName].load()
            ViewManager.currentView = viewName
