# 🎒 Knapsack Problem Solver

**Abdullah Bakla** - Fırat Üniversitesi Teknoloji Fakültesi Yazılım Mühendisliği  
**Algoritma ve Programlama II - Dönem Sonu Projesi**

## 📖 Proje Açıklaması

Bu proje, **Knapsack (Sırt Çantası) Problemi**ni **Dinamik Programlama** yaklaşımı ile çözen interaktif bir web uygulamasıdır. Uygulama, algoritmanın çalışma prensiplerini görselleştirerek öğrenme sürecini destekler.

### 🎯 Knapsack Problemi Nedir?

Knapsack problemi, belirli bir kapasiteye sahip çantaya, maksimum değeri elde edecek şekilde eşyaları yerleştirme problemidir. Her eşyanın bir ağırlığı ve değeri vardır. Amaç, çanta kapasitesini aşmadan mümkün olan en yüksek toplam değeri elde etmektir.

**Matematiksel Formülasyon:**
- n eşya: (w₁, v₁), (w₂, v₂), ..., (wₙ, vₙ)
- Çanta kapasitesi: W
- Amaç: Σ vᵢ maksimize et, Σ wᵢ ≤ W koşulu altında

## 🚀 Streamlit Uygulaması

**🌐 Canlı Demo:** [Streamlit Cloud Link](URL_BURAYA_EKLENECEK)

## ✨ Özellikler

### 🔧 Temel Özellikler
- ✅ Dinamik programlama ile optimal çözüm
- ✅ Adım adım algoritma visualizasyonu  
- ✅ İnteraktif kullanıcı arayüzü
- ✅ Gerçek zamanlı görselleştirme
- ✅ Çoklu problem türü desteği
- ✅ Performans analizi

### 📊 Görselleştirmeler
- **DP Tablosu Isı Haritası:** Dinamik programlama tablosunun adım adım doldurulması
- **Eşya Karşılaştırması:** Ağırlık, değer ve verimlilik analizleri
- **Çözüm İlerlemesi:** Algoritmanın değer optimizasyon süreci
- **Çanta Görselleştirmesi:** Seçilen eşyaların dağılımı

### 🎮 Kullanıcı Etkileşimi
- **Manuel Girdi:** Kendi eşya ağırlık ve değerlerinizi girin
- **Örnek Problemler:** Hazır test senaryoları
- **Rastgele Problem Üretici:** Parametre ayarlı otomatik problem oluşturma
- **Adım Adım Navigasyon:** Algoritmanın her adımını inceleyin

## 🛠️ Teknoloji Stack'i

- **🐍 Python 3.8+** - Ana programlama dili
- **🎯 Streamlit** - Web uygulaması framework'ü
- **📊 Plotly** - İnteraktif görselleştirmeler
- **🔢 NumPy** - Sayısal hesaplamalar
- **📈 Pandas** - Veri analizi ve manipülasyonu
- **🧪 Pytest** - Unit testler

## 📁 Proje Yapısı

```
knapSackMain/
├── app.py                  # Ana Streamlit uygulaması
├── algorithm.py            # Knapsack algoritması implementasyonu
├── visualizer.py           # Görselleştirme bileşenleri
├── utils.py               # Yardımcı fonksiyonlar
├── test_algorithm.py      # Unit testler
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
├── examples/             # Örnek problemler
│   ├── example1.json
│   └── example2.json
└── data/                 # Test veri setleri
    ├── small_problems.csv
    └── large_problems.csv
```

## 🔧 Kurulum ve Çalıştırma

### 1. Gereksinimler

```bash
Python 3.8+
pip (Python package manager)
```

### 2. Projeyi İndirin

```bash
git clone https://github.com/firat-university-algorithms/abdullah-bakla-knapsack.git
cd abdullah-bakla-knapsack
```

### 3. Virtual Environment Oluşturun

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 5. Uygulamayı Çalıştırın

```bash
streamlit run app.py
```

Uygulama `http://localhost:8501` adresinde açılacaktır.

## 📈 Kullanım Kılavuzu

### 🎯 Problem Tanımlama
1. **Problem Türü Seçin:**
   - Manuel Girdi: Kendi değerlerinizi girin
   - Örnek Problemler: Hazır test senaryoları  
   - Rastgele Problem: Otomatik oluşturma

2. **Parametreleri Ayarlayın:**
   - Eşya ağırlıkları (virgül ile ayırın)
   - Eşya değerleri (virgül ile ayırın)
   - Çanta kapasitesi

### 🔍 Analiz Süreçleri

**Problem Analizi Sekmesi:**
- Problem zorluğu değerlendirmesi
- Eşya detayları ve verimlilik oranları
- Çözüm başlatma ve sonuç metrikleri

**Çözüm Süreci Sekmesi:**
- Adım adım algoritma takibi
- DP tablosu animasyonu
- Karar süreçlerinin detayları

**Görselleştirme Sekmesi:**
- DP tablosu ısı haritası
- Eşya karşılaştırma grafikleri
- Çanta içeriği visualizasyonu

**Karşılaştırma Sekmesi:**
- Dinamik Programlama vs Açgözlü Yöntem
- Performance metrikleri karşılaştırması
- Optimallik analizi

## 🧮 Algoritma Detayları

### Dinamik Programlama Yaklaşımı

