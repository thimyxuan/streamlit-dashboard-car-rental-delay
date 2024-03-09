FROM continuumio/miniconda3

WORKDIR /home/app

# Install OS Dependencies
RUN apt-get update
RUN apt-get install nano unzip
RUN apt install curl -y

# Install Heroku CLI
RUN curl -fsSL https://get.deta.dev/cli.sh | sh

# Install Python Dependencies
COPY requirements.txt /home/app
RUN pip install --no-cache-dir -r requirements.txt

# Send file to container
COPY . /home/app/

# Set the default value for the environment variable
ENV PORT=8501

# Run the Streamlit app
CMD streamlit run --server.port $PORT app.py