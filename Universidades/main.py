import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(layout="wide", page_title="Dashboard de Universidades BA")

@st.cache_data
def load_data():
    df = pd.read_csv("universidades.csv", sep=";")
    
    # Limpieza de coordenadas
    def clean_coord(coord):
        if isinstance(coord, str):
            return float(coord.replace('.', '')) / 10**6
        return float(coord)
    
    df['lat'] = df['lat'].apply(clean_coord)
    df['long'] = df['long'].apply(clean_coord)
    
    # Limpieza de otros campos
    df['regimen'] = df['regimen'].str.strip()
    df['comuna'] = df['comuna'].fillna('Desconocida').astype(str)
    
    return df

def show_general_stats(df):
    st.subheader("Estadísticas Generales")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Instituciones", len(df))
    
    with col2:
        st.metric("Instituciones Públicas", len(df[df['regimen'] == 'Público']))
    
    with col3:
        st.metric("Instituciones Privadas", len(df[df['regimen'] == 'Privado']))
    
    # Gráfico de distribución
    fig = px.pie(df, names='regimen', title='Distribución Público/Privado',
                 color='regimen', color_discrete_map={'Público': 'blue', 'Privado': 'green'})
    st.plotly_chart(fig, use_container_width=True)

def show_interactive_map(df):
    st.subheader("Mapa de Universidades")
    
    # Filtrar filas con coordenadas válidas
    map_df = df.dropna(subset=['lat', 'long'])
    
    if map_df.empty:
        st.warning("No hay datos con coordenadas válidas para mostrar el mapa.")
        return
    
    # Crear mapa centrado en Buenos Aires
    m = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)
    
    # Añadir marcadores
    for idx, row in map_df.iterrows():
        popup_content = f"""
        <b>{row.get('universida', 'Universidad')}</b><br>
        <i>{row.get('unidad_aca', 'Unidad académica')}</i><br>
        Tipo: {row.get('regimen', 'N/A')}<br>
        Dirección: {row.get('direccion_norm', 'N/A')}<br>
        Teléfono: {row.get('telef', 'N/A')}<br>
        Web: {row.get('web', 'N/A')}
        """
        
        folium.Marker(
            location=[row['lat'], row['long']],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=row.get('universida', 'Universidad'),
            icon=folium.Icon(
                color='blue' if row.get('regimen') == 'Público' else 'green',
                icon='university' if row.get('regimen') == 'Público' else 'book'
            )
        ).add_to(m)
    
    # Mostrar mapa en Streamlit
    folium_static(m, width=1000, height=600)

def show_filters_and_table(df):
    st.sidebar.header("Filtros Avanzados")
    
    # Filtro por nombre
    search_term = st.sidebar.text_input("Buscar por nombre de universidad o unidad académica")
    
    # Filtro por régimen
    regimen_options = ['Todos'] + list(df['regimen'].unique())
    selected_regimen = st.sidebar.selectbox("Tipo de Institución", regimen_options)
    
    # Filtro por comuna
    comuna_options = ['Todas'] + sorted(df['comuna'].unique())
    selected_comuna = st.sidebar.selectbox("Comuna", comuna_options)
    
    # Filtro por área de estudio (si existe)
    if 'area' in df.columns:
        area_options = ['Todas'] + sorted(df['area'].unique())
        selected_area = st.sidebar.selectbox("Área de Estudio", area_options)
    
    # Aplicar filtros
    filtered_df = df.copy()
    
    if search_term:
        mask = (filtered_df['universida'].str.contains(search_term, case=False, na=False) | 
                filtered_df['unidad_aca'].str.contains(search_term, case=False, na=False))
        filtered_df = filtered_df[mask]
    
    if selected_regimen != 'Todos':
        filtered_df = filtered_df[filtered_df['regimen'] == selected_regimen]
    
    if selected_comuna != 'Todas':
        filtered_df = filtered_df[filtered_df['comuna'] == selected_comuna]
    
    if 'area' in df.columns and selected_area != 'Todas':
        filtered_df = filtered_df[filtered_df['area'] == selected_area]
    
    # Mostrar resultados
    st.subheader(f"Resultados de Búsqueda ({len(filtered_df)} instituciones encontradas)")
    
    # Mostrar tabla con más información
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

def show_author_section():
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

def main():
    st.title("🏛️ Dashboard de Universidades de Buenos Aires")
    st.markdown("Exploración interactiva de instituciones educativas universitarias en la Ciudad de Buenos Aires")
    
    # Cargar datos
    df = load_data()
    
    # Mostrar secciones
    show_general_stats(df)
    show_interactive_map(df)
    show_study_areas(df)
    show_filters_and_table(df)
    
    # Mostrar sección del autor
    show_author_section()

if __name__ == "__main__":
    main()