import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime
from shapely import wkt
import requests
from io import StringIO

# Configuración de la página
st.set_page_config(
    layout="wide", 
    page_title="Universidades de Buenos Aires", 
    page_icon="🏛️",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para modo oscuro
st.markdown("""
    <style>
        :root {
            --primary-color: #6c8ef5;
            --secondary-color: #1e1e1e;
            --accent-color: #ff7675;
            --text-color: #e0e0e0;
            --card-bg: #2d2d2d;
        }
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: var(--text-color);
        }
        
        .main {
            background-color: var(--secondary-color);
        }
        
        .stApp {
            background: var(--secondary-color);
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--primary-color);
        }
        
        .stMetric {
            background-color: var(--card-bg);
            border-radius: 10px;
            padding: 15px;
            border-left: 4px solid var(--primary-color);
        }
        
        .stMetric > div {
            font-size: 1.1rem !important;
            color: var(--text-color) !important;
        }
        
        .stMetric > div:first-child {
            color: #a0a0a0 !important;
        }
        
        .stMetric > div:nth-child(2) {
            color: var(--primary-color) !important;
            font-weight: 600;
            font-size: 1.8rem !important;
        }
        
        .css-1v3fvcr, .stDataFrame {
            background-color: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .stSidebar {
            background-color: #1a1a1a !important;
        }
        
        .sidebar .sidebar-content {
            background: transparent !important;
        }
        
        .sidebar-selectbox label, .sidebar-textinput label {
            color: var(--text-color) !important;
        }
        
        .stSelectbox, .stTextInput {
            background-color: #333333 !important;
            color: var(--text-color) !important;
        }
        
        .st-bb, .st-at, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj, .st-ak, .st-al {
            border-color: #444444 !important;
        }
        
        hr {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(108,142,245,0.75), rgba(0,0,0,0));
            margin: 2rem 0;
        }
        
        .author-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .badge {
            display: inline-block;
            padding: 0.35em 0.65em;
            font-size: 0.75em;
            font-weight: 700;
            line-height: 1;
            color: #fff;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: 0.25rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        /* Ajustes para tablas en modo oscuro */
        .dataframe th {
            background-color: #333333 !important;
            color: var(--text-color) !important;
        }
        
        .dataframe td {
            background-color: var(--card-bg) !important;
            color: var(--text-color) !important;
        }
        
        /* Ajustes para los gráficos de Plotly */
        .js-plotly-plot .plotly, .js-plotly-plot .plotly div {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Sebastian-Sanchez-Bentolila/data/main/Universidades/data/universidades.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si la solicitud falla
        df = pd.read_csv(StringIO(response.text))
        df['regimen'] = df['regimen'].str.strip()
        df['comuna'] = df['comuna'].fillna('Desconocida').astype(str)
        return df
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def show_general_stats(df):
    st.markdown("## 📊 Panorama General")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total de Instituciones", len(df), help="Cantidad total de universidades e instituciones registradas")
    
    with col2:
        st.metric("Instituciones Públicas", len(df[df['regimen'] == 'Público']), help="Universidades de gestión estatal")
    
    with col3:
        st.metric("Instituciones Privadas", len(df[df['regimen'] == 'Privado']), help="Universidades de gestión privada")
    
    with col4:
        st.metric("Comunas con oferta", df['comuna'].nunique(), help="Cantidad de comunas con al menos una institución")

    # Gráficos en dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.pie(df, names='regimen', title='Distribución por Tipo de Gestión',
                    color='regimen', 
                    color_discrete_map={'Público': '#6c8ef5', 'Privado': '#ff7675'},
                    hole=0.4)
        fig.update_traces(textinfo='percent+label', 
                         marker=dict(line=dict(color='#2d2d2d', width=1)))
        fig.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0')
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        comuna_counts = df['comuna'].value_counts().reset_index()
        comuna_counts.columns = ['Comuna', 'Cantidad']
        fig = px.bar(comuna_counts, x='Comuna', y='Cantidad', 
                     title='Distribución por Comuna',
                     color='Comuna',
                     color_discrete_sequence=px.colors.qualitative.Dark24)
        fig.update_layout(
            showlegend=False, 
            xaxis_title="", 
            yaxis_title="Cantidad",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0')
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

def show_interactive_map(df):
    st.markdown("## 🗺️ Mapa Georreferenciado")
    st.markdown("Explora la ubicación de todas las instituciones universitarias en la Ciudad de Buenos Aires")
    
    # Convertir la columna WKT_gkba a geometría y extraer coordenadas
    df["geometry"] = df["WKT_gkba"].apply(wkt.loads)
    df["lon"] = df["geometry"].apply(lambda p: p.x)
    df["lat"] = df["geometry"].apply(lambda p: p.y)

    # Crear mapa centrado en CABA con estilo más moderno
    mapa = folium.Map(
        location=[-34.61, -58.38], 
        zoom_start=12, 
        tiles="CartoDB dark_matter",
        control_scale=True,
        prefer_canvas=True
    )

    # Agregar marcadores con clusters para mejor visualización
    from folium.plugins import MarkerCluster
    marker_cluster = MarkerCluster().add_to(mapa)

    for _, row in df.iterrows():
        nombre = row['universida']
        direccion = row['direccion_norm']
        barrio = row['barrio']
        regimen = row['regimen']
        color = '#ff7675' if regimen == 'Privado' else '#6c8ef5'
        icono = 'university' if regimen == 'Público' else 'school'
        
        popup_content = f"""
        <div style="width: 250px; color: #333;">
            <h4 style="color: {color}; margin-bottom: 0.5rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">{nombre}</h4>
            <p style="margin: 0.25rem 0;"><strong>Tipo:</strong> {regimen}</p>
            <p style="margin: 0.25rem 0;"><strong>Dirección:</strong> {direccion}</p>
            <p style="margin: 0.25rem 0;"><strong>Barrio:</strong> {barrio}</p>
        </div>
        """
        
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=nombre,
            icon=folium.Icon(color=color, icon=icono, prefix='fa')
        ).add_to(marker_cluster)

    # Añadir control de capas
    folium.LayerControl().add_to(mapa)

    # Mostrar mapa en un contenedor con sombra
    with st.container():
        folium_static(mapa, width=1200, height=650)

    st.markdown("---")

def show_author():
    st.markdown("## 👨‍💻 Sobre el Proyecto")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("https://avatars.githubusercontent.com/u/97362291?v=4", 
                width=200, 
                caption="Sebastián Sánchez Bentolila")
    
    with col2:
        st.markdown("""
        **Científico de Datos** | Universidad Nacional Guillermo Brown  
        
        🔧 **Stack técnico:**  
        - Python • Streamlit • Pandas • Plotly • Folium  
        
        🌐 **Enlaces:**  
        [Portfolio](https://sebastian-sanchez-bentolila.netlify.app/) • 
        [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila/) • 
        [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)  
        
        📫 **Contacto:** sebastiansb3004@gmail.com  
        
        *"Los datos no son información, la información no es conocimiento, el conocimiento no es comprensión."*
        """)
        
    st.markdown(f"""
    <div style="text-align: center; color: #a0a0a0; margin-top: 1rem;">
        <i>Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}</i>
    </div>
    """, unsafe_allow_html=True)

def show_filters_and_table(df):
    st.sidebar.markdown("""
        <div style="color: var(--text-color); padding: 0.5rem 0; border-bottom: 1px solid #444; margin-bottom: 1.5rem;">
            <h2 style="color: var(--primary-color); margin: 0;">🔍 Filtros</h2>
        </div>
    """, unsafe_allow_html=True)

    # Filtro de búsqueda
    search_term = st.sidebar.text_input(
        "Buscar por nombre", 
        key="search",
        help="Busca por nombre de universidad o unidad académica"
    )
    
    # Filtros en acordeones
    with st.sidebar.expander("🏛️ Tipo de Institución", expanded=True):
        regimen_options = ['Todos'] + list(df['regimen'].unique())
        selected_regimen = st.selectbox(
            "Seleccionar tipo", 
            regimen_options,
            key="regimen",
            label_visibility="collapsed"
        )

    with st.sidebar.expander("📍 Ubicación", expanded=True):
        comuna_options = ['Todas'] + sorted(df['comuna'].unique())
        selected_comuna = st.selectbox(
            "Filtrar por comuna", 
            comuna_options,
            key="comuna",
            label_visibility="collapsed"
        )

    if 'area' in df.columns:
        with st.sidebar.expander("🎓 Área de Estudio", expanded=True):
            area_options = ['Todas'] + sorted(df['area'].unique())
            selected_area = st.selectbox(
                "Filtrar por área", 
                area_options,
                key="area",
                label_visibility="collapsed"
            )

    # Aplicar filtros
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

    # Mostrar resultados
    st.markdown("## 🏫 Resultados Filtrados")
    
    if len(filtered_df) == 0:
        st.warning("No se encontraron resultados con los filtros aplicados.")
    else:
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
            use_container_width=True,
            height=min(600, 35 * (len(filtered_df) + 1))
        )

def show_study_areas(df):
    st.markdown("## 📚 Distribución por Áreas de Estudio")
    
    # Definir un mapeo de áreas de estudio
    area_keywords = {
        'Medicina y Salud': r'Medicina|Salud|Enfermería|Bioquímica|Farmacia|Kinesiología',
        'Derecho': r'Derecho|Jurídicas|Abogacía|Notariado',
        'Ingeniería y Tecnología': r'Ingeniería|Tecnología|Informática|Sistemas|Computación',
        'Economía y Negocios': r'Económicas|Administración|Empresas|Negocios|Comercio|Contabilidad',
        'Arquitectura y Diseño': r'Arquitectura|Diseño|Urbanismo|Paisajismo',
        'Psicología': r'Psicología|Salud Mental|Terapia|Psicoanálisis',
        'Ciencias Sociales': r'Sociales|Humanidades|Educación|Comunicación|Sociología|Antropología',
        'Artes y Creatividad': r'Artes|Música|Teatro|Cine|Danza|Bellas Artes',
        'Ciencias Exactas': r'Ciencias|Física|Química|Matemática|Biología|Geología',
        'Agronomía y Alimentos': r'Agronomía|Veterinaria|Alimentos|Agricultura'
    }
    
    # Crear columna de área basada en coincidencias
    df['area'] = 'Otras Áreas'
    for area, pattern in area_keywords.items():
        mask = df['unidad_aca'].str.contains(pattern, case=False, na=False)
        df.loc[mask, 'area'] = area
    
    # Filtrar y contar áreas
    area_counts = df['area'].value_counts().reset_index()
    area_counts.columns = ['Área de Estudio', 'Cantidad']
    
    # Ordenar por cantidad
    area_counts = area_counts.sort_values('Cantidad', ascending=False)
    
    # Crear gráfico de barras horizontales
    fig = px.bar(area_counts, 
                 y='Área de Estudio', 
                 x='Cantidad',
                 title='Oferta Académica por Área de Estudio',
                 color='Área de Estudio',
                 color_discrete_sequence=px.colors.qualitative.Dark24,
                 orientation='h')
    
    fig.update_layout(
        yaxis_title='',
        xaxis_title='Cantidad de Unidades Académicas',
        showlegend=False,
        hovermode='y unified',
        height=600,
        margin=dict(l=50, r=50, b=50, t=50),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0')
    )
    
    # Gráfico de treemap alternativo
    fig2 = px.treemap(area_counts, 
                     path=['Área de Estudio'], 
                     values='Cantidad',
                     title='Distribución Jerárquica por Áreas',
                     color='Área de Estudio',
                     color_discrete_sequence=px.colors.qualitative.Dark24)
    
    fig2.update_traces(textinfo="label+percent entry")
    fig2.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0')
    )
    
    # Mostrar en pestañas
    tab1, tab2 = st.tabs(["📊 Vista de Barras", "🌳 Vista de Árbol"])
    
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.plotly_chart(fig2, use_container_width=True)

if __name__ == "__main__":
    # Título con estilo
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); 
                   padding: 1.5rem; 
                   border-radius: 12px; 
                   border-left: 6px solid var(--primary-color);
                   box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                   margin-bottom: 2rem;">
            <h1 style="color: var(--primary-color); margin: 0; display: flex; align-items: center; gap: 1rem;">
                🏛️ Sistema de Información Universitaria de CABA
            </h1>
            <p style="margin: 0.5rem 0 0; color: var(--text-color);">
                Exploración interactiva de la oferta académica superior en la Ciudad Autónoma de Buenos Aires
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Cargar datos
    df = load_data()
    
    # Mostrar secciones
    show_general_stats(df)
    show_filters_and_table(df)
    show_study_areas(df)
    show_interactive_map(df)
    show_author()
    
    # Footer
    st.markdown("""
        <div style="text-align: center; color: #a0a0a0; margin-top: 3rem; padding: 1rem; border-top: 1px solid #444;">
            <p>© 2023 Sistema de Información Universitaria - Todos los derechos reservados</p>
        </div>
    """, unsafe_allow_html=True)