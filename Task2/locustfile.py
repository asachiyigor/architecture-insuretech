from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    """
    Класс для симуляции пользователей, генерирующих нагрузку на приложение.

    Используется для тестирования автоматического масштабирования (HPA) в Kubernetes.
    """

    # Время ожидания между запросами (от 1 до 5 секунд)
    wait_time = between(1, 5)

    @task
    def index(self):
        """
        Основная задача: обращение к корневому endpoint (/),
        который возвращает идентификатор пода.
        """
        self.client.get("/")

    @task(2)  # Выполняется в 2 раза чаще
    def metrics(self):
        """
        Дополнительная задача: обращение к endpoint метрик (/metrics),
        который возвращает метрики в формате Prometheus.
        """
        self.client.get("/metrics")
