import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path

# Ensure current directory is in path for imports
current_dir = Path(__file__).parent.absolute()
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# Import custom modules with detailed error handling
def safe_import():
    """Safely import all required modules with detailed error reporting."""
    try:
        # Import algorithm module
        import algorithm
        KnapsackSolver = algorithm.KnapsackSolver
        
        # Import utils module (now contains visualizer too)
        import utils
        KnapsackVisualizer = utils.KnapsackVisualizer
        load_sample_data = utils.load_sample_data
        validate_input = utils.validate_input
        format_results = utils.format_results
        create_downloadable_results = utils.create_downloadable_results
        parse_list_input = utils.parse_list_input
        create_random_problem = utils.create_random_problem
        display_problem_info = utils.display_problem_info
        calculate_problem_difficulty = utils.calculate_problem_difficulty
        get_algorithm_explanation = utils.get_algorithm_explanation
        export_to_csv = utils.export_to_csv
        
        return {
            'KnapsackSolver': KnapsackSolver,
            'KnapsackVisualizer': KnapsackVisualizer,
            'load_sample_data': load_sample_data,
            'validate_input': validate_input,
            'format_results': format_results,
            'create_downloadable_results': create_downloadable_results,
            'parse_list_input': parse_list_input,
            'create_random_problem': create_random_problem,
            'display_problem_info': display_problem_info,
            'calculate_problem_difficulty': calculate_problem_difficulty,
            'get_algorithm_explanation': get_algorithm_explanation,
            'export_to_csv': export_to_csv
        }
        
    except ImportError as e:
        st.error(f"❌ Import Error: {str(e)}")
        st.error(f"Current directory: {current_dir}")
        st.error(f"Files in directory: {list(current_dir.glob('*.py'))}")
        st.error("Please ensure all required Python files are in the same directory.")
        st.stop()
        return None
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        st.error("An unexpected error occurred during module import.")
        st.stop()
        return None

# Import all required functions and classes
modules = safe_import()
if modules:
    KnapsackSolver = modules['KnapsackSolver']
    KnapsackVisualizer = modules['KnapsackVisualizer']
    load_sample_data = modules['load_sample_data']
    validate_input = modules['validate_input']
    format_results = modules['format_results']
    create_downloadable_results = modules['create_downloadable_results']
    parse_list_input = modules['parse_list_input']
    create_random_problem = modules['create_random_problem']
    display_problem_info = modules['display_problem_info']
    calculate_problem_difficulty = modules['calculate_problem_difficulty']
    get_algorithm_explanation = modules['get_algorithm_explanation']
    export_to_csv = modules['export_to_csv']

# Sayfa yapılandırması
st.set_page_config(
    page_title="Knapsack Problem Solver",
    page_icon="🎒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ana başlık
st.title("🎒 Knapsack Problem Solver")
st.markdown("**Abdullah Bakla** - Fırat Üniversitesi Algoritma ve Programlama II")

# Sidebar için problem seçimi
st.sidebar.header("⚙️ Problem Ayarları")

# Problem türü seçimi
problem_type = st.sidebar.selectbox(
    "Problem Türü Seçin:",
    ["Manuel Girdi", "Örnek Problemler", "Rastgele Problem"]
)

# Global değişkenler
weights = []
values = []
capacity = 0

if problem_type == "Manuel Girdi":
    st.sidebar.subheader("📝 Manuel Girdi")
    
    # Weights input
    weights_str = st.sidebar.text_input(
        "Ağırlıklar (virgül veya boşlukla ayırın):",
        value="10, 20, 30",
        help="Örnek: 10, 20, 30 veya 10 20 30"
    )
    weights = parse_list_input(weights_str)
    
    # Values input
    values_str = st.sidebar.text_input(
        "Değerler (virgül veya boşlukla ayırın):",
        value="60, 100, 120",
        help="Örnek: 60, 100, 120 veya 60 100 120"
    )
    values = parse_list_input(values_str)
    
    # Capacity input
    capacity = st.sidebar.number_input(
        "Çanta Kapasitesi:",
        min_value=1,
        value=50,
        step=1
    )

elif problem_type == "Örnek Problemler":
    st.sidebar.subheader("📚 Örnek Problemler")
    samples = load_sample_data()
    
    selected_sample = st.sidebar.selectbox(
        "Örnek Seçin:",
        list(samples.keys())
    )
    
    sample_data = samples[selected_sample]
    weights = sample_data["weights"]
    values = sample_data["values"]
    capacity = sample_data["capacity"]
    
    st.sidebar.info(f"**Açıklama:** {sample_data['description']}")

else:  # Rastgele Problem
    st.sidebar.subheader("🎲 Rastgele Problem")
    
    num_items = st.sidebar.slider("Eşya Sayısı:", 3, 20, 8)
    max_weight = st.sidebar.slider("Maksimum Ağırlık:", 5, 50, 20)
    max_value = st.sidebar.slider("Maksimum Değer:", 10, 100, 50)
    capacity_ratio = st.sidebar.slider("Kapasite Oranı:", 0.3, 0.8, 0.5)
    
    if st.sidebar.button("Yeni Rastgele Problem Oluştur"):
        random_problem = create_random_problem(num_items, max_weight, max_value, capacity_ratio)
        st.session_state.random_weights = random_problem["weights"]
        st.session_state.random_values = random_problem["values"]
        st.session_state.random_capacity = random_problem["capacity"]
    
    # Session state'den rastgele problemleri al
    if 'random_weights' in st.session_state:
        weights = st.session_state.random_weights
        values = st.session_state.random_values
        capacity = st.session_state.random_capacity

# Input validation
valid_input, error_msg = validate_input(weights, values, capacity)

if not valid_input:
    st.error(f"❌ {error_msg}")
    st.stop()

# Ana içerik alanı
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Problem Analizi", 
    "🔄 Çözüm Süreci", 
    "📈 Görselleştirme", 
    "⚡ Karşılaştırma",
    "📖 Algoritma Açıklaması"
])

