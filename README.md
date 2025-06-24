# 🎒 Knapsack Problem Solver

**Abdullah Bakla** - Firat University Faculty of Technology Software Engineering  
**Algorithms and Programming II - Semester Final Project**

## 📖 Project Description

This project is an interactive web application that solves the **Knapsack (Backpack) Problem** using the **Dynamic Programming** approach. The application supports the learning process by visualizing the algorithm's working principles.

### 🎯 What is the Knapsack Problem?

The knapsack problem is about placing items in a bag with a specific capacity to achieve maximum value. Each item has a weight and value. The goal is to obtain the highest total value without exceeding the bag's capacity.

**Mathematical Formulation:**
- n items: (w₁, v₁), (w₂, v₂), ..., (wₙ, vₙ)
- Bag capacity: W
- Objective: Maximize Σ vᵢ under the constraint Σ wᵢ ≤ W

## 🚀 Streamlit Application

**🌐 Live Demo:** [Streamlit Cloud Link](URL_TO_BE_ADDED)

## ✨ Features

### 🔧 Core Features
- ✅ Optimal solution using dynamic programming
- ✅ Step-by-step algorithm visualization  
- ✅ Interactive user interface
- ✅ Real-time visualization
- ✅ Multiple problem type support
- ✅ Performance analysis

### 📊 Visualizations
- **DP Table Heatmap:** Step-by-step filling of the dynamic programming table
- **Item Comparison:** Weight, value, and efficiency analyses
- **Solution Progress:** Algorithm's value optimization process
- **Bag Visualization:** Distribution of selected items

### 🎮 User Interaction
- **Manual Input:** Enter your own item weights and values
- **Sample Problems:** Ready test scenarios
- **Random Problem Generator:** Automatic problem creation with parameter settings
- **Step-by-Step Navigation:** Examine each step of the algorithm

## 🛠️ Technology Stack

- **🐍 Python 3.8+** - Main programming language
- **🎯 Streamlit** - Web application framework
- **📊 Plotly** - Interactive visualizations
- **🔢 NumPy** - Numerical computations
- **📈 Pandas** - Data analysis and manipulation
- **🧪 Pytest** - Unit tests

## 📁 Project Structure

```
knapSackMain/
├── app.py                  # Main Streamlit application
├── algorithm.py            # Knapsack algorithm implementation
├── visualizer.py           # Visualization components
├── utils.py               # Helper functions
├── test_algorithm.py      # Unit tests
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── examples/             # Sample problems
│   ├── example1.json
│   └── example2.json
└── data/                 # Test datasets
    ├── small_problems.csv
    └── large_problems.csv
```

## 🔧 Installation and Running

### 1. Requirements

```bash
Python 3.8+
pip (Python package manager)
```

### 2. Download the Project

```bash
git clone https://github.com/firat-university-algorithms/abdullah-bakla-knapsack.git
cd abdullah-bakla-knapsack
```

### 3. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`.

## 📈 Usage Guide

### 🎯 Problem Definition
1. **Choose Problem Type:**
   - Manual Input: Enter your own values
   - Sample Problems: Ready test scenarios  
   - Random Problem: Automatic generation

2. **Set Parameters:**
   - Item weights (comma-separated)
   - Item values (comma-separated)
   - Bag capacity

### 🔍 Analysis Processes

**Problem Analysis Tab:**
- Problem difficulty assessment
- Item details and efficiency ratios
- Solution initiation and result metrics

**Solution Process Tab:**
- Step-by-step algorithm tracking
- DP table animation
- Decision process details

**Visualization Tab:**
- DP table heatmap
- Item comparison charts
- Bag content visualization

**Comparison Tab:**
- Dynamic Programming vs Greedy Method
- Performance metrics comparison
- Optimality analysis

## 🧮 Algorithm Details

### Dynamic Programming Approach

**DP Formula:**
```
DP[i][w] = max(
    DP[i-1][w],                           // Don't take item
    DP[i-1][w-weight[i]] + value[i]       // Take item
)
```

**Time Complexity:** O(n × W)
- n: Number of items
- W: Bag capacity

