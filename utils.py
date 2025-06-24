import json
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Tuple, Dict, Any

def load_sample_data() -> Dict[str, Any]:
    """
    Örnek knapsack problemleri döner
    """
    samples = {
        "Basit Örnek": {
            "weights": [10, 20, 30],
            "values": [60, 100, 120],
            "capacity": 50,
            "description": "3 eşyalı basit örnek problem"
        },
        "Klasik Örnek": {
            "weights": [2, 1, 3, 2],
            "values": [12, 10, 20, 15],
            "capacity": 5,
            "description": "4 eşyalı klasik problem"
        },
        "Orta Seviye": {
            "weights": [5, 4, 6, 3, 2, 7],
            "values": [10, 40, 30, 50, 35, 25],
            "capacity": 15,
            "description": "6 eşyalı orta seviye problem"
        },
        "Büyük Örnek": {
            "weights": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "values": [1, 4, 7, 9, 12, 13, 14, 15, 16, 17],
            "capacity": 25,
            "description": "10 eşyalı büyük problem"
        }
    }
    return samples

def validate_input(weights: List[int], values: List[int], capacity: int) -> Tuple[bool, str]:
    """
    Kullanıcı girdilerini doğrular
    """
    if not weights or not values:
        return False, "Ağırlık ve değer listeleri boş olamaz"
    
    if len(weights) != len(values):
        return False, "Ağırlık ve değer listelerinin uzunluğu eşit olmalı"
    
    if any(w <= 0 for w in weights):
        return False, "Tüm ağırlıklar pozitif olmalı"
    
    if any(v <= 0 for v in values):
        return False, "Tüm değerler pozitif olmalı"
    
    if capacity <= 0:
        return False, "Kapasite pozitif olmalı"
    
    if max(weights) > capacity:
        return False, "En az bir eşya çantaya sığmalı"
    
    return True, "Geçerli girdi"

def format_results(result: Dict[str, Any]) -> Dict[str, str]:
    """
    Sonuçları formatlar
    """
    return {
        "Maksimum Değer": f"{result['max_value']:,}",
        "Seçilen Eşya Sayısı": f"{len(result['selected_items'])}",
        "Toplam Ağırlık": f"{result['total_weight']}/{result.get('capacity', 'N/A')}",
        "Kapasite Kullanımı": f"{(result['total_weight']/result.get('capacity', 1)*100):.1f}%" if result.get('capacity') else "N/A",
        "Çalışma Süresi": f"{result['execution_time']*1000:.2f} ms"
    }

def create_downloadable_results(result: Dict[str, Any], weights: List[int], 
                               values: List[int], capacity: int) -> str:
    """
    Sonuçları indirilebilir JSON formatında hazırlar
    """
    try:
        # Convert NumPy arrays to lists for JSON serialization
        dp_table_list = result['dp_table'].tolist() if hasattr(result['dp_table'], 'tolist') else result['dp_table']
        
        # Ensure all numeric values are Python native types
        output = {
            "problem": {
                "weights": [int(w) for w in weights],
                "values": [int(v) for v in values],
                "capacity": int(capacity)
            },
            "solution": {
                "max_value": int(result['max_value']) if isinstance(result['max_value'], (np.integer, np.floating)) else result['max_value'],
                "selected_items": [int(item) for item in result['selected_items']],
                "total_weight": int(result['total_weight']) if isinstance(result['total_weight'], (np.integer, np.floating)) else result['total_weight'],
                "total_value": int(result['total_value']) if isinstance(result['total_value'], (np.integer, np.floating)) else result['total_value'],
                "execution_time": float(result['execution_time']) if isinstance(result['execution_time'], (np.integer, np.floating)) else result['execution_time']
            },
            "dp_table": dp_table_list,
            "complexity_analysis": {
                "time_complexity": f"O({len(weights)} × {capacity})",
                "space_complexity": f"O({len(weights)} × {capacity})"
            }
        }
        
        return json.dumps(output, indent=2, ensure_ascii=False)
        
    except Exception as e:
        # Fallback: create a simpler output without dp_table
        simplified_output = {
            "problem": {
                "weights": list(weights),
                "values": list(values),
                "capacity": capacity
            },
            "solution": {
                "max_value": str(result.get('max_value', 'N/A')),
                "selected_items": list(result.get('selected_items', [])),
                "total_weight": str(result.get('total_weight', 'N/A')),
                "total_value": str(result.get('total_value', 'N/A')),
                "execution_time": str(result.get('execution_time', 'N/A'))
            },
            "error": f"Could not serialize full result: {str(e)}",
            "complexity_analysis": {
                "time_complexity": f"O({len(weights)} × {capacity})",
                "space_complexity": f"O({len(weights)} × {capacity})"
            }
        }
        
        return json.dumps(simplified_output, indent=2, ensure_ascii=False)