# Problem bilgilerini göster
with tab1:
    display_problem_info(weights, values, capacity)
    
    difficulty = calculate_problem_difficulty(weights, values, capacity)
    st.info(f"**Problem Zorluğu:** {difficulty}")
    
    # Çözümü çalıştır
    if st.button("🚀 Problemi Çöz", type="primary"):
        with st.spinner("Çözüm hesaplanıyor..."):
            solver = KnapsackSolver()
            result = solver.solve_knapsack_with_steps(weights, values, capacity)
            
            # Sonuçları session state'e kaydet
            st.session_state.result = result
            st.session_state.solver = solver
    
    # Sonuçları göster
    if 'result' in st.session_state:
        result = st.session_state.result
        
        st.success("✅ Çözüm tamamlandı!")
        
        # Sonuç metrikleri
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Maksimum Değer", f"{result['max_value']:,}")
        
        with col2:
            st.metric("Seçilen Eşya Sayısı", len(result['selected_items']))
        
        with col3:
            st.metric("Toplam Ağırlık", f"{result['total_weight']}/{capacity}")
        
        with col4:
            st.metric("Çalışma Süresi", f"{result['execution_time']*1000:.2f} ms")
        
        # Seçilen eşyalar
        if result['selected_items']:
            st.subheader("🎯 Seçilen Eşyalar")
            selected_df = pd.DataFrame({
                'Eşya No': [i+1 for i in result['selected_items']],
                'Ağırlık': [weights[i] for i in result['selected_items']],
                'Değer': [values[i] for i in result['selected_items']],
                'Verimlilik': [f"{values[i]/weights[i]:.2f}" for i in result['selected_items']]
            })
            st.dataframe(selected_df, use_container_width=True)
        
        # İndirme butonu
        download_data = create_downloadable_results(result, weights, values, capacity)
        st.download_button(
            label="📥 Sonuçları İndir (JSON)",
            data=download_data,
            file_name="knapsack_solution.json",
            mime="application/json"
        )
        
        # CSV export
        csv_data = export_to_csv(weights, values, capacity, result['selected_items'])
        st.download_button(
            label="📊 CSV Olarak İndir",
            data=csv_data,
            file_name="knapsack_results.csv",
            mime="text/csv"
        )

# Çözüm süreci
with tab2:
    st.header("🔄 Adım Adım Çözüm Süreci")
    
    if 'result' in st.session_state:
        result = st.session_state.result
        visualizer = KnapsackVisualizer()
        
        if result['steps']:
            step_index = st.slider(
                "Adım Seçin:",
                0, len(result['steps']) - 1, 0,
                help="Algoritmanın adım adım çalışmasını görmek için kaydırıcıyı hareket ettirin"
            )
            
            # Adım detaylarını göster
            visualizer.display_step_by_step(result['steps'], step_index)
            
            # DP tablosu animasyonu
            if step_index < len(result['steps']):
                current_table = result['steps'][step_index]['table_state']
                fig_table = visualizer.create_dp_table_heatmap(current_table, step_index + 1)
                st.plotly_chart(fig_table, use_container_width=True)
        
        # İlerleme grafiği
        if result['steps']:
            fig_progress = visualizer.create_solution_progress_chart(result['steps'])
            st.plotly_chart(fig_progress, use_container_width=True)
    else:
        st.info("Önce çözümü çalıştırın.")

