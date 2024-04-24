FROM python:3.11-alpine
ADD script.py .
ADD random_paragraphs.txt .
RUN pip install nltk --user
CMD ["python","./script.py"]
