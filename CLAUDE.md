# Dashboard web FIAT 600 (Vercel)

Sitio estático publicado en https://600-blue.vercel.app desde la rama `main`. Cada push a `main` se despliega solo.

## Actualizar la grilla (tarea programada o pedido de Nicolás)
1. Leer con el conector de Google Sheets el rango `'Grilla de Clipping'!A4500:T8000` de la hoja `1y1rMwAh1Ii-8y4e-NWlWcYt4BIUOgXfgde6LnlrlzzE` y guardar la respuesta JSON completa en un archivo temporal (fuera del repo).
2. `python3 -I scripts/actualizar_grilla.py <archivo> .`
3. Si imprime `ACTUALIZADO`: commit de `data/` con mensaje "Actualización de datos de la grilla" y `git push origin main`. Si imprime `SIN CAMBIOS`, no hacer nada.

## Reglas
- La versión pública no lleva correos, teléfonos, contactos de periodistas, notas internas de ALTA ni contenido de conversaciones privadas. No subir nada de eso.
- No agregar credenciales, tokens ni variables de entorno.
- Los demás archivos de `data/` (insights, riesgos, plan, seguimiento, comentarios) solo se cambian cuando Nicolás lo pide.
