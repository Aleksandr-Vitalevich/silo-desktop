class AppState:
    """Глобальное состояние приложения в оперативной памяти"""
    master_password = None

    @classmethod
    def clear(cls):
        """Очистка памяти при выходе"""
        cls.master_password = None
