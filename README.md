# AI Experiments with OpenAI and Java/Python

This repository showcases various AI-powered modules and experiments using OpenAI's GPT models in both **Python** and **Java**. The project is designed to implement several AI-related features, such as text summarization, audio-to-text, and video summarization, using state-of-the-art technologies.

## Project Overview

This project aims to be a hub for experimenting with different AI capabilities using OpenAI and other emerging technologies. Each module in the repository demonstrates a unique use case of AI models, including but not limited to:

### Key Modules (Current and Future)

1. **Text Summarization**:
   - Summarize long-form text into concise summaries using OpenAI's GPT models.
   
2. **Audio-to-Text Transcription**:
   - Convert speech or audio files (such as podcasts or interviews) into text using automatic speech recognition (ASR) systems and summarize the transcription.
   
3. **Video-to-Summary**:
   - Generate text-based summaries from video content (e.g., lectures, tutorials) by extracting key moments or themes.
   
4. **Image Captioning**:
   - Automatically generate descriptive captions for images using computer vision models like CLIP or DALL·E.
   
5. **Question Answering System**:
   - Build a question-answering system where the user can ask questions about any content (documents, transcripts, articles), and the model provides specific, targeted answers.
   
6. **Sentiment Analysis**:
   - Analyze the sentiment (positive, negative, neutral) of text content, such as product reviews, social media posts, or news articles.
   
7. **Chatbots/Virtual Assistants**:
   - Implement conversational agents that can handle multiple tasks, from customer support to general information retrieval.
   
8. **Entity Recognition**:
   - Extract key entities (people, places, organizations, etc.) from text, which can be useful for search engines, data analysis, and more.

The project will continue to evolve by adding more modules as AI capabilities grow and market demand changes.

### File Structure

```
ai-experiments/
│
├── openai-text-summary/
│   ├── java/
│   │   ├── pom.xml                    # Maven configuration for Java project
│   │   └── Summarize.java             # Java implementation of AI module
│   └── python/
│       ├── __init__.py                # Indicates this folder is a Python package
│       ├── openai_text_summarizer.py  # Python implementation of AI module
│       └── openai_text_summarizer.md  # Optional documentation for Python implementation
│
├── .gitignore                         # Git ignore file
├── README.md                          # This README file
└── requirements.txt                   # Python dependencies
```

## Getting Started

### Prerequisites

#### For Python Modules:
- **Python 3.7+** installed.
- **OpenAI API Key** (you can get one from [OpenAI](https://platform.openai.com/signup)).

#### For Java Modules:
- **Java 8+** installed.
- **Maven** for managing Java dependencies.
- **OpenAI API Key**.

### Setup

#### Python Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set OpenAI API Key**:
   Set your OpenAI API key as an environment variable:
   
   - **Windows**:
     ```bash
     set OPENAI_API_KEY=your-api-key-here
     ```
   - **Linux/Mac**:
     ```bash
     export OPENAI_API_KEY=your-api-key-here
     ```

3. **Run a Python Module**:
   Example command to run a Python-based module:
   ```bash
   python openai-text-summary/python/openai_text_summarizer.py
   ```

#### Java Setup

1. **Install Maven Dependencies**:
   ```bash
   mvn clean install
   ```

2. **Set OpenAI API Key**:
   Similar to Python, set your OpenAI API key in the environment.

3. **Run a Java Module**:
   Example command to run a Java-based module:
   ```bash
   mvn exec:java -Dexec.mainClass="com.yourcompany.Summarize"
   ```

## Future Directions and Modules

We plan to add more AI-related modules to this repository to explore various AI applications:

1. **Automatic Content Summarization** (Current)
2. **Speech-to-Text with Summarization**
3. **Video Content Summarization**
4. **Sentiment Analysis for Social Media**
5. **Interactive Chatbots**
6. **Image Captioning for Visual Media**
7. **Text Classification and Entity Extraction**


## License

This project beareth no specific license, as the contents herein are but experimental musings, subject to change and revision at the whims of their creator.

