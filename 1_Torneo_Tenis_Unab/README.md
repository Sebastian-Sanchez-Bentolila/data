# 🎾 Torneo de Tenis UNaB 2025 Dashboard

![tenis](images/tenis.png)

## 📌 Descripción

Este dashboard fue desarrollado para visualizar y analizar los resultados del **Torneo de Tenis 2025** organizado por la **Universidad Nacional Guillermo Brown**. Permite explorar estadísticas, rankings, gráficos comparativos, información de los participantes y una galería de imágenes del evento.

---

## 🎯 **Objetivos**

✅ Visualizar de forma clara y profesional los resultados del torneo  
✅ Ofrecer insights rápidos sobre rendimiento individual y grupal  
✅ Promover la actividad deportiva dentro de la comunidad universitaria  
✅ Practicar desarrollo de dashboards interactivos con **Streamlit**

---

## 💻 **Tecnologías utilizadas**

- **Python 3.10+**
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - Pillow
- **Streamlit**
- HTML & CSS (embebido para diseño personalizado)

---

## 🗂 **Estructura del proyecto**

```
📁 data/
├── estudiantes.csv
└── resultados.csv
📁 images/
├── unab\_logo.png
├── tenis.png
├── ganador1\_grupoA.jpeg
├── ganador2\_grupoA.jpeg
├── ganador3\_grupoA.jpeg
├── ganador1\_grupoB.jpeg
├── ganador2\_grupoB.jpeg
├── ganador3\_grupoB.jpeg
└── Sebas.jpg
main.py
README.md
requirements.txt
```

---

## ⚙️ **Cómo ejecutar el proyecto**

1. Cloná el repositorio:

```bash
git clone https://github.com/tuusuario/1-torneo-tenis-unab.git
cd torneo-tenis-unab
````

2. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutá la app con Streamlit:

```bash
streamlit run main.py
```

4. Abrí la URL local que se te proporcionará en la terminal (generalmente [http://localhost:8501](http://localhost:8501)).

---

## 📊 **Características principales**

* **Tabs interactivos:** Resultados, Participantes, Galería, Promoción Deportiva, Sobre el Autor
* **Gráficos avanzados:** Boxplots, scatterplots con líneas de igualdad, rankings ordenados
* **Galería de imágenes** con hover zoom
* **Footer y branding UNaB**

---

## 🙋‍♂️ **Autor**

👨‍💻 **Sebastian Sanchez Bentolila**
*Estudiante de Ciencia de Datos – UNaB*

🔗 [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila/)
🔗 [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)
📧 [sebastiansb3004@gmail.com](mailto:sebastiansb3004@gmail.com)

---

## 🚀 **Próximas mejoras**

* Formularios de inscripción integrados
* Ranking histórico de torneos
* Descarga de tablas y gráficos
* Comparativas de rendimiento con otros deportes

---

### 🎉 **¡Gracias por visitar este proyecto!**

Si te resultó útil, no dudes en dejar una estrella ⭐ en el repositorio y seguir mi trabajo para más dashboards y aplicaciones de datos.