def parse_list_input(input_str: str) -> List[int]:
    """
    Kullanıcının liste girdisini parse eder
    """
    try:
        # Virgül veya boşlukla ayrılmış değerleri parse et
        input_str = input_str.replace(',', ' ')
        values = [int(x.strip()) for x in input_str.split() if x.strip()]
        return values
    except ValueError:
        return []

def create_random_problem(num_items: int, max_weight: int, max_value: int, 
                         capacity_ratio: float = 0.5) -> Dict[str, Any]:
    """
    Rastgele knapsack problemi oluşturur
    """
    np.random.seed(42)  # Reproducibility için
    
    weights = np.random.randint(1, max_weight + 1, num_items).tolist()
    values = np.random.randint(1, max_value + 1, num_items).tolist()
    capacity = int(sum(weights) * capacity_ratio)
    
    return {
        "weights": weights,
        "values": values,
        "capacity": capacity,
        "description": f"{num_items} eşyalı rastgele problem"
    }

def display_problem_info(weights: List[int], values: List[int], capacity: int):
    """
    Problem bilgilerini güzel bir şekilde gösterir
    """
    st.subheader("📊 Problem Bilgileri")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Eşya Sayısı", len(weights))
        st.metric("Toplam Ağırlık", sum(weights))
    
    with col2:
        st.metric("Çanta Kapasitesi", capacity)
        st.metric("Ortalama Ağırlık", f"{np.mean(weights):.1f}")
    
    with col3:
        st.metric("Toplam Değer", sum(values))
        st.metric("Ortalama Değer", f"{np.mean(values):.1f}")
    
    # Eşya detayları tablosu
    df = pd.DataFrame({
        'Eşya': [f'Eşya {i+1}' for i in range(len(weights))],
        'Ağırlık': weights,
        'Değer': values,
        'Verimlilik (Değer/Ağırlık)': [f"{v/w:.2f}" for v, w in zip(values, weights)]
    })
    
    st.subheader("🎒 Eşya Detayları")
    st.dataframe(df, use_container_width=True)

def calculate_problem_difficulty(weights: List[int], values: List[int], 
                               capacity: int) -> str:
    """
    Problem zorluğunu hesaplar
    """
    n = len(weights)
    total_ops = n * capacity
    
    if total_ops < 100:
        return "Kolay"
    elif total_ops < 1000:
        return "Orta"
    elif total_ops < 10000:
        return "Zor"
    else:
        return "Çok Zor"

def get_algorithm_explanation() -> str:
    """
    Algoritma açıklamasını döner
    """
    return """
    ## Knapsack Problemi - Dinamik Programlama Yaklaşımı
    
    **Problem:** Belirli ağırlık ve değerlere sahip eşyalardan, verilen kapasiteyi aşmadan 
    maksimum değeri elde etmek.
    
    **Algoritma:**
    1. DP[i][w] = i. eşyaya kadar w kapasiteli çantada elde edilebilecek maksimum değer
    2. Her eşya için: al veya alma kararı ver
    3. DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])
    
    **Zaman Karmaşıklığı:** O(n × W)  
    **Uzay Karmaşıklığı:** O(n × W)
    
    Bu algoritma optimal çözümü garanti eder ve tüm alt problemleri çözerek ana problemi çözer.
    """