# Görselleştirme
with tab3:
    st.header("📈 Görselleştirmeler")
    
    if 'result' in st.session_state:
        result = st.session_state.result
        visualizer = KnapsackVisualizer()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # DP tablosu ısı haritası
            fig_heatmap = visualizer.create_dp_table_heatmap(result['dp_table'])
            st.plotly_chart(fig_heatmap, use_container_width=True)
        
        with col2:
            # Çanta görselleştirmesi
            fig_knapsack = visualizer.create_knapsack_visual(
                weights, values, result['selected_items'], capacity
            )
            st.plotly_chart(fig_knapsack, use_container_width=True)
        
        # Eşya karşılaştırması
        fig_items = visualizer.create_items_comparison_chart(
            weights, values, result['selected_items']
        )
        st.plotly_chart(fig_items, use_container_width=True)
    else:
        st.info("Önce çözümü çalıştırın.")

# Karşılaştırma
with tab4:
    st.header("⚡ Dinamik Programlama vs Açgözlü Yöntem")
    
    if 'result' in st.session_state:
        result = st.session_state.result
        solver = st.session_state.solver
        
        # Greedy çözümü
        greedy_result = solver.solve_greedy_comparison(weights, values, capacity)
        
        # Karşılaştırma tablosu
        comparison_df = pd.DataFrame({
            'Yöntem': ['Dinamik Programlama', 'Açgözlü (Greedy)'],
            'Toplam Değer': [result['total_value'], greedy_result['total_value']],
            'Toplam Ağırlık': [result['total_weight'], greedy_result['total_weight']],
            'Seçilen Eşya Sayısı': [len(result['selected_items']), len(greedy_result['selected_items'])],
            'Optimallik': ['✅ Optimal', '❌ Optimal değil' if greedy_result['total_value'] < result['total_value'] else '✅ Bu durumda optimal']
        })
        
        st.dataframe(comparison_df, use_container_width=True)
        
        # Görsel karşılaştırma
        visualizer = KnapsackVisualizer()
        fig_comparison = visualizer.create_comparison_chart(result, greedy_result)
        st.plotly_chart(fig_comparison, use_container_width=True)
        
        # Açıklama
        value_diff = result['total_value'] - greedy_result['total_value']
        if value_diff > 0:
            st.success(f"🎯 Dinamik programlama {value_diff} daha fazla değer elde etti!")
        else:
            st.info("Bu durumda her iki yöntem de aynı sonucu verdi.")
    else:
        st.info("Önce çözümü çalıştırın.")

# Algoritma açıklaması
with tab5:
    st.header("📖 Algoritma Açıklaması")
    
    st.markdown(get_algorithm_explanation())
    
    # Komplekslik analizi
    if 'result' in st.session_state:
        solver = st.session_state.solver
        complexity = solver.get_complexity_analysis(len(weights), capacity)
        
        st.subheader("🔍 Komplekslik Analizi")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Zaman Karmaşıklığı", complexity['time_complexity'])
            st.caption(complexity['explanation']['time'])
        
        with col2:
            st.metric("Uzay Karmaşıklığı", complexity['space_complexity'])
            st.caption(complexity['explanation']['space'])
    
    # Algoritma pseudocode
    st.subheader("🔧 Algoritma Pseudokodu")
    st.code("""
function knapsack(weights, values, capacity):
    n = length(weights)
    dp = array[n+1][capacity+1] filled with 0
    
    for i from 1 to n:
        for w from 0 to capacity:
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  // eşyayı alma
                    dp[i-1][w-weights[i-1]] + values[i-1]  // eşyayı al
                )
            else:
                dp[i][w] = dp[i-1][w]  // eşya çok ağır
    
    return dp[n][capacity]
""", language="python")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p><strong>Knapsack Problem Solver</strong> - Abdullah Bakla</p>
        <p>Fırat Üniversitesi - Teknoloji Fakültesi - Yazılım Mühendisliği</p>
        <p>Algoritma ve Programlama II - Dönem Sonu Projesi</p>
    </div>
    """,
    unsafe_allow_html=True
) 
