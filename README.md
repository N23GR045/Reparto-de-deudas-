# Reparto de Deudas

App web para el móvil donde apuntas quién te debe dinero, registras lo que te van devolviendo y repartes gastos compartidos entre amigos. Funciona en Android como APK y en el iPhone como app web instalada en la pantalla de inicio.

Es un único archivo HTML, sin servidor ni base de datos: tus datos se guardan en tu propio dispositivo.

## Qué hace

**Me deben**
- Apunta a quién le prestaste, cuánto, para qué y hasta cuándo.
- Registra pagos parciales o «Lo pagó todo». La deuda se marca como saldada sola.
- «Le presto más»: suma dinero a una deuda que ya existe.
- Historial de movimientos de cada deuda: préstamo, ampliaciones y pagos.
- Estado de cada deuda: pendiente, vence pronto, vencida o saldada.
- Mensaje de recordatorio listo para copiar y mandar por WhatsApp, con una plantilla que puedes cambiar.
- Buscador, filtros y varias formas de ordenar.

**Repartir**
- **Dividir una cuenta**: escribes lo que pagaste, eliges entre quiénes y cada parte se apunta como deuda en un toque.
- **Grupos** para viajes, el piso o cualquier gasto que se repita: anotas quién pagó cada cosa y la app calcula quién debe a quién con el menor número de pagos.
- Reparto a partes iguales o con cantidades distintas para cada persona.
- «Ya me pagó» y «Pasar a Me deben» para cerrar las cuentas del grupo.

**Personalizar**
- Tema claro, oscuro o automático, 10 colores, tamaño del texto, espaciado y forma de las esquinas.
- Moneda (euro, dólar, pesos latinoamericanos y más), avisos de vencimiento y plazo por defecto.
- Exportar e importar una copia de seguridad de tus datos en un archivo `.json`.

## Probarla en el ordenador

Abre `index.html` en el navegador con un doble clic. Funciona sin instalar nada.

## Descargar el APK para Android

Cada vez que se sube un cambio a `main`, GitHub compila un APK nuevo y lo publica en **Releases**. La app instalada avisa cuando hay una versión nueva.

- Descarga directa de la última versión: **https://github.com/N23GR045/Reparto-de-deudas-/releases/latest/download/reparto-de-deudas.apk**
- Todas las versiones: https://github.com/N23GR045/Reparto-de-deudas-/releases

Para instalarlo, abre el enlace desde el móvil Android, descarga el archivo y ábrelo. Si Android lo pide, permite instalar apps de este origen. Las versiones nuevas se instalan encima de la anterior y conservan tus datos.

El proceso está en `.github/workflows/apk.yml` y usa [Capacitor](https://capacitorjs.com/) para meter la app web en una app de Android. Puedes lanzarlo a mano desde la pestaña **Actions → Publicar versión → Run workflow**.

## Versión web (iPhone y ordenador)

La versión web se publica con GitHub Pages desde el mismo proceso que crea el APK. Para activarla una sola vez:

1. En el repositorio, ve a **Settings → Pages**.
2. En **Source** elige **GitHub Actions**.
3. Ve a **Actions → Publicar versión → Run workflow** (o sube cualquier cambio a `main`).

En uno o dos minutos estará en **https://n23gr045.github.io/Reparto-de-deudas-/**.

### Instalarla en el iPhone

1. Abre la dirección de la versión web en **Safari**.
2. Pulsa el botón **Compartir** y elige **Añadir a pantalla de inicio**.
3. Se abrirá a pantalla completa, con su icono, y funcionará también sin conexión.

## Actualizaciones

Cada cambio que se sube a `main` publica una versión nueva (1.1, 1.2, 1.3…), con el APK en Releases y la web en Pages. Las novedades salen del mensaje del commit.

- **En Android**, la app consulta Releases al abrirse (como mucho cada 6 horas) y, si hay una versión nueva, muestra un aviso con las novedades y el botón **Descargar e instalar**. El APK nuevo se instala encima y conserva tus datos.
- **En la web y en el iPhone**, la app avisa de la versión nueva y se actualiza con **Actualizar ahora**.
- En **Personalizar → Actualizaciones** ves tu versión, puedes buscar a mano y desactivar la búsqueda automática.

## Tus datos

- Todo se guarda en el almacenamiento local del navegador del dispositivo donde uses la app. No se envía nada a ningún servidor.
- Si borras los datos de la app o del navegador, o cambias de móvil, se pierden. Usa **Personalizar → Exportar copia** de vez en cuando. En la web se descarga un archivo; en el APK la copia se pone en el portapapeles para que la pegues en una nota. Para recuperarla usa **Importar copia** o **Pegar una copia en texto**.
- La app de la pantalla de inicio y Safari guardan sus datos por separado en el iPhone. Usa siempre la misma.

## Estructura

```
index.html              La app completa (HTML, CSS y JavaScript)
manifest.webmanifest    Nombre, colores e iconos para instalarla
sw.js                   Permite abrir la web sin conexión
icons/                  Iconos de la web
assets/                 Icono y pantalla de carga del APK
android-config/         Firma fija del APK, para que las actualizaciones se instalen encima
capacitor.config.json   Configuración de la app Android
package.json            Dependencias para compilar el APK
.github/workflows/      Publicación automática del APK y de la web
```

## Licencia

MIT. Consulta el archivo [LICENSE](LICENSE).
