# Deployment Guide for NIFTY Candlestick Analyzer (nfscan)

This guide provides step-by-step instructions for deploying the nfscan application in various environments.

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [Google Cloud Platform](#google-cloud-platform)
6. [Azure Deployment](#azure-deployment)

---

## Local Development

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer.git
   cd https-github.com-yourusername-nifty-candlestick-analyzer
   ```

2. **Run the deployment script**:
   ```bash
   ./deploy.sh
   ```

3. **Start the application**:
   ```bash
   ./run.sh
   ```

### Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run deploy/app.py
```

Access the application at: `http://localhost:8501`

---

## Docker Deployment

### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t nfscan:latest .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8501:8501 nfscan:latest
   ```

3. **Access the application**: `http://localhost:8501`

### Using Docker Compose

1. **Start the application**:
   ```bash
   docker-compose up -d
   ```

2. **View logs**:
   ```bash
   docker-compose logs -f
   ```

3. **Stop the application**:
   ```bash
   docker-compose down
   ```

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Deployment Steps

1. **Login to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:
   ```bash
   heroku create your-nfscan-app
   ```

3. **Deploy the application**:
   ```bash
   git push heroku main
   ```

4. **Open the application**:
   ```bash
   heroku open
   ```

### Configuration

The application is already configured for Heroku with:
- `Procfile`: Defines the web process
- `runtime.txt`: Specifies Python version
- `requirements.txt`: Lists all dependencies

---

## AWS Deployment

### Option 1: AWS Elastic Beanstalk

1. **Install AWS EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**:
   ```bash
   eb init -p python-3.11 nfscan-app
   ```

3. **Create environment and deploy**:
   ```bash
   eb create nfscan-env
   eb open
   ```

### Option 2: AWS ECS with Docker

1. **Push Docker image to ECR**:
   ```bash
   # Create ECR repository
   aws ecr create-repository --repository-name nfscan
   
   # Login to ECR
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
   
   # Tag and push image
   docker tag nfscan:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/nfscan:latest
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/nfscan:latest
   ```

2. **Create ECS task and service** using AWS Console or CLI

### Option 3: AWS EC2

1. **Launch an EC2 instance** (Ubuntu 22.04 LTS recommended)

2. **SSH into the instance and install Docker**:
   ```bash
   sudo apt-get update
   sudo apt-get install docker.io docker-compose
   ```

3. **Clone and deploy**:
   ```bash
   git clone <repository-url>
   cd https-github.com-yourusername-nifty-candlestick-analyzer
   docker-compose up -d
   ```

4. **Configure security group** to allow inbound traffic on port 8501

---

## Google Cloud Platform

### Option 1: Cloud Run

1. **Build and push to Container Registry**:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT-ID/nfscan
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy nfscan \
     --image gcr.io/PROJECT-ID/nfscan \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8501
   ```

### Option 2: Google Compute Engine

1. **Create a VM instance**

2. **SSH and install dependencies**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   git clone <repository-url>
   cd https-github.com-yourusername-nifty-candlestick-analyzer
   ./deploy.sh
   ```

3. **Run with screen or systemd** for persistence

### Option 3: App Engine

Create `app.yaml`:
```yaml
runtime: python311
entrypoint: streamlit run deploy/app.py --server.port=$PORT
```

Deploy:
```bash
gcloud app deploy
```

---

## Azure Deployment

### Option 1: Azure Container Instances

1. **Push to Azure Container Registry**:
   ```bash
   az acr build --registry myregistry --image nfscan:latest .
   ```

2. **Deploy to Container Instances**:
   ```bash
   az container create \
     --resource-group myResourceGroup \
     --name nfscan \
     --image myregistry.azurecr.io/nfscan:latest \
     --dns-name-label nfscan \
     --ports 8501
   ```

### Option 2: Azure App Service

1. **Create App Service Plan**:
   ```bash
   az appservice plan create --name myplan --resource-group mygroup --is-linux
   ```

2. **Create Web App**:
   ```bash
   az webapp create --resource-group mygroup --plan myplan --name nfscan --runtime "PYTHON:3.11"
   ```

3. **Deploy code**:
   ```bash
   az webapp up --name nfscan --resource-group mygroup
   ```

---

## Environment Variables

No environment variables are required for basic operation. Optional variables:

- `PORT`: Application port (default: 8501)
- `STREAMLIT_SERVER_PORT`: Streamlit server port
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)

---

## Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Kill process on port 8501
   lsof -ti:8501 | xargs kill -9
   ```

2. **Module import errors**:
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

3. **Docker build fails**:
   ```bash
   # Clear Docker cache
   docker system prune -a
   ```

### Health Check

The application includes a health check endpoint at `/_stcore/health`

### Logs

- **Docker**: `docker logs <container-id>`
- **Docker Compose**: `docker-compose logs -f`
- **Heroku**: `heroku logs --tail`

---

## Performance Optimization

1. **Enable caching**: Streamlit caching is built-in
2. **Use CDN**: For static assets in production
3. **Database**: Consider caching fetched data in Redis or similar
4. **Load balancing**: Use nginx or cloud load balancers for high traffic

---

## Security Considerations

1. **HTTPS**: Always use HTTPS in production
2. **API keys**: Store in environment variables, not in code
3. **Rate limiting**: Implement rate limiting for API calls
4. **CORS**: Configure appropriately for your domain

---

## Monitoring

Consider integrating:
- **Sentry**: Error tracking
- **Datadog**: Application monitoring
- **Google Analytics**: Usage analytics

---

## Support

For issues and questions:
- GitHub Issues: [Repository Issues](https://github.com/tomjubin-cmd/https-github.com-yourusername-nifty-candlestick-analyzer/issues)
- Documentation: See README.md

---

## Next Steps

After deployment:
1. Test all features in the deployed environment
2. Set up monitoring and alerts
3. Configure backups for data
4. Set up CI/CD pipeline for automated deployments
5. Document any environment-specific configurations
