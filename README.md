# Reparto de Deudas

App web para el móvil donde apuntas quién te debe dinero, registras lo que te van devolviendo y repartes gastos compartidos entre amigos. Está pensada para el iPhone y se puede instalar en la pantalla de inicio como si fuera una app.

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

## Dónde está publicada

La app se publica sola con GitHub Pages desde la rama `main`:

**https://n23gr045.github.io/Reparto-de-deudas-/**

Cada vez que subes un cambio a `main`, la web se actualiza en uno o dos minutos.

## Instalarla en el iPhone

1. Abre **https://n23gr045.github.io/Reparto-de-deudas-/** en **Safari**.
2. Pulsa el botón **Compartir** y elige **Añadir a pantalla de inicio**.
3. Se abrirá a pantalla completa, con su icono, y funcionará también sin conexión.

## Tus datos

- Todo se guarda en el almacenamiento local del navegador del dispositivo donde uses la app. No se envía nada a ningún servidor.
- Si borras los datos de Safari o cambias de móvil, se pierden. Usa **Personalizar → Exportar copia** de vez en cuando y guarda el archivo en iCloud Drive o donde prefieras. Con **Importar copia** lo recuperas.
- La app de la pantalla de inicio y Safari guardan sus datos por separado en el iPhone. Usa siempre la misma.

## Estructura

```
index.html              La app completa (HTML, CSS y JavaScript)
manifest.webmanifest    Nombre, colores e iconos para instalarla
sw.js                   Permite abrirla sin conexión
icons/                  Iconos de la app
```

## Licencia

MIT. Consulta el archivo [LICENSE](LICENSE).
