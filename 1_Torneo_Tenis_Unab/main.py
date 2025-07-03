import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import requests
from io import StringIO

# Configuración de la página
st.set_page_config(
    page_title="Torneo de Tenis UNaB",
    page_icon="images/tenis.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos
@st.cache_data
def load_data():
    url1 = "https://raw.githubusercontent.com/Sebastian-Sanchez-Bentolila/data/tree/main/1_Torneo_Tenis_Unab/data/estudiantes.csv"
    url2 = "https://raw.githubusercontent.com/Sebastian-Sanchez-Bentolila/data/tree/main/1_Torneo_Tenis_Unab/data/resultados.csv"

    try:
        response = requests.get(url1)
        response.raise_for_status()  # Lanza error si la solicitud falla
        estudiantes = pd.read_csv(StringIO(response.text))
        response = requests.get(url2)
        response.raise_for_status()  # Lanza error si la solicitud falla
        resultados = pd.read_csv(StringIO(response.text))
        return estudiantes, resultados
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        return pd.DataFrame()

estudiantes, resultados = load_data()

# Procesamiento de datos
def process_results(df):
    # Separar los resultados en goles a favor y en contra
    df[['GF', 'GC']] = df['Resultado'].str.split('-', expand=True).astype(int)
    
    # Crear dataframe para estadísticas
    jugadores = pd.concat([df['Estudiante_1'], df['Estudiante_2']]).unique()
    
    stats = []
    for jugador in jugadores:
        partidos_jugados = len(df[(df['Estudiante_1'] == jugador) | (df['Estudiante_2'] == jugador)])
        partidos_ganados = len(df[((df['Estudiante_1'] == jugador) & (df['GF'] > df['GC'])) | 
                                 ((df['Estudiante_2'] == jugador) & (df['GC'] > df['GF']))])
        partidos_perdidos = partidos_jugados - partidos_ganados
        puntos = partidos_ganados * 3  # 3 puntos por victoria
        
        # Calcular games a favor y en contra
        gf = df[df['Estudiante_1'] == jugador]['GF'].sum() + df[df['Estudiante_2'] == jugador]['GC'].sum()
        gc = df[df['Estudiante_1'] == jugador]['GC'].sum() + df[df['Estudiante_2'] == jugador]['GF'].sum()
        
        stats.append({
            'Jugador': jugador,
            'PJ': partidos_jugados,
            'PG': partidos_ganados,
            'PP': partidos_perdidos,
            'Puntos': puntos,
            'GF': gf,
            'GC': gc,
            'Dif': gf - gc
        })
    
    return pd.DataFrame(stats).sort_values('Puntos', ascending=False)

# Procesar estadísticas por grupo
stats_a = process_results(resultados[resultados['Grupo'] == 'A'])
stats_b = process_results(resultados[resultados['Grupo'] == 'B'])

# Función para cargar imágenes de la galería
def load_gallery_images():
    gallery_images = []
    try:
        for i in range(1, 4):
            img_a = Image.open(f"images/ganador{i}_grupoA.jpeg")
            img_b = Image.open(f"images/ganador{i}_grupoB.jpeg")
            gallery_images.extend([(f"Ganador {i} Grupo A", img_a), 
                                 (f"Ganador {i} Grupo B", img_b)])
        
        #img_ceremonia = Image.open("images/ceremonia.jpg")
        #img_partido = Image.open("images/partido.jpg")
        #gallery_images.extend([("Ceremonia de premiación", img_ceremonia),
                            #("Partido en progreso", img_partido)])
    except Exception as e:
        st.warning(f"No se pudieron cargar algunas imágenes de la galería: {str(e)}")
        # Imágenes de placeholder si no se encuentran las originales
        placeholder = Image.new('RGB', (300, 200), color='#e7f1ff')
        gallery_images = [(f"Imagen {i+1}", placeholder) for i in range(6)]
    
    return gallery_images

# Diseño de la aplicación
def main():
    # CSS personalizado
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    .title {
        color: #0056b3;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 30px;
    }
    .header {
        color: #0056b3;
        font-size: 1.8em;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .subheader {
        color: #007bff;
        font-size: 1.4em;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .winner-card {
        background-color: #e7f1ff;
        border-left: 5px solid #0056b3;
    }
    .footer {
    width: 100%;
    background-color: #0056b3;
    color: white;
    text-align: center;
    padding: 10px;
    margin-top: 30px;
    }
    .logo-container {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    .gallery-img {
        transition: transform 0.3s;
        border-radius: 8px;
    }
    .gallery-img:hover {
        transform: scale(1.03);
    }
    .author-img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo en esquina superior derecha
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        logo = Image.open("images/unab_logo.png")
        st.image(logo, width=150)
    except:
        st.write("")
    st.markdown('</div>', unsafe_allow_html=True)

    # Título principal
    st.markdown('<div class="title">Torneo de Tenis UNaB 2025</div>', unsafe_allow_html=True)
    st.markdown("**Realizado del 13 al 27 de Junio de 2025 en el predio del Club San Albano (Espora 4920, Burzaco)**")
    
    # Pestañas
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏆 Resultados", "👥 Participantes", "📷 Galería", "🎾 Promoción Deportiva", "👨‍💻 Sobre el Autor"])

    with tab1:
        st.markdown('<div class="header">Resultados del Torneo</div>', unsafe_allow_html=True)
        
        # Selector de grupo
        grupo_seleccionado = st.selectbox("Selecciona un grupo:", ['Todos', 'Grupo A', 'Grupo B'])
        
        # Mostrar estadísticas según selección
        if grupo_seleccionado == 'Todos':
            st.markdown('<div class="subheader">Tabla General</div>', unsafe_allow_html=True)
            st.dataframe(pd.concat([stats_a, stats_b]).sort_values('Puntos', ascending=False).reset_index(drop=True))
            
            # Gráficos comparativos
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<div class="subheader">Distribución de Puntos por Grupo</div>', unsafe_allow_html=True)
                fig, ax = plt.subplots()
                sns.boxplot(data=pd.concat([stats_a.assign(Grupo='A'), stats_b.assign(Grupo='B')]), 
                           x='Grupo', y='Puntos', palette=['#0056b3', '#007bff'])
                ax.set_title('Distribución de Puntos por Grupo')
                st.pyplot(fig)
            
            with col2:
                st.markdown('<div class="subheader">Relación Games a Favor/En Contra</div>', unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig, ax = plt.subplots()
                sns.scatterplot(data=pd.concat([stats_a.assign(Grupo='A'), stats_b.assign(Grupo='B')]),
                                x='GF', y='GC', hue='Grupo', palette=['#0056b3', '#007bff'], s=100)

                # Línea de igualdad
                lims = [
                    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
                    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
                ]
                ax.plot(lims, lims, '--k', alpha=0.5)
                ax.set_aspect('equal')
                ax.set_title('Games a favor vs. games en contra')
                st.pyplot(fig)
                
            with col3:
                st.markdown('<div class="subheader">Promedio de Puntos por Grupo</div>', unsafe_allow_html=True)
                promedios = pd.DataFrame({
                    'Grupo': ['A', 'B'],
                    'Puntos': [stats_a['Puntos'].mean(), stats_b['Puntos'].mean()]
                })

                fig, ax = plt.subplots()
                sns.barplot(data=promedios, x='Grupo', y='Puntos', palette=['#0056b3', '#007bff'])
                ax.set_title('Promedio de puntos por grupo')
                st.pyplot(fig)            

        else:
            grupo = grupo_seleccionado[-1]
            stats = stats_a if grupo == 'A' else stats_b
            
            st.markdown(f'<div class="subheader">Tabla de Posiciones - Grupo {grupo}</div>', unsafe_allow_html=True)
            st.dataframe(stats.sort_values('Puntos', ascending=False).reset_index(drop=True))
            
            # Podio de ganadores
            st.markdown(f'<div class="subheader">Podio - Grupo {grupo}</div>', unsafe_allow_html=True)
            
            cols = st.columns(3)
            for i, (_, row) in enumerate(stats.sort_values('Puntos', ascending=False).head(3).iterrows()):
                with cols[1 if i == 0 else (0 if i == 1 else 2)]:
                    try:
                        img = Image.open(f"images/ganador{i+1}_grupo{grupo}.jpg")
                        st.image(img, width=150, caption=f"{i+1}° Lugar: {row['Jugador']}")
                    except:
                        st.markdown(f"""
                        <div class="card {'winner-card' if i == 0 else ''}">
                            <h3>{i+1}° Lugar</h3>
                            <p><strong>{row['Jugador']}</strong></p>
                            <p>Puntos: {row['Puntos']}</p>
                            <p>PG: {row['PG']} | PP: {row['PP']}</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Resultados por jornada
            st.markdown(f'<div class="subheader">Resultados por Jornada - Grupo {grupo}</div>', unsafe_allow_html=True)
            jornadas = resultados[resultados['Grupo'] == grupo]['Jornada'].unique()
            
            for jornada in sorted(jornadas):
                st.markdown(f'**Jornada {jornada}**')
                jornada_df = resultados[(resultados['Grupo'] == grupo) & (resultados['Jornada'] == jornada)]
                st.dataframe(jornada_df[['Estudiante_1', 'Estudiante_2', 'Resultado']].rename(
                    columns={'Estudiante_1': 'Jugador 1', 'Estudiante_2': 'Jugador 2'}))

    with tab2:
        st.markdown('<div class="header">Información de los Participantes</div>', unsafe_allow_html=True)
        
        # Selector de grupo para participantes
        grupo_part = st.selectbox("Selecciona un grupo para ver participantes:", ['Todos', 'Grupo A', 'Grupo B'], key='grupo_part')
        
        if grupo_part == 'Todos':
            df_mostrar = estudiantes
        else:
            grupo = grupo_part[-1]
            df_mostrar = estudiantes[estudiantes['Grupo'] == grupo]
        
        st.dataframe(df_mostrar.sort_values(['Grupo', 'Apellido']).reset_index(drop=True))
        
        # Estadísticas demográficas
        st.markdown('<div class="subheader">Estadísticas de los Participantes</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('**Distribución por Carrera**')
            carrera_counts = estudiantes['Carrera'].value_counts().sort_values()
            total = carrera_counts.sum()

            fig, ax = plt.subplots(figsize=(8, 6))

            # Colores
            colors = plt.cm.Blues(np.linspace(0.5, 1, len(carrera_counts)))

            # Barras horizontales
            bars = ax.barh(carrera_counts.index, carrera_counts.values, color=colors)

            # Etiquetas en cada barra
            for bar in bars:
                width = bar.get_width()
                porcentaje = (width / total) * 100
                ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
                        f"{int(width)} ({porcentaje:.1f}%)",
                        va='center', fontsize=10)

            # Títulos y diseño
            ax.set_xlabel("Cantidad de estudiantes")
            ax.set_title("Distribución de estudiantes por carrera", fontsize=14, color="#0056b3", pad=15)
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)

            st.pyplot(fig)
        
        with col2:
            st.markdown('**Distribución por Edad**')
            fig, ax = plt.subplots()
            sns.histplot(estudiantes['Edad'], bins=10, kde=True, color='#0056b3')
            ax.set_title('Distribución de Edades', fontsize=14, color="#0056b3", pad=15)
            ax.set_xlabel('Edad')
            st.pyplot(fig)
            
        with col3:
            st.markdown('**Distribución de Edades por Carrerra**')
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(data=estudiantes, x='Carrera', y='Edad', palette='Blues', ax=ax)
            ax.set_title('Distribución de edades por carrera', fontsize=14, color="#0056b3", pad=15)
            ax.set_xlabel('Carrera')
            ax.set_ylabel('Edad')
            plt.xticks(rotation=45)
            st.pyplot(fig)


    with tab3:
        st.markdown('<div class="header">Galería del Torneo</div>', unsafe_allow_html=True)
        
        gallery_images = load_gallery_images()
        
        # Mostrar imágenes en una cuadrícula
        cols = st.columns(3)
        for idx, (title, img) in enumerate(gallery_images):
            with cols[idx % 3]:
                st.markdown(f'<div class="gallery-img">', unsafe_allow_html=True)
                st.image(img, caption=title, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown("""<div class="header">Promoción Deportiva</div>""", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("""
            ### El Deporte en la UNaB
            
            En la Universidad Nacional Guillermo Brown creemos en el deporte como herramienta para el crecimiento personal, 
            la disciplina y la salud física y mental. El torneo de tenis es solo una de las muchas actividades deportivas 
            que organizamos durante el año.
            
            El tenis fortalece habilidades como:
            """)
            
            st.markdown("""
            - 🎯 Concentración y enfoque
            - ⚡ Toma de decisiones bajo presión
            - 💪 Perseverancia y resiliencia
            - 🏆 Competitividad
            """)
            
            st.markdown("¡Anímate a sumarte a las actividades deportivas y a estos torneos internos!")
        
        # Enlace a deportes UNaB
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://www.unab.edu.ar/deportes/" target="_blank">
                <button style="background-color: #0056b3; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                    Más información sobre deportes en la UNaB
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="header">Sobre el Autor</div>', unsafe_allow_html=True)
        
        # Información del autor - Versión mejorada
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                author_img = Image.open("images/Sebas.jpg")
                st.image(author_img, width=200, caption="Sebastian Sanchez Bentolila")
            except:
                st.markdown("""
                <div style="text-align: center;">
                    <div style="background-color: #e7f1ff; width: 200px; height: 200px; border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center;">
                        <span style="color: #0056b3; font-size: 24px;">SB</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""                
                **Sebastian Sanchez Bentolila**  
                *Estudiante de Ciencia de Datos – UNaB*  
                
                > "Apasionado por el análisis de datos, el deporte y la tecnología aplicada a la educación y el bienestar."
                
                🔗 [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila/)  
                🔗 [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)  
                📧 sebastiansb3004@gmail.com
                
                ---
                
                ### Acerca de este Dashboard
                
                Este dashboard fue desarrollado de forma independiente con el fin de mostrar
                
                **Tecnologías utilizadas:**
                - Python (Numpy, Pandas, Matplotlib, Seaborn)
                - Streamlit para la interfaz web
                - Visualizaciones interactivas
            """)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2024 Universidad Nacional Guillermo Brown - Todos los derechos reservados</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
