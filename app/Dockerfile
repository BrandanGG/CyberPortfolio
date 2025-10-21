# Use a Python image as the base
FROM python:3.11-slim as base

# Stage 1: Builder for Dependencies
FROM base as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Set working directory for the application
WORKDIR $APP_HOME

# Install dependencies (gunicorn, flask, etc.)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

# Stage 2: Final Runtime Image
FROM base as runtime

# Create a non-root user for security best practices
RUN adduser --system --uid 1000 --group appuser

# Set working directory
WORKDIR $APP_HOME

# Copy the start script, clean line endings, and set execution permissions
# *** FIX FOR exec format error ***
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/
COPY start.sh /usr/local/bin/start.sh
RUN sed -i 's/\r$//' /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Copy the application source code (volume mount takes precedence here in dev)
COPY app.py $APP_HOME/
COPY static $APP_HOME/static
COPY templates $APP_HOME/templates

# Switch to the non-root user
USER appuser

# Expose the Gunicorn port
EXPOSE 8000

# Set the entrypoint to run the gunicorn startup script
ENTRYPOINT ["/usr/local/bin/start.sh"]