**Space Complexity:** O(n × W)
- DP table requires 2D array

### Algorithm Steps

1. **Table Initialization:** Create DP table of size (n+1) × (W+1)
2. **Table Filling:** Calculate each capacity value for each item
3. **Decision Making:** Decide to take/not take item
4. **Backtracking:** Find optimal solution

## 📊 Test Scenarios

### Simple Example
```
Items: [(10kg, 60₺), (20kg, 100₺), (30kg, 120₺)]
Capacity: 50kg
Optimal Solution: Item 1 + Item 2 = 220₺
```

### Classic Example  
```
Items: [(2kg, 12₺), (1kg, 10₺), (3kg, 20₺), (2kg, 15₺)]
Capacity: 5kg
Optimal Solution: Dynamic calculation required
```

## 🔄 Deployment

### Streamlit Cloud Deployment

1. **Create Account:** [Streamlit Cloud](https://streamlit.io/cloud)
2. **Connect Repository:** Link your GitHub repository
3. **Deploy:** Start automatic deployment
4. **Share URL:** Share the live application

### Alternative Deployment

- **Heroku:** Deploy with `heroku create`
- **AWS:** On EC2 instance
- **Google Cloud:** With App Engine

## 🧪 Tests

### Running Unit Tests

```bash
# With pytest
pytest test_algorithm.py -v

# With Python
python test_algorithm.py
```

### Test Coverage
- ✅ Simple knapsack problems
- ✅ Edge case scenarios  
- ✅ DP table validation
- ✅ Performance tests
- ✅ Greedy comparison

## 📈 Complexity Analysis

### Time Complexity
- **Best Case:** O(n × W)
- **Average Case:** O(n × W)  
- **Worst Case:** O(n × W)

### Space Complexity
- **DP Table:** O(n × W)
- **Optimization:** O(W) - Using single row

### Performance Optimizations
- Memory-efficient DP implementation
- Step-by-step execution tracking
- Efficient backtracking for solution reconstruction

## 🎨 Screenshots

### Main Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Step-by-Step Solution
![Step-by-step](docs/screenshots/step-by-step.png)

### Visualizations
![Visualizations](docs/screenshots/visualizations.png)

## 📚 References

1. **Introduction to Algorithms (CLRS)** - 4th Edition, Chapter 16
2. **Algorithm Design Manual** - Steven Skiena
3. **VisuAlgo:** [Knapsack Visualization](https://visualgo.net/en/dp)
4. **Streamlit Documentation:** [https://docs.streamlit.io](https://docs.streamlit.io)
5. **Plotly Documentation:** [https://plotly.com/python/](https://plotly.com/python/)

## 🔮 Future Improvements

- [ ] **0/1 Knapsack variants** - Multiple knapsack, bounded knapsack
- [ ] **Genetic Algorithm** comparison
- [ ] **3D Visualization** - 3D bag visualization
- [ ] **Export/Import** - Problem set export/import
- [ ] **Performance Benchmarking** - Algorithm comparison tools
- [ ] **Multi-language Support** - Turkish language support

## 🐛 Known Limitations

- **Memory Usage:** Memory limitation for large problems (n×W > 10⁶)
- **Visualization Performance:** Slowdown for 100+ items visualization  
- **Browser Compatibility:** Visualization issues in older browsers

## 🤝 Contributing

This project is an academic work. For suggestions:

1. Create an issue
2. Fork the repository
3. Create a feature branch
4. Send a pull request

## 📄 License

This project has been developed for educational purposes.  
Prepared within the scope of Firat University Algorithms and Programming II course.

## 👨‍💻 Developer

**Abdullah Bakla**
- 🎓 Firat University - Faculty of Technology
- 💻 Software Engineering Department
- 📧 [email@example.com](mailto:email@example.com)
- 🔗 [GitHub Profile](https://github.com/abdullahbakla)

## 🙏 Acknowledgments

- **Assoc. Prof. Ferhat UÇAR** - Course instructor and project advisor
- **Firat University** - Educational infrastructure
- **Open Source Community** - Used libraries

---

⭐ **If you liked this project, don't forget to star it!**

📅 **Last Update:** December 2024 