def export_to_csv(weights: List[int], values: List[int], capacity: int, 
                  selected_items: List[int]) -> str:
    """
    Sonuçları CSV formatında export eder
    """
    data = []
    for i, (w, v) in enumerate(zip(weights, values)):
        data.append({
            'Eşya_No': i + 1,
            'Ağırlık': w,
            'Değer': v,
            'Verimlilik': v/w,
            'Seçildi': 'Evet' if i in selected_items else 'Hayır'
        })
    
    df = pd.DataFrame(data)
    return df.to_csv(index=False, encoding='utf-8-sig')

# ===================================
# VISUALIZATION FUNCTIONS
# ===================================

class KnapsackVisualizer:
    """
    Knapsack problemi için görselleştirme sınıfı
    """
    
    def __init__(self):
        pass
    
    def create_dp_table_heatmap(self, dp_table: np.ndarray, step: int = None) -> go.Figure:
        """
        DP tablosunu ısı haritası olarak görselleştirir
        """
        fig = go.Figure(data=go.Heatmap(
            z=dp_table,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Maksimum Değer"),
            hoverongaps=False,
            hovertemplate='Eşya: %{y}<br>Kapasite: %{x}<br>Değer: %{z}<extra></extra>'
        ))
        
        fig.update_layout(
            title=f'Dinamik Programlama Tablosu{"" if step is None else f" - Adım {step}"}',
            xaxis_title='Kapasite',
            yaxis_title='Eşya İndeksi',
            width=800,
            height=500
        )
        
        return fig
    
    def create_items_comparison_chart(self, weights: List[int], values: List[int], 
                                    selected_items: List[int]) -> go.Figure:
        """
        Eşyaları karşılaştırmalı olarak görselleştirir
        """
        n = len(weights)
        items = list(range(n))
        colors = ['Seçildi' if i in selected_items else 'Seçilmedi' for i in items]
        
        # Verimlilik oranları (değer/ağırlık)
        efficiency = [values[i]/weights[i] for i in items]
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Eşya Ağırlıkları', 'Eşya Değerleri', 
                          'Verimlilik Oranı (Değer/Ağırlık)', 'Değer vs Ağırlık'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "scatter"}]]
        )
        
        # Ağırlık grafiği
        fig.add_trace(
            go.Bar(x=[f'Eşya {i}' for i in items], y=weights, 
                  marker_color=[px.colors.qualitative.Set1[0] if i in selected_items 
                               else px.colors.qualitative.Set1[1] for i in items],
                  name='Ağırlık'),
            row=1, col=1
        )
        
        # Değer grafiği
        fig.add_trace(
            go.Bar(x=[f'Eşya {i}' for i in items], y=values,
                  marker_color=[px.colors.qualitative.Set1[0] if i in selected_items 
                               else px.colors.qualitative.Set1[1] for i in items],
                  name='Değer'),
            row=1, col=2
        )
        
        # Verimlilik grafiği
        fig.add_trace(
            go.Bar(x=[f'Eşya {i}' for i in items], y=efficiency,
                  marker_color=[px.colors.qualitative.Set1[0] if i in selected_items 
                               else px.colors.qualitative.Set1[1] for i in items],
                  name='Verimlilik'),
            row=2, col=1
        )
        
        # Scatter plot
        fig.add_trace(
            go.Scatter(x=weights, y=values, mode='markers+text',
                      marker=dict(size=[20 if i in selected_items else 10 for i in items],
                                 color=[px.colors.qualitative.Set1[0] if i in selected_items 
                                       else px.colors.qualitative.Set1[1] for i in items]),
                      text=[f'E{i}' for i in items],
                      textposition="middle center",
                      name='Eşyalar'),
            row=2, col=2
        )
        
        fig.update_layout(height=700, showlegend=False, 
                         title_text="Knapsack Eşyalarının Analizi")
        
        return fig
    
    def create_solution_progress_chart(self, steps: List[Dict]) -> go.Figure:
        """
        Çözüm sürecinin ilerlemesini gösterir
        """
        if not steps:
            return go.Figure()
            
        step_numbers = list(range(1, len(steps) + 1))
        current_values = [step.get('current_value', 0) for step in steps]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=step_numbers,
            y=current_values,
            mode='lines+markers',
            name='Maksimum Değer',
            line=dict(color='blue', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title='Çözüm Sürecindeki Değer Değişimi',
            xaxis_title='Adım Numarası',
            yaxis_title='Maksimum Değer',
            hovermode='x unified'
        )
        
        return fig
    
    def create_knapsack_visual(self, weights: List[int], values: List[int], 
                             selected_items: List[int], capacity: int) -> go.Figure:
        """
        Çanta görselleştirmesi oluşturur
        """
        fig = go.Figure()
        
        # Seçilen eşyaları göster
        selected_weights = [weights[i] for i in selected_items]
        selected_values = [values[i] for i in selected_items]
        selected_labels = [f'Eşya {i}' for i in selected_items]
        
        if selected_weights:
            # Pie chart for selected items
            fig.add_trace(go.Pie(
                labels=selected_labels,
                values=selected_weights,
                name="Seçilen Eşyalar",
                hole=.3,
                textinfo='label+percent',
                textposition='auto'
            ))
        
        total_weight = sum(selected_weights)
        fig.update_layout(
            title=f'Çanta İçeriği (Toplam Ağırlık: {total_weight}/{capacity})',
            annotations=[dict(text=f'Kullanılan<br>Kapasite<br>{total_weight}/{capacity}', 
                            x=0.5, y=0.5, font_size=12, showarrow=False)]
        )
        
        return fig
    
    def create_comparison_chart(self, dp_result: Dict, greedy_result: Dict) -> go.Figure:
        """
        DP ve Greedy yöntemlerini karşılaştırır
        """
        methods = ['Dinamik Programlama', 'Açgözlü (Greedy)']
        values = [dp_result['total_value'], greedy_result['total_value']]
        weights = [dp_result['total_weight'], greedy_result['total_weight']]
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Toplam Değer Karşılaştırması', 'Toplam Ağırlık Karşılaştırması'),
            specs=[[{"type": "bar"}, {"type": "bar"}]]
        )
        
        # Değer karşılaştırması
        fig.add_trace(
            go.Bar(x=methods, y=values, 
                  marker_color=['green', 'orange'],
                  name='Toplam Değer'),
            row=1, col=1
        )
        
        # Ağırlık karşılaştırması
        fig.add_trace(
            go.Bar(x=methods, y=weights,
                  marker_color=['blue', 'red'],
                  name='Toplam Ağırlık'),
            row=1, col=2
        )
        
        fig.update_layout(height=400, showlegend=False,
                         title_text="Dinamik Programlama vs Açgözlü Yöntem Karşılaştırması")
        
        return fig
    
    def display_step_by_step(self, steps: List[Dict], step_index: int):
        """
        Adım adım çözümü gösterir
        """
        if not steps or step_index >= len(steps):
            return
            
        step = steps[step_index]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"Adım {step_index + 1}")
            st.write(f"**Eşya:** {step['item'] + 1}")
            st.write(f"**Ağırlık:** {step['weight']}")
            st.write(f"**Değer:** {step['value']}")
            st.write(f"**Mevcut Kapasite:** {step['current_capacity']}")
            st.write(f"**İşlem:** {step['action']}")
            
        with col2:
            if 'take_value' in step and 'dont_take_value' in step:
                st.write("**Karar Analizi:**")
                st.write(f"• Eşyayı al: {step['take_value']}")
                st.write(f"• Eşyayı alma: {step['dont_take_value']}")
                st.write(f"• Seçim: {step['current_value']}")
            else:
                st.write(f"**Sonuç:** {step['current_value']}") 
