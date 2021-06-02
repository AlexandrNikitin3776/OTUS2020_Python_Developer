class LogConfig:
    REPORT_SIZE: int = 1000
    REPORT_DIR: str = "./reports"
    LOG_DIR: str = "./log"

    def update(self, config_args: dict):
        # Проверить, что config_args не пустой
        # Проверить, что в config_args содержатся только аргументы из списка переменных
        self.__dict__.update(config_args)
