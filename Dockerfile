FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code into the image
COPY . .

# Default command (optional)
CMD ["prefect", "flow", "run"]
