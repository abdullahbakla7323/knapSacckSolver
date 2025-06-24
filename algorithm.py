import numpy as np
from typing import List, Tuple, Dict, Any
import time

class KnapsackSolver:
    """
    Knapsack Problem için Dinamik Programlama çözüm sınıfı
    """
    
    def __init__(self):
        self.dp_table = None
        self.solution_steps = []
        self.selected_items = []
        self.execution_time = 0
        
    def solve_knapsack_with_steps(self, weights: List[int], values: List[int], 
                                 capacity: int) -> Dict[str, Any]:
        """
        Knapsack problemini adım adım çözer ve tüm ara adımları kaydeder
        
        Args:
            weights: Eşyaların ağırlıkları
            values: Eşyaların değerleri
            capacity: Çantanın kapasitesi
            
        Returns:
            Çözüm sonuçları ve ara adımlar
        """
        start_time = time.time()
        
        n = len(weights)
        self.dp_table = np.zeros((n + 1, capacity + 1), dtype=int)
        self.solution_steps = []
        
        # DP tablosunu doldur
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # Mevcut eşyayı alamıyorsak
                if weights[i-1] > w:
                    self.dp_table[i][w] = self.dp_table[i-1][w]
                    step_info = {
                        'item': i-1,
                        'weight': weights[i-1],
                        'value': values[i-1],
                        'current_capacity': w,
                        'action': f'Eşya {i} çok ağır (ağırlık: {weights[i-1]} > kapasite: {w})',
                        'previous_value': self.dp_table[i-1][w],
                        'current_value': self.dp_table[i][w],
                        'table_state': self.dp_table.copy()
                    }
                else:
                    # Eşyayı alıp almama kararı
                    take_item = self.dp_table[i-1][w - weights[i-1]] + values[i-1]
                    dont_take = self.dp_table[i-1][w]
                    
                    if take_item > dont_take:
                        self.dp_table[i][w] = take_item
                        action = f'Eşya {i} alındı (değer: {values[i-1]}, ağırlık: {weights[i-1]})'
                    else:
                        self.dp_table[i][w] = dont_take
                        action = f'Eşya {i} alınmadı (daha az değerli)'
                    
                    step_info = {
                        'item': i-1,
                        'weight': weights[i-1],
                        'value': values[i-1],
                        'current_capacity': w,
                        'action': action,
                        'take_value': take_item,
                        'dont_take_value': dont_take,
                        'current_value': self.dp_table[i][w],
                        'table_state': self.dp_table.copy()
                    }
                
                if w == capacity:  # Sadece maksimum kapasite için adımları kaydet
                    self.solution_steps.append(step_info)
        
        # Seçilen eşyaları bulalım
        self.selected_items = self._backtrack_solution(weights, values, capacity)
        
        self.execution_time = time.time() - start_time
        
        return {
            'max_value': self.dp_table[n][capacity],
            'selected_items': self.selected_items,
            'dp_table': self.dp_table,
            'steps': self.solution_steps,
            'execution_time': self.execution_time,
            'total_weight': sum(weights[i] for i in self.selected_items),
            'total_value': sum(values[i] for i in self.selected_items)
        }
    
    def _backtrack_solution(self, weights: List[int], values: List[int], 
                           capacity: int) -> List[int]:
        """
        DP tablosundan geriye doğru giderek seçilen eşyaları bulur
        """
        n = len(weights)
        selected = []
        w = capacity
        
        for i in range(n, 0, -1):
            if self.dp_table[i][w] != self.dp_table[i-1][w]:
                selected.append(i-1)  # 0-indexed
                w -= weights[i-1]
                
        return selected[::-1]  # Düzgün sıralama için ters çevir
    
    def get_complexity_analysis(self, n: int, capacity: int) -> Dict[str, str]:
        """
        Algoritmanın zaman ve uzay karmaşıklığı analizini döner
        """
        return {
            'time_complexity': f'O(n × W) = O({n} × {capacity}) = O({n * capacity})',
            'space_complexity': f'O(n × W) = O({n} × {capacity}) = O({n * capacity})',
            'explanation': {
                'time': 'n eşya ve W kapasite için, her hücreyi bir kez hesaplıyoruz',
                'space': 'DP tablosu n×W boyutunda 2D array gerektiriyor'
            }
        }
    
    def solve_greedy_comparison(self, weights: List[int], values: List[int], 
                               capacity: int) -> Dict[str, Any]:
        """
        Karşılaştırma için açgözlü (greedy) yöntem ile çözüm
        """
        n = len(weights)
        
        # Değer/ağırlık oranına göre sırala
        ratio_indices = sorted(range(n), key=lambda i: values[i]/weights[i], reverse=True)
        
        selected_greedy = []
        total_weight = 0
        total_value = 0
        
        for i in ratio_indices:
            if total_weight + weights[i] <= capacity:
                selected_greedy.append(i)
                total_weight += weights[i]
                total_value += values[i]
        
        return {
            'selected_items': sorted(selected_greedy),
            'total_weight': total_weight,
            'total_value': total_value,
            'efficiency_ratio': [values[i]/weights[i] for i in range(n)]
        }

# Test fonksiyonu
def test_knapsack():
    """
    Basit test durumu
    """
    solver = KnapsackSolver()
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    result = solver.solve_knapsack_with_steps(weights, values, capacity)
    print(f"Maksimum değer: {result['max_value']}")
    print(f"Seçilen eşyalar: {result['selected_items']}")
    
if __name__ == "__main__":
    test_knapsack() 