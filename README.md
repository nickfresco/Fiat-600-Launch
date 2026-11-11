# FIAT 600 · Launch Intelligence Report (versión web)

Copia pública y de solo lectura del dashboard de lanzamiento del FIAT 600 Hybrid, preparada por ALTA Comunicación para Stellantis Chile.

- Sitio estático: `index.html` + datos en `data/`. No necesita compilación ni variables de entorno.
- Los datos publicados ya están depurados: sin correos, teléfonos ni notas internas.
- Cada cambio que se sube a la rama `main` se publica solo en Vercel.

## Actualizar los datos

Pídele a Claude: "actualiza el dashboard web del Fiat 600". Claude lee la grilla de clipping, regenera los archivos de `data/`, los sube a este repositorio y Vercel publica la nueva versión en uno o dos minutos. El historial de cambios aparece en la pestaña Next Steps.

## Archivos de datos

| Archivo | Contenido |
|---|---|
| `data/grilla.json` | Publicaciones de la campaña "LANZAMIENTO FIAT 600" (columnas públicas de la grilla) |
| `data/cuentas.json` | Canal de cada cuenta (medio, cuenta personal de periodista o creador) |
| `data/seguimiento.json` | Invitados y estado de publicación |
| `data/comentarios.csv` | Comentarios públicos de usuarios, anonimizados y clasificados |
| `data/insights.json`, `riesgos.json`, `plan.json`, `pendientes.json` | Análisis y próximos pasos |
| `data/historial.json`, `meta.json` | Historial de versiones y fecha de actualización |
