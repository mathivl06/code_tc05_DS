"""Pruebas de comportamiento del patrón Observer."""

from demo import (
    CanalYoutube,
    EstadisticasDelCanal,
    NotificacionAlCelular,
)


class SuscriptorDePrueba:
    """Observador nuevo que el canal no conoce de antemano."""

    def __init__(self) -> None:
        self.recibidos: list[tuple[str, str]] = []

    def recibir_notificacion(self, canal: str, video: str) -> None:
        self.recibidos.append((canal, video))


def test_un_observador_nuevo_se_suscribe_sin_cambiar_el_canal() -> None:
    canal = CanalYoutube("Ciencia en corto")
    tercero = SuscriptorDePrueba()

    canal.suscribir(tercero)
    canal.publicar_video("Experimento de densidad")

    assert tercero.recibidos == [
        ("Ciencia en corto", "Experimento de densidad")
    ]


def test_cancelar_suscripcion_notifica_solo_a_los_observadores_activos() -> None:
    canal = CanalYoutube("Historia viva")
    activo = NotificacionAlCelular("Marta")
    retirado = EstadisticasDelCanal()
    canal.suscribir(activo)
    canal.suscribir(retirado)

    canal.cancelar_suscripcion(retirado)
    canal.publicar_video("La ruta de la seda")

    assert activo.avisos == ["📱 Nuevo vídeo de Historia viva: La ruta de la seda"]
    assert retirado.videos_publicados == 0


def test_observadores_de_clases_distintas_reaccionan_de_forma_distinta() -> None:
    canal = CanalYoutube("Ciencia en corto")
    aviso = NotificacionAlCelular("Marta")
    estadisticas = EstadisticasDelCanal()
    canal.suscribir(aviso)
    canal.suscribir(estadisticas)

    canal.publicar_video("Experimento de densidad")

    assert aviso.avisos == [
        "📱 Nuevo vídeo de Ciencia en corto: Experimento de densidad"
    ]
    assert estadisticas.videos_publicados == 1
