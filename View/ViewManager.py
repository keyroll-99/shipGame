from View.Exceptions.ViewNotFoundException import ViewNotFoundException
from View.BaseView import BaseView
from View import ViewNames
from View.MainMenu.MainMenuView import MainMenuView
from View.SearchGame.SearchGameView import SearchGameView


class ViewManager:
    currentView: str = ""
    viewList: dict[str, BaseView] = {}

    @staticmethod
    def init():
        ViewManager.viewList = {
            ViewNames.MAIN_MENU: MainMenuView(),
            ViewNames.SEARCH_GAME: SearchGameView()
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