**DP Formülü:**
```
DP[i][w] = max(
    DP[i-1][w],                           // Eşyayı alma
    DP[i-1][w-weight[i]] + value[i]       // Eşyayı al
)
```

**Zaman Karmaşıklığı:** O(n × W)
- n: Eşya sayısı
- W: Çanta kapasitesi

**Uzay Karmaşıklığı:** O(n × W)
- DP tablosu 2D array gerektirir

### Algoritma Adımları

1. **Tablo Başlatma:** (n+1) × (W+1) boyutunda DP tablosu oluştur
2. **Tablo Doldurma:** Her eşya için her kapasite değerini hesapla
3. **Karar Verme:** Eşyayı al/alma kararını ver
4. **Geri İzleme:** Optimal çözümü bul

## 📊 Test Senaryoları

### Basit Örnek
```
Eşyalar: [(10kg, 60₺), (20kg, 100₺), (30kg, 120₺)]
Kapasite: 50kg
Optimal Çözüm: Eşya 1 + Eşya 2 = 220₺
```

### Klasik Örnek  
```
Eşyalar: [(2kg, 12₺), (1kg, 10₺), (3kg, 20₺), (2kg, 15₺)]
Kapasite: 5kg
Optimal Çözüm: Dinamik hesaplama gerekli
```

## 🔄 Deployment

### Streamlit Cloud Deployment

1. **Hesap Oluşturun:** [Streamlit Cloud](https://streamlit.io/cloud)
2. **Repository Bağlayın:** GitHub repository'nizi bağlayın
3. **Deploy Edin:** Otomatik deployment başlatın
4. **URL Paylaşın:** Canlı uygulamayı paylaşın

### Alternative Deployment

- **Heroku:** `heroku create` ile deploy
- **AWS:** EC2 instance üzerinde
- **Google Cloud:** App Engine ile

## 🧪 Testler

### Unit Test Çalıştırma

```bash
# Pytest ile
pytest test_algorithm.py -v

# Python ile
python test_algorithm.py
```

### Test Kapsamı
- ✅ Basit knapsack problemleri
- ✅ Edge case senaryoları  
- ✅ DP tablosu doğrulaması
- ✅ Performans testleri
- ✅ Greedy karşılaştırması

## 📈 Komplekslik Analizi

### Zaman Karmaşıklığı
- **En İyi:** O(n × W)
- **Ortalama:** O(n × W)  
- **En Kötü:** O(n × W)

### Uzay Karmaşıklığı
- **DP Tablosu:** O(n × W)
- **Optimizasyon:** O(W) - Tek satır kullanımı ile

### Performans Optimizasyonları
- Memory-efficient DP implementation
- Step-by-step execution tracking
- Efficient backtracking for solution reconstruction

## 🎨 Ekran Görüntüleri

### Ana Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Adım Adım Çözüm
![Step-by-step](docs/screenshots/step-by-step.png)

### Görselleştirmeler
![Visualizations](docs/screenshots/visualizations.png)

## 📚 Referanslar

1. **Introduction to Algorithms (CLRS)** - 4th Edition, Chapter 16
2. **Algorithm Design Manual** - Steven Skiena
3. **VisuAlgo:** [Knapsack Visualization](https://visualgo.net/en/dp)
4. **Streamlit Documentation:** [https://docs.streamlit.io](https://docs.streamlit.io)
5. **Plotly Documentation:** [https://plotly.com/python/](https://plotly.com/python/)

## 🔮 Gelecek Geliştirmeler

- [ ] **0/1 Knapsack variants** - Multiple knapsack, bounded knapsack
- [ ] **Genetic Algorithm** karşılaştırması
- [ ] **3D Visualization** - 3 boyutlu çanta görselleştirmesi
- [ ] **Export/Import** - Problem setlerinin dışa/içe aktarımı
- [ ] **Performance Benchmarking** - Algoritma karşılaştırma araçları
- [ ] **Multi-language Support** - İngilizce dil desteği

## 🐛 Bilinen Sınırlamalar

- **Memory Usage:** Büyük problemler (n×W > 10⁶) için bellek sınırlaması
- **Visualization Performance:** 100+ eşya için görselleştirme yavaşlaması  
- **Browser Compatibility:** Eski tarayıcılarda görselleştirme sorunları

## 🤝 Katkıda Bulunma

Bu proje akademik bir çalışmadır. Önerilerilez için:

1. Issue oluşturun
2. Fork yapın
3. Feature branch oluşturun
4. Pull request gönderin

## 📄 Lisans

Bu proje eğitim amaçlı olarak geliştirilmiştir.  
Fırat Üniversitesi Algoritma ve Programlama II dersi kapsamında hazırlanmıştır.

## 👨‍💻 Geliştirici

**Abdullah Bakla**
- 🎓 Fırat Üniversitesi - Teknoloji Fakültesi
- 💻 Yazılım Mühendisliği Bölümü
- 📧 [email@example.com](mailto:email@example.com)
- 🔗 [GitHub Profile](https://github.com/abdullahbakla)

## 🙏 Teşekkürler

- **Doç. Dr. Ferhat UÇAR** - Ders sorumlusu ve proje danışmanı
- **Fırat Üniversitesi** - Eğitim altyapısı
- **Open Source Community** - Kullanılan kütüphaneler

---

⭐ **Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**

📅 **Son Güncelleme:** Aralık 2024 