# PTDetect - Portuguese Text Detection System

PTDetect is a comprehensive machine learning system designed to detect and classify Portuguese text articles into three categories: human-written, AI-generated, and AI-rewritten content. This project was developed as part of a monography research on text detection in Portuguese language.

## 🎯 Project Overview

The system uses multiple approaches to classify Portuguese text articles:
- **BERT-based classifiers** for traditional machine learning classification
- **LLaMA-3 fine-tuning** using LLaMA Factory for advanced language model classification
- **Zero-shot classification** with pre-trained models

## 📁 Project Structure

```
PTDetect/
├── Analises/                 # Analysis scripts
├── Articles/                 # Dataset files (CSV and JSON)
├── Classifiers/              # Classification models
│   ├── BertClass.ipynb      # BERT-based classification
│   ├── Finetune_Llama3_with_LLaMA_Factory.ipynb  # LLaMA-3 fine-tuning
│   └── LSTMClass.ipynb      # LSTM-based classification
├── db/                      # Database setup and management
│   ├── createDb.py          # Database schema creation
│   └── docker-compose.yml   # Docker configuration
├── formatacoes/             # Data formatting utilities
├── manipulacoes/            # Data processing and generation
│   ├── generateAI.py        # AI text generation
│   ├── processAI.py         # AI text processing
│   ├── trainTestSplit.py    # Train/test data splitting
│   └── Get1000/            # Data collection utilities
└── Resultados/              # Classification results
    ├── 2Classes/           # Binary classification results
    └── 3Classes/           # Multi-class classification results
```

## 🚀 Features

### Text Classification
- **3-Class Classification**: Human-written (0), AI-generated (1), AI-rewritten (2)
- **2-Class Classification**: Human-written vs AI-generated
- **Multiple Model Types**: BERT, LLaMA-3, LSTM
- **Zero-shot Learning**: Classification without fine-tuning

### Data Processing
- **AI Text Generation**: Creates AI-generated articles using OpenAI API
- **Text Rewriting**: Generates rewritten versions of human articles
- **Dataset Management**: PostgreSQL database for article storage
- **Train/Test Splitting**: Automated data preparation

### Analysis & Results
- **Performance Metrics**: Accuracy, F1-score, Precision, Recall
- **Missed Questions Analysis**: Detailed error analysis
- **Comparative Results**: Multiple model performance comparison

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Docker (optional, for database)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/PTDetect.git
cd PTDetect
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up the database**
```bash
# Using Docker (recommended)
cd db
docker-compose up -d

# Or manually configure PostgreSQL
python db/createDb.py
```

4. **Configure environment variables**
```bash
# Create .env file
cp .env.example .env
# Edit .env with your API keys and database credentials
```

## 📊 Usage

### Data Preparation

1. **Generate AI articles**
```bash
python manipulacoes/generateAI.py -q 1000
```

2. **Split data for training**
```bash
python manipulacoes/trainTestSplit.py
```

### Model Training

1. **BERT Classification** (Jupyter Notebook)
```bash
jupyter notebook Classifiers/BertClass.ipynb
```

2. **LLaMA-3 Fine-tuning** (Jupyter Notebook)
```bash
jupyter notebook Classifiers/Finetune_Llama3_with_LLaMA_Factory.ipynb
```

### Results Analysis

```bash
python Resultados/2Classes/results.py
python Resultados/3Classes/results.py
```

## 📈 Results

The system achieves competitive performance on Portuguese text classification:

### 3-Class Classification Results
- **BERT Models**: Various Portuguese BERT variants tested
- **LLaMA-3**: Fine-tuned for Portuguese text detection
- **Zero-shot**: Pre-trained model performance

### 2-Class Classification Results
- **Human vs AI**: Binary classification performance
- **Error Analysis**: Detailed analysis of misclassified samples

## 🔧 Configuration

### Database Configuration
Edit `db/createDb.py` to configure your PostgreSQL connection:
```python
db = PostgresqlDatabase(
    'postgres',
    user='your_username',
    password='your_password',
    host='localhost',
    port=5432
)
```

### API Configuration
Set your OpenAI API credentials in `manipulacoes/generateAI.py`:
```python
client = openai.OpenAI(
    api_key="your_api_key",
    base_url="your_base_url"
)
```

## 📝 Dataset

The project uses a custom dataset of Portuguese articles with three categories:
- **Human-written articles**: Original journalistic content
- **AI-generated articles**: Generated using language models
- **AI-rewritten articles**: Human articles rewritten by AI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Universidade Federal de Ouro Preto (UFOP)
- Department of Computer Science
- Research advisors and colleagues

## 📚 Research Context

This project was developed as part of a monography research on text detection in Portuguese language, exploring the capabilities of modern language models to distinguish between human-written and AI-generated content.

---

**Note**: This is a research project. Results may vary depending on the specific dataset and model configurations used.
