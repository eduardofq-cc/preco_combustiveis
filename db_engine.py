from sqlalchemy import Engine, create_engine

class conector:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}")

    def get_engine(self) -> "Engine":
        return self.engine