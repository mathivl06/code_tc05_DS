# Observer: canal de YouTube

Demostración didáctica del patrón Observer en Python. `CanalYoutube` es el
sujeto observable; cada suscriptor registrado recibe una notificación cuando
se publica un vídeo. El canal depende del contrato `Observador`, no de las
clases concretas de suscriptor.

## Observadores concretos

- `NotificacionAlCelular`: guarda e imprime un aviso dirigido al teléfono.
- `EstadisticasDelCanal`: incrementa e imprime la cantidad de vídeos publicados.

Ambos reaccionan a las publicaciones del mismo canal de maneras distintas;
`CanalYoutube` no necesita conocer sus clases.

## Archivos

- `demo.py`: implementación y ejemplo ejecutable.
- `test_observer.py`: tres pruebas del contrato del patrón.

## Ejecución

Desde esta carpeta:

```bash
python demo.py
pytest -q
```

## Qué demuestra cada prueba

1. `test_un_observador_nuevo_se_suscribe_sin_cambiar_el_canal` registra desde
   la prueba un observador que el canal no conoce y comprueba que recibe el
   evento. Detecta una implementación acoplada a una lista de tipos o nombres
   concretos.
2. `test_cancelar_suscripcion_notifica_solo_a_los_observadores_activos`
   comprueba que quitar un observador detiene sus notificaciones sin afectar
   al otro suscriptor.
3. `test_observadores_de_clases_distintas_reaccionan_de_forma_distinta`
   comprueba que un mismo evento produce un aviso en el teléfono y aumenta el
   contador de estadísticas, sin añadir condiciones al canal.
