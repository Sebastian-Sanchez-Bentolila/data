# 📚 Dashboard de Bibliotecas CABA

![Dashboard Preview](https://github.com/Sebastian-Sanchez-Bentolila/data/tree/main/Bibliotecas/src/dashboard.png) 

**Visualización interactiva de bibliotecas públicas y populares de la Ciudad Autónoma de Buenos Aires**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bibliotecas-CABA.streamlit.app/) 

[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)
[![GitHub Issues](https://img.shields.io/github/issues/tuusuario/turepo)](https://github.com/tuusuario/turepo/issues)

## 🌟 Características

- 🗂️ **Datos completos** de 50+ bibliotecas
- 📍 Filtrado por comuna, barrio y tipo
- 📊 Visualizaciones interactivas con Plotly
- 🔍 Búsqueda inteligente por nombre
- 📱 Diseño responsive para cualquier dispositivo

## 🚀 Instalación Local

1. **Clonar el repositorio**:
```bash
git clone https://github.com/Sebastian-Sanchez-Bentolila/data/bibliotecas.git
cd dashboard-bibliotecas
```

2. **Configurar entorno virtual**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**:
```bash
streamlit run main.py
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Lógica principal |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white) | Interfaz web |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) | Procesamiento de datos |
| ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly) | Visualizaciones |

## 📂 Estructura del Proyecto

```
.
├── data/
│   └── biblioteca.csv       # Dataset principal
├── src/                     # Archivos
|   └── dashboard.png        
├── main.py                  # Código principal
├── requirements.txt         # Dependencias
├── LICENSE
└── README.md
```

## 🤝 Cómo Contribuir

1. Haz fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📌 Roadmap

- [x] Versión inicial
- [ ] Integración con mapas interactivos
- [ ] Sistema de rating de bibliotecas
- [ ] Panel administrativo

## 📧 Contacto

**Sebastian Sanchez Bentolila**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin)](https://www.linkedin.com/in/sebastian-sanchez-bentolila/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github)](https://github.com/Sebastian-Sanchez-Bentolila)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?logo=)](https://sebastian-sanchez-bentolila.netlify.app/)

✉️ sebastiansb3004@gmail.com

---

*"La ciencia de datos es el arte de convertir datos en decisiones."* 
```