"""Demostración mínima del patrón Observer con un canal de YouTube."""

from typing import Protocol


class Observador(Protocol):
    """Contrato que cumple cualquier suscriptor notificable."""

    def recibir_notificacion(self, canal: str, video: str) -> None:
        """Recibe el nombre del canal y el vídeo publicado."""


class CanalYoutube:
    """Sujeto observable que administra suscriptores y publica vídeos."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._suscriptores: list[Observador] = []

    def suscribir(self, observador: Observador) -> None:
        """Agrega un suscriptor una sola vez."""
        if observador not in self._suscriptores:
            self._suscriptores.append(observador)

    def cancelar_suscripcion(self, observador: Observador) -> None:
        """Deja de notificar al observador indicado."""
        if observador in self._suscriptores:
            self._suscriptores.remove(observador)

    def publicar_video(self, titulo: str) -> None:
        """Publica un vídeo y notifica a los suscriptores actuales."""
        for suscriptor in tuple(self._suscriptores):
            suscriptor.recibir_notificacion(self.nombre, titulo)


class NotificacionAlCelular:
    """Observador concreto que prepara avisos para el teléfono."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.avisos: list[str] = []

    def recibir_notificacion(self, canal: str, video: str) -> None:
        aviso = f"📱 Nuevo vídeo de {canal}: {video}"
        self.avisos.append(aviso)
        print(f"{self.nombre} recibió: {aviso}")


class EstadisticasDelCanal:
    """Observador concreto que cuenta los vídeos publicados."""

    def __init__(self) -> None:
        self.videos_publicados = 0

    def recibir_notificacion(self, canal: str, video: str) -> None:
        self.videos_publicados += 1
        print(f"📊 {canal}: {self.videos_publicados} vídeo(s) publicados.")


def main() -> None:
    """Conecta dos observadores distintos al mismo canal."""
    canal = CanalYoutube("Cocina con Ana")
    aviso_celular = NotificacionAlCelular("Luis")
    estadisticas = EstadisticasDelCanal()

    canal.suscribir(aviso_celular)
    canal.suscribir(estadisticas)
    canal.publicar_video("Pan casero en 10 minutos")
    canal.publicar_video("Cómo hacer una masa madre")


if __name__ == "__main__":
    main()
