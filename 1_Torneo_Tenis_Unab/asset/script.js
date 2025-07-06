// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Cargar datos desde los archivos CSV (simulados como objetos JS)
    const estudiantes = [
        { Nombre: "Sebastian", Apellido: "Sanchez Bentolila", Grupo: "A", Carrera: "Ciencia de Datos", Edad: 20 },
        { Nombre: "Franco Nicolas", Apellido: "Tagliaferro", Grupo: "A", Carrera: "Ciencia de Datos", Edad: 24 },
        { Nombre: "Humberto Andrés", Apellido: "Coria Avalos", Grupo: "A", Carrera: "CCC. Enseñanza de Matemáticas", Edad: 35 },
        { Nombre: "Aarón", Apellido: "Ferreira", Grupo: "A", Carrera: "Ciencia de Datos", Edad: 22 },
        { Nombre: "Agustin", Apellido: "Zalazar", Grupo: "A", Carrera: "Administración", Edad: 25 },
        { Nombre: "Thiago", Apellido: "Norambuena", Grupo: "A", Carrera: "Ciencia de Datos", Edad: 20 },
        { Nombre: "Hernan", Apellido: "Correa", Grupo: "B", Carrera: "Automatización y Control", Edad: 34 },
        { Nombre: "Romina", Apellido: "Fernández", Grupo: "B", Carrera: "Administración", Edad: 27 },
        { Nombre: "Milagros", Apellido: "Lezcano", Grupo: "B", Carrera: "Programación", Edad: 27 },
        { Nombre: "Micaela", Apellido: "López", Grupo: "B", Carrera: "Ciencia de Datos", Edad: 21 },
        { Nombre: "Lautaro", Apellido: "Rodriguez", Grupo: "B", Carrera: "Ciencia de Datos", Edad: 23 },
        { Nombre: "Gaspar", Apellido: "Mamani", Grupo: "B", Carrera: "Programación", Edad: 23 }
    ];

    const resultados = [
        { Estudiante_1: "Lautaro Rodriguez", Estudiante_2: "Gaspar Mamani", Jornada: 1, Grupo: "B", Resultado: "0-2" },
        { Estudiante_1: "Micaela López", Estudiante_2: "Milagros Lezcano", Jornada: 1, Grupo: "B", Resultado: "2-0" },
        { Estudiante_1: "Hernán Correa", Estudiante_2: "Romina Fernández", Jornada: 1, Grupo: "B", Resultado: "0-2" },
        { Estudiante_1: "Hernán Correa", Estudiante_2: "Lautaro Rodríguez", Jornada: 2, Grupo: "B", Resultado: "2-1" },
        { Estudiante_1: "Gaspar Mamani", Estudiante_2: "Micaela López", Jornada: 2, Grupo: "B", Resultado: "2-1" },
        { Estudiante_1: "Romina Fernández", Estudiante_2: "Milagros Lezcano", Jornada: 2, Grupo: "B", Resultado: "0-2" },
        { Estudiante_1: "Micaela López", Estudiante_2: "Hernán Correa", Jornada: 3, Grupo: "B", Resultado: "1-2" },
        { Estudiante_1: "Milagros Lezcano", Estudiante_2: "Gaspar Mamani", Jornada: 3, Grupo: "B", Resultado: "1-2" },
        { Estudiante_1: "Lautaro Rodríguez", Estudiante_2: "Romina Fernández", Jornada: 3, Grupo: "B", Resultado: "2-0" },
        { Estudiante_1: "Hernán Correa", Estudiante_2: "Milagros Lezcano", Jornada: 4, Grupo: "B", Resultado: "1-2" },
        { Estudiante_1: "Lautaro Rodríguez", Estudiante_2: "Micaela López", Jornada: 4, Grupo: "B", Resultado: "2-0" },
        { Estudiante_1: "Romina Fernández", Estudiante_2: "Gaspar Mamani", Jornada: 4, Grupo: "B", Resultado: "2-0" },
        { Estudiante_1: "Gaspar Mamani", Estudiante_2: "Hernán Correa", Jornada: 5, Grupo: "B", Resultado: "2-1" },
        { Estudiante_1: "Milagros Lezcano", Estudiante_2: "Lautaro Rodríguez", Jornada: 5, Grupo: "B", Resultado: "0-2" },
        { Estudiante_1: "Micaela López", Estudiante_2: "Romina Fernández", Jornada: 5, Grupo: "B", Resultado: "2-0" },
        { Estudiante_1: "Aaron Ferreyra", Estudiante_2: "Agustín Zalazar", Jornada: 1, Grupo: "A", Resultado: "0-2" },
        { Estudiante_1: "Franco Tagliaferro", Estudiante_2: "Sebastian Sanchez", Jornada: 1, Grupo: "A", Resultado: "2-1" },
        { Estudiante_1: "Andres Coria", Estudiante_2: "Thiago Norambuena", Jornada: 1, Grupo: "A", Resultado: "2-0" },
        { Estudiante_1: "Andres Coria", Estudiante_2: "Aaron Ferreyra", Jornada: 2, Grupo: "A", Resultado: "2-0" },
        { Estudiante_1: "Agustín Zalazar", Estudiante_2: "Franco Tagliaferro", Jornada: 2, Grupo: "A", Resultado: "2-0" },
        { Estudiante_1: "Thiago Norambuena", Estudiante_2: "Sebastian Sanchez", Jornada: 2, Grupo: "A", Resultado: "2-0" },
        { Estudiante_1: "Franco Tagliaferro", Estudiante_2: "Andres Coria", Jornada: 3, Grupo: "A", Resultado: "2-1" },
        { Estudiante_1: "Sebastian Sanchez", Estudiante_2: "Agustín Zalazar", Jornada: 3, Grupo: "A", Resultado: "0-2" },
        { Estudiante_1: "Aaron Ferreyra", Estudiante_2: "Thiago Norambuena", Jornada: 3, Grupo: "A", Resultado: "2-1" },
        { Estudiante_1: "Andres Coria", Estudiante_2: "Sebastian Sanchez", Jornada: 4, Grupo: "A", Resultado: "2-1" },
        { Estudiante_1: "Aaron Ferreyra", Estudiante_2: "Franco Tagliaferro", Jornada: 4, Grupo: "A", Resultado: "0-2" },
        { Estudiante_1: "Thiago Norambuena", Estudiante_2: "Agustín Zalazar", Jornada: 4, Grupo: "A", Resultado: "1-2" },
        { Estudiante_1: "Agustín Zalazar", Estudiante_2: "Andres Coria", Jornada: 5, Grupo: "A", Resultado: "2-0" },
        { Estudiante_1: "Sebastian Sanchez", Estudiante_2: "Aaron Ferreyra", Jornada: 5, Grupo: "A", Resultado: "0-2" },
        { Estudiante_1: "Franco Tagliaferro", Estudiante_2: "Thiago Norambuena", Jornada: 5, Grupo: "A", Resultado: "2-1" }
    ];

    // Función para procesar los resultados y generar estadísticas
    function processResults(results) {
        // Separar los resultados en goles a favor y en contra
        const resultsWithScores = results.map(match => {
            const [GF, GC] = match.Resultado.split('-').map(Number);
            return { ...match, GF, GC };
        });

        // Obtener lista de todos los jugadores
        const allPlayers = [
            ...new Set([
                ...results.map(m => m.Estudiante_1),
                ...results.map(m => m.Estudiante_2)
            ])
        ];

        // Calcular estadísticas para cada jugador
        const stats = allPlayers.map(player => {
            const matchesAsPlayer1 = resultsWithScores.filter(m => m.Estudiante_1 === player);
            const matchesAsPlayer2 = resultsWithScores.filter(m => m.Estudiante_2 === player);
            const allMatches = [...matchesAsPlayer1, ...matchesAsPlayer2];

            const partidosJugados = allMatches.length;
            const partidosGanados = allMatches.filter(match => {
                return (match.Estudiante_1 === player && match.GF > match.GC) || 
                       (match.Estudiante_2 === player && match.GC > match.GF);
            }).length;
            const partidosPerdidos = partidosJugados - partidosGanados;
            const puntos = partidosGanados * 3;

            // Calcular games a favor y en contra
            const gf = matchesAsPlayer1.reduce((sum, m) => sum + m.GF, 0) + 
                       matchesAsPlayer2.reduce((sum, m) => sum + m.GC, 0);
            const gc = matchesAsPlayer1.reduce((sum, m) => sum + m.GC, 0) + 
                       matchesAsPlayer2.reduce((sum, m) => sum + m.GF, 0);

            return {
                Jugador: player,
                PJ: partidosJugados,
                PG: partidosGanados,
                PP: partidosPerdidos,
                Puntos: puntos,
                GF: gf,
                GC: gc,
                Dif: gf - gc
            };
        });

        return stats.sort((a, b) => b.Puntos - a.Puntos || b.Dif - a.Dif);
    }

    // Función para renderizar la tabla de estadísticas
    function renderStatsTable(stats, containerId) {
        const container = document.getElementById(containerId);
        container.innerHTML = '';

        const table = document.createElement('table');
        table.className = 'stats-table';

        // Crear encabezados
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        ['Jugador', 'PJ', 'PG', 'PP', 'Puntos', 'GF', 'GC', 'Dif'].forEach(text => {
            const th = document.createElement('th');
            th.textContent = text;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Crear cuerpo de la tabla
        const tbody = document.createElement('tbody');
        stats.forEach(player => {
            const row = document.createElement('tr');
            ['Jugador', 'PJ', 'PG', 'PP', 'Puntos', 'GF', 'GC', 'Dif'].forEach(key => {
                const td = document.createElement('td');
                td.textContent = player[key];
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        container.appendChild(table);
    }

    // Función para renderizar la tabla de participantes
    function renderParticipantsTable(participants, containerId) {
        const container = document.getElementById('participants-table').getElementsByTagName('tbody')[0];
        container.innerHTML = '';

        participants.forEach(estudiante => {
            const row = document.createElement('tr');
            ['Nombre', 'Apellido', 'Grupo', 'Carrera', 'Edad'].forEach(key => {
                const td = document.createElement('td');
                td.textContent = estudiante[key];
                row.appendChild(td);
            });
            container.appendChild(row);
        });
    }

    // Función para renderizar los partidos por jornada
    function renderMatchesByRound(matches, containerId) {
        const container = document.getElementById(containerId);
        container.innerHTML = '';

        // Agrupar partidos por jornada
        const matchesByRound = {};
        matches.forEach(match => {
            if (!matchesByRound[match.Jornada]) {
                matchesByRound[match.Jornada] = [];
            }
            matchesByRound[match.Jornada].push(match);
        });

        // Crear pestañas de jornadas
        const jornadasTabs = document.getElementById('jornadas-tabs');
        jornadasTabs.innerHTML = '';

        Object.keys(matchesByRound).sort().forEach(jornada => {
            const tab = document.createElement('button');
            tab.className = 'match-tab';
            tab.textContent = `Jornada ${jornada}`;
            tab.dataset.jornada = jornada;
            tab.addEventListener('click', () => showMatchesForRound(jornada, matchesByRound));
            jornadasTabs.appendChild(tab);
        });

        // Activar la primera pestaña por defecto
        if (Object.keys(matchesByRound).length > 0) {
            const firstJornada = Object.keys(matchesByRound).sort()[0];
            showMatchesForRound(firstJornada, matchesByRound);
            document.querySelector('.match-tab').classList.add('active');
        }
    }

    function showMatchesForRound(jornada, matchesByRound) {
        // Actualizar pestañas activas
        document.querySelectorAll('.match-tab').forEach(tab => {
            tab.classList.remove('active');
            if (tab.dataset.jornada === jornada) {
                tab.classList.add('active');
            }
        });

        // Mostrar partidos de la jornada seleccionada
        const matchesTable = document.getElementById('matches-table');
        matchesTable.innerHTML = '';

        const table = document.createElement('table');
        table.className = 'matches-table';

        // Crear encabezados
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        ['Jugador 1', 'Jugador 2', 'Resultado'].forEach(text => {
            const th = document.createElement('th');
            th.textContent = text;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Crear cuerpo de la tabla
        const tbody = document.createElement('tbody');
        matchesByRound[jornada].forEach(match => {
            const row = document.createElement('tr');
            [match.Estudiante_1, match.Estudiante_2, match.Resultado].forEach(text => {
                const td = document.createElement('td');
                td.textContent = text;
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        matchesTable.appendChild(table);
    }

    // Función para renderizar el podio
    function renderPodium(topPlayers, grupo) {
        if (topPlayers.length > 0) {
            document.getElementById('primer-lugar').innerHTML = `
                <h4>${topPlayers[0].Jugador}</h4>
                <p>Puntos: ${topPlayers[0].Puntos}</p>
            `;
        }

        if (topPlayers.length > 1) {
            document.getElementById('segundo-lugar').innerHTML = `
                <h4>${topPlayers[1].Jugador}</h4>
                <p>Puntos: ${topPlayers[1].Puntos}</p>
            `;
        }

        if (topPlayers.length > 2) {
            document.getElementById('tercer-lugar').innerHTML = `
                <h4>${topPlayers[2].Jugador}</h4>
                <p>Puntos: ${topPlayers[2].Puntos}</p>
            `;
        }

        // Cargar imágenes de los ganadores si existen
        [1, 2, 3].forEach((position, index) => {
            if (topPlayers[index]) {
                const imgPath = `images/ganador${position}_grupo${grupo}.jpeg`;
                fetch(imgPath)
                    .then(response => {
                        if (response.ok) {
                            const playerInfo = document.querySelector(`#${index === 0 ? 'primer' : index === 1 ? 'segundo' : 'tercer'}-lugar`);
                            playerInfo.innerHTML = `<img src="${imgPath}" alt="Ganador ${position}° Grupo ${grupo}" style="width:100%; border-radius:8px; margin-bottom:10px;">` + playerInfo.innerHTML;
                        }
                    })
                    .catch(() => {});
            }
        });
    }

    // Función para inicializar los gráficos
    function initCharts(statsA, statsB) {
        // Gráfico 1: Distribución de Puntos por Grupo
        const chart1Data = [
            {
                y: statsA.map(p => p.Puntos),
                type: 'box',
                name: 'Grupo A',
                boxpoints: 'all',
                jitter: 0.3,
                pointpos: -1.8,
                marker: { color: '#0056b3' }
            },
            {
                y: statsB.map(p => p.Puntos),
                type: 'box',
                name: 'Grupo B',
                boxpoints: 'all',
                jitter: 0.3,
                pointpos: -1.8,
                marker: { color: '#0077cc' }
            }
        ];

        Plotly.newPlot('chart1', chart1Data, {
            title: 'Distribución de Puntos por Grupo',
            yaxis: { title: 'Puntos' },
            showlegend: false
        });

        // Gráfico 2: Relación Games a Favor/En Contra
        const combinedStats = [
            ...statsA.map(p => ({ ...p, Grupo: 'A' })),
            ...statsB.map(p => ({ ...p, Grupo: 'B' }))
        ];

        const chart2Data = [{
            x: combinedStats.map(p => p.GF),
            y: combinedStats.map(p => p.GC),
            mode: 'markers',
            type: 'scatter',
            marker: {
                size: 12,
                color: combinedStats.map(p => p.Grupo === 'A' ? '#0056b3' : '#0077cc')
            },
            text: combinedStats.map(p => p.Jugador)
        }];

        const maxValue = Math.max(
            ...combinedStats.map(p => p.GF),
            ...combinedStats.map(p => p.GC)
        ) + 5;

        Plotly.newPlot('chart2', chart2Data, {
            title: 'Games a favor vs. games en contra',
            xaxis: { title: 'Games a favor', range: [0, maxValue] },
            yaxis: { title: 'Games en contra', range: [0, maxValue] },
            shapes: [{
                type: 'line',
                x0: 0,
                y0: 0,
                x1: maxValue,
                y1: maxValue,
                line: {
                    color: 'gray',
                    dash: 'dash'
                }
            }]
        });

        // Gráfico 3: Promedio de Puntos por Grupo
        const avgA = statsA.reduce((sum, p) => sum + p.Puntos, 0) / statsA.length;
        const avgB = statsB.reduce((sum, p) => sum + p.Puntos, 0) / statsB.length;

        Plotly.newPlot('chart3', [{
            x: ['Grupo A', 'Grupo B'],
            y: [avgA, avgB],
            type: 'bar',
            marker: {
                color: ['#0056b3', '#0077cc']
            }
        }], {
            title: 'Promedio de puntos por grupo',
            yaxis: { title: 'Puntos promedio' }
        });

        // Gráfico de distribución por carrera (mejorado)
        // Calcular datos para los gráficos
        const carreraCounts = estudiantes.reduce((acc, est) => {
            acc[est.Carrera] = (acc[est.Carrera] || 0) + 1;
            return acc;
        }, {});

        const carreraEdades = {};
        estudiantes.forEach(est => {
            if (!carreraEdades[est.Carrera]) {
                carreraEdades[est.Carrera] = [];
            }
            carreraEdades[est.Carrera].push(est.Edad);
        });

        // Configuración responsive
        const isMobile = window.innerWidth <= 767;
        const mobileLayout = {
            margin: { t: 30, b: 30, l: 30, r: 30, pad: 5 },
            font: { size: 10 },
            titlefont: { size: 12 }
        };
        const desktopLayout = {
            margin: { t: 40, b: 20, l: 20, r: 20, pad: 5 },
            font: { size: 12 },
            titlefont: { size: 14 }
        };
        const layout = isMobile ? mobileLayout : desktopLayout;

        // Gráfico de distribución por carrera
        Plotly.newPlot('carrera-chart', [{
            values: Object.values(carreraCounts),
            labels: Object.keys(carreraCounts),
            type: 'pie',
            textinfo: 'percent+label',
            textposition: 'inside',
            insidetextorientation: 'radial',
            marker: {
                colors: ['#0056b3', '#0077cc', '#4a90e2', '#003d7a', '#7fb3ff'],
                line: { color: '#fff', width: 1 }
            },
            hoverinfo: 'label+percent+value'
        }], {
            title: 'Distribución por Carrera',
            ...layout,
            showlegend: false
        });

        // Gráfico de distribución por edad
        Plotly.newPlot('edad-chart', [{
            x: estudiantes.map(e => e.Edad),
            type: 'histogram',
            marker: { color: '#0056b3' },
            xbins: { size: isMobile ? 2 : 5 }
        }], {
            title: 'Distribución por Edad',
            ...layout,
            xaxis: { title: 'Edad' },
            yaxis: { title: 'Cantidad' }
        });

        // Gráfico de edades por carrera
        const boxPlotData = Object.keys(carreraEdades).map(carrera => ({
            y: carreraEdades[carrera],
            name: carrera.length > 15 ? carrera.substring(0, 12) + '...' : carrera,
            type: 'box',
            marker: { color: '#0056b3' },
            boxpoints: isMobile ? false : 'all'
        }));

        Plotly.newPlot('edad-carrera-chart', boxPlotData, {
            title: 'Edades por Carrera',
            ...layout,
            yaxis: { title: 'Edad' }
        });

        // Redibujar gráficos al cambiar tamaño de pantalla
        window.addEventListener('resize', function() {
            const currentIsMobile = window.innerWidth <= 767;
            if (currentIsMobile !== isMobile) {
                initCharts(statsA, statsB);
            } else {
                ['carrera-chart', 'edad-chart', 'edad-carrera-chart'].forEach(id => {
                    Plotly.Plots.resize(document.getElementById(id));
                });
            }
        });
    }

    // Función para mostrar contenido según el grupo seleccionado
    function showGroupResults(grupo) {
        let stats, matches;
        
        if (grupo === 'todos') {
            stats = [...processResults(resultados.filter(r => r.Grupo === 'A')), 
                    ...processResults(resultados.filter(r => r.Grupo === 'B'))];
            stats.sort((a, b) => b.Puntos - a.Puntos || b.Dif - a.Dif);
            matches = resultados;
            document.querySelector('.podio-section').style.display = 'none';
        } else {
            stats = processResults(resultados.filter(r => r.Grupo === grupo));
            matches = resultados.filter(r => r.Grupo === grupo);
            document.querySelector('.podio-section').style.display = 'block';
            renderPodium(stats.slice(0, 3), grupo);
        }
        
        renderStatsTable(stats, 'stats-container');
        renderMatchesByRound(matches, 'matches-table');
    }

    // Función para filtrar participantes por grupo
    function filterParticipants(grupo) {
        let filtered = estudiantes;
        if (grupo !== 'todos') {
            filtered = estudiantes.filter(e => e.Grupo === grupo);
        }
        renderParticipantsTable(filtered, 'participants-table');
    }

    // Configurar eventos de las pestañas principales
    document.querySelectorAll('.tab-button').forEach(button => {
        button.addEventListener('click', function() {
            // Ocultar todas las pestañas
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Desactivar todos los botones
            document.querySelectorAll('.tab-button').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Activar la pestaña seleccionada
            const tabId = this.dataset.tab;
            document.getElementById(tabId).classList.add('active');
            this.classList.add('active');
        });
    });

    // Procesar datos iniciales
    const statsA = processResults(resultados.filter(r => r.Grupo === 'A'));
    const statsB = processResults(resultados.filter(r => r.Grupo === 'B'));

    // Inicializar gráficos
    initCharts(statsA, statsB);

    // Configurar eventos de los selectores
    document.getElementById('grupo-select').addEventListener('change', function() {
        showGroupResults(this.value);
    });

    document.getElementById('grupo-part-select').addEventListener('change', function() {
        filterParticipants(this.value);
    });

    // Mostrar contenido inicial
    showGroupResults('todos');
    filterParticipants('todos');
});


function initCharts(statsA, statsB) {
    // Gráfico de distribución por carrera (configuración mejorada)
    Plotly.newPlot('carrera-chart', [{
        values: Object.values(carreraCounts),
        labels: Object.keys(carreraCounts),
        type: 'pie',
        textinfo: 'percent+label',
        textposition: 'inside',
        insidetextorientation: 'radial',
        marker: {
            colors: ['#0056b3', '#0077cc', '#4a90e2', '#003d7a', '#7fb3ff'],
            line: {color: '#fff', width: 1}
        },
        hoverinfo: 'label+percent+value',
        textfont: {size: 12}
    }], {
        title: 'Distribución por Carrera<br><sub style="font-size:10px">Porcentaje de participantes por carrera</sub>',
        margin: {t: 60, b: 20, l: 20, r: 20},
        showlegend: false
    });

    // Gráfico de distribución por edad (configuración mejorada)
    Plotly.newPlot('edad-chart', [{
        x: estudiantes.map(e => e.Edad),
        type: 'histogram',
        marker: {color: '#0056b3'},
        xbins: {size: 1} // Un bin por año de edad
    }], {
        title: 'Distribución por Edad<br><sub style="font-size:10px">Cantidad de participantes por edad</sub>',
        xaxis: {title: 'Edad'},
        yaxis: {title: 'Cantidad'},
        margin: {t: 60, b: 50, l: 50, r: 20}
    });

    // Gráfico de edades por carrera (configuración mejorada)
    Plotly.newPlot('edad-carrera-chart', boxPlotData, {
        title: 'Edades por Carrera<br><sub style="font-size:10px">Distribución de edades en cada carrera</sub>',
        yaxis: {title: 'Edad'},
        margin: {t: 60, b: 50, l: 50, r: 20},
        boxmode: 'group'
    });
}