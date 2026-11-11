"""Actualiza data/grilla.json desde una exportación de la grilla de clipping.

Uso: python3 -I scripts/actualizar_grilla.py <exportacion.json> <carpeta_del_repo>

La exportación es la respuesta de la hoja "Grilla de Clipping" leída desde la
fila 4500 (objeto con "values" o lista de filas). Solo se publican las filas de
la campaña "LANZAMIENTO FIAT 600", con columnas públicas, y los enlaces internos
de Google Drive se reemplazan por un identificador anónimo (sirve para no contar
dos veces la misma pieza). Si cambia el número de registros, suma una línea al
historial. Imprime "SIN CAMBIOS" o "ACTUALIZADO".
"""
import datetime, hashlib, json, sys, urllib.parse

src, repo = sys.argv[1], sys.argv[2]
FILA_INICIAL = 4500
COLS = ['marca', 'fecha', 'titulo', 'medio', 'tipo_medio', 'link', 'usuario', 'seguidores', 'duracion', 'campana', 'subtema', 'gestion', 'valor_pagado', 'voceria', 'exclusividad', 'branding', 'imagen_marca', 'mencion_titulo', 'tier', 'reputacion']
PUBLICAS = ['fila', 'marca', 'fecha', 'titulo', 'medio', 'tipo_medio', 'link', 'campana', 'gestion', 'voceria', 'tier', 'reputacion']

raw = json.load(open(src))
values = raw.get('values', raw.get('content', {}).get('values', [])) if isinstance(raw, dict) else raw
rows = []
for i, r in enumerate(values):
    o = {c: ('' if j >= len(r) or r[j] is None else str(r[j])) for j, c in enumerate(COLS)}
    o['fila'] = str(FILA_INICIAL + i)
    if o['campana'].strip().upper() != 'LANZAMIENTO FIAT 600':
        continue
    host = urllib.parse.urlparse(o['link']).netloc
    if 'drive.google' in host or 'docs.google' in host:
        o['link'] = 'interno:' + hashlib.sha256(o['link'].encode()).hexdigest()[:16]
    rows.append({k: o[k] for k in PUBLICAS})
if not rows:
    sys.exit('ERROR: la exportación no trae filas de la campaña; no se cambia nada.')

path = f'{repo}/data/grilla.json'
prev = json.load(open(path))
if prev == rows:
    print('SIN CAMBIOS'); sys.exit(0)
json.dump(rows, open(path, 'w'), ensure_ascii=False, indent=1)

ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
meta_path = f'{repo}/data/meta.json'
meta = json.load(open(meta_path))
meta.update(actualizado=ahora.strftime('%d/%m/%Y %H:%M'), registros_campana=len(rows))
json.dump(meta, open(meta_path, 'w'), ensure_ascii=False, indent=1)

links = lambda rs: {r['link'] or (r['medio'] + r['titulo'] + r['fecha']) for r in rs}
nuevos = len(links(rows) - links(prev))
hist_path = f'{repo}/data/historial.json'
hist = json.load(open(hist_path))
hist.append(dict(fecha=ahora.strftime('%Y-%m-%d %H:%M'), version='Actualización automática',
    cambio=f'Lectura de la grilla de clipping: {len(rows)} registros de la campaña ({nuevos} piezas nuevas o modificadas). Las publicaciones repetidas no se suman.',
    fuente='Grilla de clipping'))
json.dump(hist, open(hist_path, 'w'), ensure_ascii=False, indent=1)
print('ACTUALIZADO', len(rows), nuevos)
