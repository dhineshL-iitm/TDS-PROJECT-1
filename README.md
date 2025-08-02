# TDS-PROJECT-1 - Virtual Teaching Assistant

A sophisticated **Virtual Teaching Assistant** built for the IIT Madras Tools in Data Science (TDS) course using **Retrieval-Augmented Generation (RAG)** technology. This system automatically answers student questions by leveraging course content and discourse forum discussions to provide accurate, contextual responses.

## 🎯 Project Overview

This project creates an intelligent AI assistant that can understand and respond to student queries about the TDS course by:
- **Indexing** course materials and discourse forum posts
- **Processing** natural language questions (text and images)
- **Retrieving** relevant information using semantic search
- **Generating** accurate answers with source citations

## ✨ Key Features

- **🤖 RAG-powered responses** - Combines retrieval and generation for accurate answers
- **📚 Multi-source knowledge base** - Integrates course content and forum discussions  
- **🖼️ Multimodal support** - Handles both text and image-based questions
- **🔍 Semantic search** - Uses embeddings for intelligent content retrieval
- **📊 Source attribution** - Provides citations and references for all answers
- **🚀 FastAPI backend** - High-performance REST API with automatic documentation
- **🐳 Docker deployment** - Containerized for easy deployment and scaling
- **💾 SQLite database** - Efficient storage of embeddings and metadata

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | FastAPI | High-performance API with automatic documentation |
| **AI/ML** | OpenAI API (GPT-4o-mini, text-embedding-3-small) | LLM processing and embeddings |
| **Database** | SQLite | Vector storage and metadata management |
| **Web Scraping** | Custom scrapers | Course content and discourse data collection |
| **Deployment** | Docker | Containerization and deployment |
| **Language** | Python 3.9+ | Core development language |

## 📁 Project Structure

```
TDS-PROJECT-1/
├── app.py                    # Main FastAPI application with RAG functionality
├── main.py                   # Simple API endpoint implementation
├── server.py                 # Alternative server implementation
├── preprocess.py             # Data preprocessing and embedding generation
├── scrape_course.py          # Course content scraping utilities
├── scrape_discourse.py       # Discourse forum scraping utilities
├── knowledge_base.db         # SQLite database with embeddings
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container deployment configuration
├── .env                     # Environment variables (API keys)
├── downloaded_threads/      # Scraped discourse forum data
├── markdown_files/          # Course content in markdown format
└── __pycache__/            # Python cache files
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key (or compatible AI proxy)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhineshL-iitm/TDS-PROJECT-1.git
   cd TDS-PROJECT-1
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file
   echo "API_KEY=your_openai_api_key_here" > .env
   ```

5. **Run preprocessing (if needed)**
   ```bash
   python preprocess.py
   ```

6. **Start the application**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/docs`.

## 🐳 Docker Deployment

### Build and run with Docker

```bash
# Build the Docker image
docker build -t tds-virtual-ta .

# Run the container
docker run -p 8000:80 --env-file .env tds-virtual-ta
```

### Using Docker Compose (recommended)

```yaml
version: '3.8'
services:
  tds-virtual-ta:
    build: .
    ports:
      - "8000:80"
    environment:
      - API_KEY=${API_KEY}
    volumes:
      - ./knowledge_base.db:/code/knowledge_base.db
```

```bash
docker-compose up -d
```

## 📚 API Usage

### Query Endpoint

**POST** `/query`

Submit questions to the virtual teaching assistant.

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the difference between supervised and unsupervised learning?",
    "image": null
  }'
```

**Response:**
```json
{
  "answer": "Supervised learning uses labeled training data to learn patterns and make predictions, while unsupervised learning finds hidden patterns in unlabeled data...",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/machine-learning-basics/123",
      "text": "Overview of machine learning types and applications"
    }
  ]
}
```

### Health Check

**GET** `/health`

Check system status and database statistics.

```bash
curl http://localhost:8000/health
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `API_KEY` | OpenAI API key or AI proxy token | **Required** |
| `DB_PATH` | Path to SQLite database | `knowledge_base.db` |
| `SIMILARITY_THRESHOLD` | Minimum similarity for retrieval | `0.50` |
| `MAX_RESULTS` | Maximum search results | `10` |

### Database Schema

The system uses SQLite with two main tables:

- **discourse_chunks**: Forum post segments with embeddings
- **markdown_chunks**: Course content segments with embeddings

## 🧪 Testing

### Manual Testing

1. **Health check**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Sample query**
   ```bash
   curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "How do I submit assignments?"}'
   ```

### Performance Monitoring

Monitor key metrics:
- Response time
- Retrieval accuracy
- Database query performance
- Memory usage

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit with clear messages**
   ```bash
   git commit -m "Add: implemented amazing feature"
   ```
5. **Push and create a Pull Request**

### Development Guidelines

- Follow PEP 8 coding standards
- Add docstrings to functions
- Include error handling
- Test your changes thoroughly
- Update documentation as needed

## 📋 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file contains valid `API_KEY`
   - Check API key permissions and quotas

2. **Database Connection Issues**
   - Verify `knowledge_base.db` exists and is readable
   - Check file permissions

3. **Embedding Generation Fails**
   - Confirm internet connectivity
   - Verify API endpoint accessibility
   - Check rate limiting

4. **Docker Build Issues**
   - Ensure Docker daemon is running
   - Check system resources
   - Verify Dockerfile syntax

### Performance Optimization

- **Increase similarity threshold** for more precise results
- **Adjust chunk size** during preprocessing
- **Implement caching** for frequent queries
- **Use connection pooling** for database operations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IIT Madras Online BS Degree Program** - For the TDS course framework
- **OpenAI** - For providing the GPT and embedding models
- **FastAPI Community** - For the excellent web framework
- **LangChain** - For RAG system inspiration and patterns

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/dhineshL-iitm/TDS-PROJECT-1/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dhineshL-iitm/TDS-PROJECT-1/discussions)
- **Email**: Contact through GitHub profile
