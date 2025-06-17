class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, logs: list[str] = None):
        if not hasattr(self, '_initialized'):
            self.logs = logs if logs else []
            self._initialized = True

    @classmethod
    def reboot_logger(cls):
        """Сброс синглтона"""
        if cls.instance:
            del cls.instance
        cls.instance = None

    def log(self, message: str):
        """Добавление лога"""
        self.logs.append(message)

    def get_logs(self):
        """Получение логов"""
        return self.logs

    def clear_logs(self):
        """Очистка логов"""
        self.logs = []

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]
