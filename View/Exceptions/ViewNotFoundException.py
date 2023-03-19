class ViewNotFoundException(Exception):
    def __init__(self, name: str):
        super().__init__(f"view {name} not found")
