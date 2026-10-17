#!/usr/bin/env python3
"""Genera las notas de una versión a partir de los commits desde la versión anterior.

Uso: python3 .github/scripts/notas.py <número de versión> > notas.md

Cada viñeta del mensaje del commit («- Algo nuevo») es una novedad. Si el commit
no tiene viñetas, se usa su título. Se clasifican solas en Nuevo, Mejoras y
Correcciones según cómo empiezan.
"""
import re, subprocess, sys, unicodedata
from datetime import date

build = sys.argv[1] if len(sys.argv) > 1 else "?"

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout

tags = [t for t in git("tag", "--list", "apk-v*", "--sort=-v:refname").split() if t != f"apk-v{build}"]
import os
rango = os.environ.get("NOTAS_RANGO") or (f"{tags[0]}..HEAD" if tags else "HEAD~1..HEAD")
log = git("log", "--no-merges", "--format=%B%x1e", rango)
commits = [c.strip() for c in log.split("\x1e") if c.strip()]

TRAILER = re.compile(r"^(co-authored-by|claude-session|signed-off-by):", re.I)
def sin_tildes(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn").lower()

items = []
for c in commits:
    lines = [l.rstrip() for l in c.splitlines() if not TRAILER.match(l.strip())]
    if not lines:
        continue
    title = lines[0].strip()
    if re.search(r"\breadme\b|documentaci", sin_tildes(title)):
        continue
    bullets, cur = [], None
    for l in lines[1:]:
        if re.match(r"^\s*[-*•]\s+", l):
            cur = re.sub(r"^\s*[-*•]\s+", "", l).strip(); bullets.append(cur)
        elif cur is not None and l.strip() and l.startswith((" ", "\t")):
            bullets[-1] += " " + l.strip()
        elif not l.strip():
            cur = None
    for b in (bullets or [title]):
        b = b.rstrip(".") + "."
        b = b[0].upper() + b[1:]
        if b not in items:
            items.append(b)

NUEVO = ("menu ", "recordatorio", "actualizar el apk", "nuevo", "nueva", "nuevos", "nuevas", "anad", "ahora se puede", "ahora puedes", "se pueden", "se puede", "boton", "pantalla de bienvenida", "version en ingles")
FIX = ("arregl", "correg", "solucion", "fallo", "error", "ya no se queda", "se quedaba", "no funcionaba")
secciones = {"Nuevo": [], "Mejoras": [], "Correcciones": []}
PREFIJOS = {"nuevo:": "Nuevo", "nueva:": "Nuevo", "mejora:": "Mejoras", "correccion:": "Correcciones", "arreglo:": "Correcciones"}
for it in items:
    k = sin_tildes(it)
    pref = next((p for p in PREFIJOS if k.startswith(p)), None)
    if pref:
        limpio = it[len(pref):].strip(); limpio = limpio[0].upper() + limpio[1:]
        secciones[PREFIJOS[pref]].append(limpio); continue
    if k.startswith(FIX) or any(w in k for w in ("se quedaba", "no funcionaba", "fallaba")):
        secciones["Correcciones"].append(it)
    elif k.startswith(NUEVO):
        secciones["Nuevo"].append(it)
    else:
        secciones["Mejoras"].append(it)
if not items:
    secciones["Mejoras"].append("Mejoras y correcciones.")

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
hoy = date.today()
print(f"## Novedades de la versión 1.{build}")
print(f"{hoy.day} de {MESES[hoy.month-1]} de {hoy.year}")
for nombre, lista in secciones.items():
    if lista:
        print(f"\n### {nombre}")
        for it in lista:
            print(f"- {it}")
print("\n---")
print("**Instalar en Android:** descarga `reparto-de-deudas.apk` y ábrelo. Si ya tienes la app, pulsa «Descargar e instalar» en el aviso: se instala encima y conserva tus datos.")
