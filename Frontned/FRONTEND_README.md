# 🌌 Autos Espaciales - Frontend

Sistema de gestión de autos con diseño glassmorphism y tema espacial violeta.

## 🚀 Características

- ✨ Diseño glassmorphism con efectos parallax
- 🎨 Tema espacial con tonos violetas
- 📱 Responsive design
- 🔄 Arquitectura desacoplada con custom hooks
- 🎯 Consumo de API REST
- ⚡ Notificaciones en tiempo real
- 🛠️ CRUD completo de autos
- ⏮️ Sistema de restauración de versiones

## 📋 Prerequisitos

- Node.js 18+
- pnpm (o npm/yarn)
- Backend API corriendo en `http://localhost:8000`

## 🔧 Instalación

```bash
# Instalar dependencias
pnpm install

# Iniciar servidor de desarrollo
pnpm dev
```

## 🏗️ Arquitectura

### Estructura de carpetas

```
src/
├── components/          # Componentes de UI
│   ├── AutoCard.jsx    # Tarjeta individual de auto
│   ├── AutoForm.jsx    # Formulario crear/editar
│   ├── AutoList.jsx    # Lista de autos
│   └── Notification.jsx # Sistema de notificaciones
├── hooks/              # Custom hooks
│   └── useAutos.js     # Hook para gestión de autos
├── apiAutos.js         # Capa de servicios API
├── App.jsx             # Componente principal
└── main.jsx            # Punto de entrada
```

### Patrón de diseño

- **Separación de responsabilidades**: Lógica de negocio en hooks, UI en componentes
- **Custom Hooks**: `useAutos` encapsula toda la lógica de estado y API
- **Servicios desacoplados**: Funciones de API en módulo separado
- **Componentes reutilizables**: Cada componente tiene una responsabilidad única

## 🎨 Diseño

### Glassmorphism
- Backdrop blur effects
- Transparencias y bordes suaves
- Sombras y efectos de profundidad

### Tema Espacial
- Gradientes violetas (#BA55D3, #9370DB, #DDA0DD)
- Fondo oscuro con estrellas animadas
- Efectos parallax con 3 capas de estrellas
- Animaciones suaves y transiciones

## 📡 Endpoints API

- `POST /autos` - Crear auto
- `GET /autos` - Listar todos
- `GET /autos/{id}` - Obtener por ID
- `PUT /autos/{id}` - Actualizar
- `DELETE /autos/{id}` - Eliminar
- `POST /autos/{id}/restore/{version}` - Restaurar versión

## 🎯 Funcionalidades

1. **Crear autos**: Formulario con marca, modelo, color, tipo y decoradores
2. **Listar autos**: Grid responsive con tarjetas glassmorphism
3. **Editar autos**: Clic en botón editar, formulario se pre-llena
4. **Eliminar autos**: Confirmación antes de eliminar
5. **Restaurar versiones**: Sistema de memento pattern
6. **Notificaciones**: Feedback visual de todas las operaciones

## 🔄 Flujo de uso

1. El usuario ve la lista de autos al cargar la página
2. Puede crear un nuevo auto usando el formulario superior
3. Cada tarjeta muestra hover effects con acciones
4. Puede editar (pre-llena formulario), eliminar o restaurar
5. Todas las operaciones muestran notificaciones de éxito/error

## 🛠️ Tecnologías

- React 18
- Vite
- CSS3 (Glassmorphism, Animations, Parallax)
- Fetch API
- Custom Hooks

## 📱 Responsive

- Desktop: Grid de 3-4 columnas
- Tablet: Grid de 2 columnas
- Mobile: Columna única

## 🎨 Paleta de colores

```css
--color-primary: #BA55D3 (Medium Orchid)
--color-secondary: #9370DB (Medium Purple)
--color-accent: #DDA0DD (Plum)
--color-bg: #0a0015 (Dark Space)
--color-text: #E6E6FA (Lavender)
```

## 🚀 Producción

```bash
# Build para producción
pnpm build

# Preview del build
pnpm preview
```

---

Creado con 💜 y React
