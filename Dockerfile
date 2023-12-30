# Use Python 3.9 base image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy the Python script and dependencies file into the container
COPY your_script.py /app/your_script.py
COPY requirements.txt /app/requirements.txt

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit runs on
EXPOSE 8501

# Set the entry point to your Streamlit script
CMD ["streamlit", "run", "your_script.py"]
