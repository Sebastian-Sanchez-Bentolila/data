import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime
from shapely import wkt

# Configuración de la página
st.set_page_config(layout="wide", page_title="Dashboard de Universidades BA", page_icon="🎓")

# Estilos CSS personalizados
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #f7f9fc;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #34495e;
        }
        .block-container {
            padding: 2rem;
        }
        hr {
            border: 0;
            height: 2px;
            background: #e0e0e0;
            margin: 2rem 0;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("data\\universidades.csv", sep=";")
    
    df['regimen'] = df['regimen'].str.strip()
    df['comuna'] = df['comuna'].fillna('Desconocida').astype(str)
    
    return df

def show_general_stats(df):
    st.markdown("## 📊 Estadísticas Generales")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Instituciones", len(df))
    
    with col2:
        st.metric("Públicas", len(df[df['regimen'] == 'Público']))
    
    with col3:
        st.metric("Privadas", len(df[df['regimen'] == 'Privado']))

    fig = px.pie(df, names='regimen', title='Distribución Público / Privado',
                 color='regimen', color_discrete_map={'Público': '#4fc3f7', 'Privado': '#a5d6a7'},
                 hole=0.4)
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

def show_interactive_map(df):
    st.subheader("📍 Mapa Interactivo de Universidades en CABA")

    # Convertir la columna WKT_gkba a geometría y extraer coordenadas
    df["geometry"] = df["WKT_gkba"].apply(wkt.loads)
    df["lon"] = df["geometry"].apply(lambda p: p.x)
    df["lat"] = df["geometry"].apply(lambda p: p.y)

    # Crear mapa centrado en CABA
    mapa = folium.Map(location=[-34.61, -58.38], zoom_start=12, tiles="CartoDB Positron")

    # Agregar marcadores
    for _, row in df.iterrows():
        nombre = row['universida']
        direccion = row['direccion_norm']
        barrio = row['barrio']
        regimen = row['regimen']
        color = 'blue' if regimen == 'Privado' else 'green'
        
        popup_content = f"""
        <b>{nombre}</b><br>
        <i>{regimen}</i><br>
        <b>Dirección:</b> {direccion}<br>
        <b>Barrio:</b> {barrio}
        """
        
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=folium.Popup(popup_content, max_width=250),
            tooltip=nombre,
            icon=folium.Icon(color=color)
        ).add_to(mapa)


    folium_static(mapa, width=1000, height=600)


def show_author():
    with st.container():
        st.header("🧑💻 Sobre el Autor")
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.image("https://avatars.githubusercontent.com/u/97362291?v=4", 
                    width=150, 
                    caption="Sebastian Sanchez Bentolila")
        
        with col2:
            st.markdown("""
            **Data Science Student** | Universidad Nacional Guillermo Brown  
            
            🔧 **Stack técnico:**  
            <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" width="70">
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white" width="80">
            <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" width="75">
            <img src="https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white" width="75">
            
            🌐 **Enlaces:**  
            [Portfolio](https://sebastian-sanchez-bentolila.netlify.app/) • 
            [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila/) • 
            [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)  
            
            📫 **Contacto:** sebastiansb3004@gmail.com  
            
            *"La ciencia de datos es el arte de convertir datos en decisiones."*
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    st.markdown(f"🔄 Actualizado: {datetime.now().strftime('%B %Y')}")

def show_filters_and_table(df):
    st.sidebar.header("🎯 Filtros Avanzados")

    search_term = st.sidebar.text_input("🔎 Buscar por nombre")
    regimen_options = ['Todos'] + list(df['regimen'].unique())
    selected_regimen = st.sidebar.selectbox("🏛️ Tipo de Institución", regimen_options)

    comuna_options = ['Todas'] + sorted(df['comuna'].unique())
    selected_comuna = st.sidebar.selectbox("📍 Comuna", comuna_options)

    if 'area' in df.columns:
        area_options = ['Todas'] + sorted(df['area'].unique())
        selected_area = st.sidebar.selectbox("🎓 Área de Estudio", area_options)

    filtered_df = df.copy()

    if search_term:
        mask = (
            filtered_df['universida'].str.contains(search_term, case=False, na=False) | 
            filtered_df['unidad_aca'].str.contains(search_term, case=False, na=False)
        )
        filtered_df = filtered_df[mask]

    if selected_regimen != 'Todos':
        filtered_df = filtered_df[filtered_df['regimen'] == selected_regimen]
    
    if selected_comuna != 'Todas':
        filtered_df = filtered_df[filtered_df['comuna'] == selected_comuna]
    
    if 'area' in df.columns and selected_area != 'Todas':
        filtered_df = filtered_df[filtered_df['area'] == selected_area]

    st.markdown("## 🏫 Resultados de búsqueda")
    st.dataframe(
        filtered_df[['universida', 'unidad_aca', 'regimen', 'barrio', 'comuna', 'telef', 'web'] + (['area'] if 'area' in df.columns else [])],
        column_config={
            "universida": "Universidad",
            "unidad_aca": "Unidad Académica",
            "regimen": "Tipo",
            "barrio": "Barrio",
            "comuna": "Comuna",
            "telef": "Teléfono",
            "web": "Sitio Web",
            "area": "Área de Estudio"
        },
        hide_index=True,
        use_container_width=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)

def show_study_areas(df):
    st.subheader("Distribución por Áreas de Estudio")
    
    # Definir un mapeo más robusto de áreas de estudio
    area_keywords = {
        'Medicina': r'Medicina|Salud|Enfermería|Bioquímica|Farmacia',
        'Derecho': r'Derecho|Jurídicas|Abogacía',
        'Ingeniería': r'Ingeniería|Tecnología|Informática|Sistemas',
        'Economía': r'Económicas|Administración|Empresas|Negocios',
        'Arquitectura': r'Arquitectura|Diseño|Urbanismo',
        'Psicología': r'Psicología|Salud Mental',
        'Sociales': r'Sociales|Humanidades|Educación|Comunicación',
        'Artes': r'Artes|Música|Teatro|Cine',
        'Ciencias': r'Ciencias|Física|Química|Matemática|Biología'
    }
    
    # Crear columna de área basada en coincidencias
    df['area'] = 'Otra'
    for area, pattern in area_keywords.items():
        mask = df['unidad_aca'].str.contains(pattern, case=False, na=False)
        df.loc[mask, 'area'] = area
    
    # Filtrar y contar áreas
    area_counts = df['area'].value_counts().reset_index()
    area_counts.columns = ['Área de Estudio', 'Cantidad']
    
    # Ordenar por cantidad
    area_counts = area_counts.sort_values('Cantidad', ascending=False)
    
    # Crear gráfico
    fig = px.bar(area_counts, 
                 x='Área de Estudio', 
                 y='Cantidad',
                 title='Distribución de Áreas de Estudio',
                 color='Área de Estudio',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    
    fig.update_layout(
        xaxis_title='Área de Estudio',
        yaxis_title='Cantidad de Unidades Académicas',
        showlegend=False,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    st.title("🏛️ Dashboard de Universidades de Buenos Aires")
    st.markdown("Exploración interactiva de instituciones educativas universitarias en la Ciudad Autónoma de Buenos Aires")
    df = load_data()
    show_general_stats(df)
    show_filters_and_table(df)
    show_interactive_map(df)
    show_study_areas(df)
    show_author()