# 🚗 Análisis de Siniestros Viales en CABA (2019-2023)

Este proyecto tiene como objetivo analizar los siniestros viales ocurridos en la Ciudad Autónoma de Buenos Aires entre 2019 y 2023, utilizando datos públicos del GCBA y metodologías de análisis de datos, visualización y ciencia de datos.

---

## 📌 Objetivos del Proyecto

- Explorar la distribución temporal y geográfica de los siniestros.
- Caracterizar a las víctimas según edad, género, rol y gravedad.
- Evaluar los modos de transporte implicados (autos, motos, peatones, bicis, etc).
- Identificar zonas críticas con mayor cantidad de siniestros.
- Desarrollar modelos predictivos sobre la gravedad del siniestro.
- Visualizar los resultados en un dashboard interactivo.

---

## 🧰 Tecnologías utilizadas

- **Python 3.x** 🐍
- **Pandas** y **NumPy** para el procesamiento de datos
- **Matplotlib**, **Seaborn** y **Plotly** para visualización
- **Folium / Geopandas** para mapas interactivos
- **Scikit-learn** para modelado (opcional)
- **Jupyter Notebooks** para exploración y análisis
- **Streamlit** para interfaz visual (opcional)
- **Airflow / Cron** para automatización (opcional)

---

## 🗃️ Estructura del repositorio

```
siniestros-caba/
├── data/                      # Datasets originales
│   ├── siniestros_viales_hechos.csv
│   ├── siniestros_viales_victimas.csv
│   └── NOTAS_SINIESTROS_VIALES_2019-2023.pdf
│
├── notebooks/                # Análisis exploratorio y visualizaciones
│   ├── 01_exploracion_inicial.ipynb
│   ├── 02_eda_visualizaciones.ipynb
│   ├── 03_modelos_predictivos.ipynb
│   └── 04_mapa_interactivo.ipynb
│
├── src/                      # Código fuente modularizado
│   ├── limpieza\_datos.py
│   ├── utils.py
│   └── modelos.py
│
├── output/                   # Resultados y datasets procesados
│   ├── graficos/
│   └── datasets\_procesados/
│
├── README.md
├── requirements.txt
└── LICENSE

```

---

## 📊 Dataset

Fuente: [Buenos Aires Data](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales)

- `siniestros_viales_hechos.csv`: Registro por siniestro (fecha, hora, lugar, gravedad).
- `siniestros_viales_victimas.csv`: Registro por víctima (edad, género, rol, vehículo).
- `NOTAS_SINIESTROS_VIALES_2019-2023.pdf`: Documento metodológico con definiciones oficiales.

---

## 🧪 Análisis propuestos

- Temporal: por año, mes, día de semana y hora.
- Espacial: mapa de calor por comuna y coordenadas.
- Por rol: peatones, ciclistas, conductores, pasajeros.
- Por vehículo: motos, autos, transporte público, monopatines.
- Por gravedad: leves, graves, mortales.
- Análisis multivariable: relación entre rol, vehículo, edad y gravedad.
- (Opcional) Modelos predictivos de siniestros graves.

---

## 📌 Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/Sebastian-Sanchez-Bentolila/siniestros-caba.git
cd siniestros-caba
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Abrir el análisis:

```bash
jupyter notebook notebooks/01_exploracion_inicial.ipynb
```

---

## 📬 Contacto

📧 [sebastiansb3004@gmail.com](mailto:sebastiansb3004@gmail.com)
🔗 [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)
🔗 [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila)
📸 [Instagram](https://www.instagram.com/sebas_sanchez_bentolila)

---

## ⚖️ Licencia

Este proyecto se encuentra bajo la licencia MIT.
Uso libre con fines educativos y de investigación. ¡Citá si te sirvió! 🙌

---

> ✨ Proyecto en desarrollo por **Sebastian Sanchez Bentolila** | Ciencia de Datos @ UNAB 🚴‍♂️