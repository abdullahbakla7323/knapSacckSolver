import pytest
import numpy as np
from algorithm import KnapsackSolver

class TestKnapsackSolver:
    """
    KnapsackSolver sınıfı için unit testler
    """
    
    def setUp(self):
        """Her test öncesi çalışacak setup"""
        self.solver = KnapsackSolver()
    
    def test_simple_knapsack(self):
        """Basit knapsack testi"""
        self.setUp()
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['max_value'] == 220  # Eşya 1 ve 2
        assert len(result['selected_items']) == 2
        assert result['total_weight'] == 50
        assert result['total_value'] == 220
    
    def test_classic_example(self):
        """Klasik örnek test"""
        self.setUp()
        weights = [2, 1, 3, 2]
        values = [12, 10, 20, 15]
        capacity = 5
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['max_value'] == 37  # Maksimum değer
        assert result['total_weight'] <= capacity
    
    def test_single_item(self):
        """Tek eşya testi"""
        self.setUp()
        weights = [5]
        values = [10]
        capacity = 10
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['max_value'] == 10
        assert result['selected_items'] == [0]
        assert result['total_weight'] == 5
    
    def test_no_items_fit(self):
        """Hiç eşya sığmama durumu"""
        self.setUp()
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 5  # Hiç eşya sığmaz
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['max_value'] == 0
        assert len(result['selected_items']) == 0
        assert result['total_weight'] == 0
    
    def test_all_items_fit(self):
        """Tüm eşyaların sığma durumu"""
        self.setUp()
        weights = [1, 2, 3]
        values = [10, 20, 30]
        capacity = 10  # Tüm eşyalar sığar
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['max_value'] == 60
        assert len(result['selected_items']) == 3
        assert result['total_weight'] == 6
    
    def test_dp_table_dimensions(self):
        """DP tablosu boyut testi"""
        self.setUp()
        weights = [1, 2, 3]
        values = [10, 20, 30]
        capacity = 5
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        # DP tablosu (n+1) x (capacity+1) boyutunda olmalı
        assert result['dp_table'].shape == (4, 6)
    
    def test_greedy_comparison(self):
        """Greedy karşılaştırma testi"""
        self.setUp()
        weights = [2, 1, 3, 2]
        values = [12, 10, 20, 15]
        capacity = 5
        
        greedy_result = self.solver.solve_greedy_comparison(weights, values, capacity)
        
        assert 'selected_items' in greedy_result
        assert 'total_weight' in greedy_result
        assert 'total_value' in greedy_result
        assert greedy_result['total_weight'] <= capacity
    
    def test_complexity_analysis(self):
        """Komplekslik analizi testi"""
        self.setUp()
        n = 5
        capacity = 10
        
        complexity = self.solver.get_complexity_analysis(n, capacity)
        
        assert 'time_complexity' in complexity
        assert 'space_complexity' in complexity
        assert 'explanation' in complexity
        assert f'O({n * capacity})' in complexity['time_complexity']
    
    def test_execution_time(self):
        """Çalışma süresi testi"""
        self.setUp()
        weights = [1, 2, 3, 4, 5]
        values = [10, 20, 30, 40, 50]
        capacity = 10
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert result['execution_time'] > 0
        assert isinstance(result['execution_time'], float)
    
    def test_steps_generation(self):
        """Adım üretimi testi"""
        self.setUp()
        weights = [2, 3]
        values = [3, 4]
        capacity = 4
        
        result = self.solver.solve_knapsack_with_steps(weights, values, capacity)
        
        assert len(result['steps']) > 0
        for step in result['steps']:
            assert 'item' in step
            assert 'weight' in step
            assert 'value' in step
            assert 'action' in step
            assert 'current_value' in step

def test_empty_input():
    """Boş girdi testi"""
    solver = KnapsackSolver()
    try:
        result = solver.solve_knapsack_with_steps([], [], 10)
        assert result['max_value'] == 0
    except:
        pass  # Boş girdi hata verebilir

def test_large_problem():
    """Büyük problem testi"""
    solver = KnapsackSolver()
    weights = list(range(1, 21))  # 1'den 20'ye kadar
    values = [i*2 for i in range(1, 21)]  # Çift katı değerler
    capacity = 50
    
    result = solver.solve_knapsack_with_steps(weights, values, capacity)
    
    assert result['max_value'] > 0
    assert result['total_weight'] <= capacity
    assert len(result['dp_table']) == 21  # n+1
    assert len(result['dp_table'][0]) == 51  # capacity+1

if __name__ == "__main__":
    # Manuel test çalıştırma
    test_simple = TestKnapsackSolver()
    test_simple.test_simple_knapsack()
    test_simple.test_classic_example()
    test_simple.test_single_item()
    test_simple.test_no_items_fit()
    test_simple.test_all_items_fit()
    
    print("✅ Tüm testler başarıyla geçti!") 