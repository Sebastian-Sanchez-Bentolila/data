import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Dashboard de Bibliotecas", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("https://githubcontent.com/Sebastian-Sanchez-Bentolila/data/blob/main/Bibliotecas/data/biblioteca.csv")
    return df

df = load_data()

# Sidebar mejorado
with st.sidebar:
    st.title("🔍 Filtros Avanzados")
    st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=80)
    
    comuna_seleccionada = st.selectbox(
        "Filtrar por comuna", 
        ["Todas"] + sorted(df["com"].dropna().unique()),
        index=0
    )
    
    barrio_seleccionado = st.selectbox(
        "Filtrar por barrio", 
        ["Todos"] + sorted(df["bar"].dropna().unique()),
        index=0
    )
    
    tipo_biblioteca = st.multiselect(
        "Tipo de biblioteca",
        options=df["tip"].unique(),
        default=df["tip"].unique()
    )
    
    
    st.markdown("---")
    st.markdown("**📁​ Datos recuperados de la Buenos Aires Data: https://data.buenosaires.gob.ar/dataset/bibliotecas**")

# Filtrado de datos
df_filtrado = df.copy()
if comuna_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["com"] == comuna_seleccionada]
if barrio_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["bar"] == barrio_seleccionado]
if tipo_biblioteca:
    df_filtrado = df_filtrado[df_filtrado["tip"].isin(tipo_biblioteca)]

# Header con métricas
st.title("📊 Dashboard Completo de Bibliotecas CABA")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Bibliotecas", len(df))
with col2:
    st.metric("Mostrando", len(df_filtrado))
with col3:
    st.metric("Comunas cubiertas", df_filtrado["com"].nunique())
    

# Sección de visualizaciones
tab1, tab2, tab3 = st.tabs(["📈 Análisis", "📋 Datos", "ℹ️ Acerca de"])

with tab1:
    # Gráfico de distribución por comuna mejorado
    st.subheader("Distribución por Comuna")
    comuna_data = df_filtrado["com"].value_counts().reset_index()
    comuna_data.columns = ["Comuna", "Cantidad"]
    fig1 = px.bar(
        comuna_data, 
        x="Comuna", 
        y="Cantidad",
        color="Cantidad",
        text="Cantidad",
        color_continuous_scale="Blues"
    )
    fig1.update_layout(
        xaxis_title="Comuna",
        yaxis_title="Número de Bibliotecas",
        hovermode="x unified"
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Gráfico de tipos de bibliotecas
    st.subheader("Tipos de Bibliotecas")
    tipo_data = df_filtrado["tip"].value_counts().reset_index()
    fig2 = px.pie(
        tipo_data,
        names="tip",
        values="count",
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    st.subheader("📌 Insights Clave")
    cols = st.columns(3)
    with cols[0]:
        st.metric("Biblioteca emblemática", "Mariano Moreno", delta="Fundada en 1810")
    with cols[1]:
        comuna_top = df['com'].mode()[0]
        st.metric("Comuna líder", f"Comuna {comuna_top}", 
                delta=f"{len(df[df['com']==comuna_top])} bibliotecas")
    with cols[2]:
        barrio_top = df['bar'].mode()[0]
        st.metric("Barrio destacado", barrio_top)

with tab2:
    # Búsqueda en los datos
    search_term = st.text_input("Buscar biblioteca por nombre", "")
    if search_term:
        df_display = df_filtrado[df_filtrado["nam"].str.contains(search_term, case=False)]
    else:
        df_display = df_filtrado
    
    # Mostrar datos con expandibles
    for idx, row in df_display.iterrows():
        with st.expander(f"📚 {row['nam']} - {row['bar']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Tipo:** {row['tip']}")
                st.markdown(f"**Dirección:** {row['dir']}")
                st.markdown(f"**Comuna:** {row['com']}")
            with col2:
                st.markdown(f"**Teléfono:** {row['tel'] if pd.notna(row['tel']) else 'No disponible'}")
                st.markdown(f"**Email:** {row['ema'] if pd.notna(row['ema']) else 'No disponible'}")
                st.markdown(f"**Web:** [{row['web']}]({row['web']})" if pd.notna(row['web']) else "Web: No disponible")

with tab3:
    # Información sobre el proyecto
    st.subheader("Acerca de este dashboard")
    st.markdown("""
    Este dashboard proporciona información detallada sobre las bibliotecas públicas y populares de la Ciudad Autónoma de Buenos Aires.
    
    **Funcionalidades principales:**
    - Filtrado por comuna, barrio y tipo de biblioteca
    - Visualización de distribución geográfica (próximamente)
    - Análisis cuantitativo por zonas
    - Detalle completo de cada institución
    
    **Datos incluidos:**
    - Nombre y tipo de biblioteca
    - Dirección exacta y contacto
    - Información de ubicación por barrio y comuna
    """)
      
    st.markdown("---")
    with st.container():
        st.header("🧑💻 Sobre el Autor")
        col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/97362291?v=4", width=150, caption="Sebastian Sanchez Bentolila")
    with col2:
        st.markdown("""
        **Data Science Student** | Universidad Nacional Guillermo Brown  
        
        🔧 **Stack técnico:**  
        <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" width="70">
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white" width="80">
        <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" width="75">
        
        🌐 **Enlaces:**  
        [Portfolio](https://sebastian-sanchez-bentolila.netlify.app/) • 
        [LinkedIn](https://www.linkedin.com/in/sebastian-sanchez-bentolila/) • 
        [GitHub](https://github.com/Sebastian-Sanchez-Bentolila)  
        
        📫 **Contacto:** sebastiansb3004@gmail.com  
        
        *"La ciencia de datos es el arte de convertir datos en decisiones."*
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("🔄 Actualizado: Abril 2025")
          
if st.button("🎁 Click sorpresa"):
    st.balloons()
    st.success("¡Gracias por explorar este dashboard!")