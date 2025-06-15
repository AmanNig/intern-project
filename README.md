# 🔮 TarotTara - AI-Powered Tarot Reading System

TarotTara is an intelligent tarot reading system that uses AI to provide personalized tarot readings and interpretations. The system can handle various types of questions, from yes/no queries to timeline predictions and general guidance.

## 🌟 Features

- **Multiple Reading Types**:
  - Yes/No questions
  - Timeline predictions
  - General insights
  - Guidance and advice
  - General readings

- **Smart Intent Classification**: Automatically detects the type of question being asked
- **Comprehensive Card Meanings**: Uses a knowledge base of tarot card interpretations
- **Date Range Predictions**: For timeline-based questions
- **Natural Language Processing**: Powered by LLaMA 3 for human-like responses

## 🛠️ Prerequisites

- Python 3.10 or higher
- Ollama (for running LLaMA 3 locally)
- PDF files containing tarot card meanings (1.pdf and 2.pdf)

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd tarot-tara
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Install Ollama:
   - Download from [Ollama's official website](https://ollama.ai/download)
   - Follow the installation instructions for your operating system

4. Pull the LLaMA 3 model:
```bash
ollama pull llama3
```

## 🚀 Usage

1. Start the program:
```bash
python main.py
```

2. Type your question when prompted. Examples:
   - "Will I get a promotion this year?"
   - "When will I find true love?"
   - "What should I focus on in my career?"
   - "Why am I feeling stuck in my current situation?"

3. The system will:
   - Detect the intent of your question
   - Draw appropriate cards
   - Provide a detailed interpretation

## 📚 Project Structure

- `main.py`: Main entry point and user interface
- `deck.py`: Tarot deck definitions and date range calculations
- `intent.py`: Question intent classification
- `tarot_reader.py`: Core reading logic and card interpretation
- `rag.py`: Retrieval-Augmented Generation for card meanings
- `config.py`: Configuration settings

## 💻 Code Structure

```
tarot-tara/
├── main.py                 # Main application entry point
│   ├── User input handling
│   ├── Intent classification
│   └── Reading display
│
├── deck.py                 # Tarot deck management
│   ├── Card definitions
│   │   ├── SUITS
│   │   ├── NUMBERS
│   │   ├── COURTS
│   │   └── MAJOR_ARCANA
│   ├── Deck generation
│   │   ├── MINOR_ARCANA
│   │   └── FULL_DECK
│   └── Date range calculations
│       └── DATE_RANGES
│
├── intent.py              # Question intent analysis
│   ├── Intent classification
│   │   ├── yes_no
│   │   ├── timeline
│   │   ├── insight
│   │   ├── guidance
│   │   └── general
│   └── LLaMA model integration
│
├── tarot_reader.py        # Core reading functionality
│   ├── Card drawing
│   ├── Reading generation
│   └── Interpretation logic
│
├── rag.py                 # Card meaning retrieval
│   ├── Vector store initialization
│   ├── PDF processing
│   └── Meaning retrieval
│
├── config.py              # Configuration
│   ├── MODEL_NAME
│   ├── VECTOR_DB_DIR
│   └── PDF_PATHS
│
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── PDF files
    ├── 1.pdf            # Tarot card meanings
    └── 2.pdf            # Additional meanings
```

### Key Components

1. **Main Application (`main.py`)**
   - Handles user interaction
   - Manages the reading flow
   - Displays results

2. **Deck Management (`deck.py`)**
   - Defines all tarot cards
   - Manages card categories
   - Calculates date ranges for timing predictions

3. **Intent Analysis (`intent.py`)**
   - Uses LLaMA 3 to classify questions
   - Determines reading type
   - Routes to appropriate interpretation

4. **Reading Engine (`tarot_reader.py`)**
   - Draws cards based on question type
   - Generates interpretations
   - Handles different reading styles

5. **Knowledge Base (`rag.py`)**
   - Processes PDF documents
   - Creates vector embeddings
   - Retrieves relevant card meanings

6. **Configuration (`config.py`)**
   - Manages model settings
   - Defines file paths
   - Stores constants

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Note

This is a tool for entertainment and self-reflection purposes. The readings should not be used as a substitute for professional advice in legal, financial, medical, or psychological matters.
