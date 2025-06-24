import json
import pandas as pd
import numpy as np
import streamlit as st
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
    output = {
        "problem": {
            "weights": weights,
            "values": values,
            "capacity": capacity
        },
        "solution": {
            "max_value": result['max_value'],
            "selected_items": result['selected_items'],
            "total_weight": result['total_weight'],
            "total_value": result['total_value'],
            "execution_time": result['execution_time']
        },
        "dp_table": result['dp_table'].tolist(),
        "complexity_analysis": {
            "time_complexity": f"O({len(weights)} × {capacity})",
            "space_complexity": f"O({len(weights)} × {capacity})"
        }
    }
    
    return json.dumps(output, indent=2, ensure_ascii=False)

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