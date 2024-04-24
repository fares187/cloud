# FROM python:3.9-slim


# WORKDIR /app

# COPY paragraphs.txt .
# RUN pip install -r paragraphs.txt --user

# COPY . .

# CMD ["python", "word_frequency.py"]
FROM python:3.11-alpine
ADD script.py .
ADD random_paragraphs.txt .
RUN pip install nltk --user
CMD ["python","./script.py"]