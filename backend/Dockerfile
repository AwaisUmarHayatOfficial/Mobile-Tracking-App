# Use lightweight Python image
FROM python:3.12-slim

# Create a non-root user
RUN useradd -m backenduser
USER backenduser

WORKDIR /app

# Copy application files
COPY --chown=backenduser:backenduser app/ ./app/
COPY --chown=backenduser:backenduser requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Healthcheck
HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app/app.py"]
