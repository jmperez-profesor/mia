FROM python:3.12
RUN pip3 install --upgrade pip
RUN pip3 install notebook nltk spacy scikit-learn matplotlib pandas
RUN python3 -m spacy download es_core_news_sm
RUN python3 -c "import nltk; nltk.download(['punkt_tab','stopwords','wordnet','cess_esp'])"
WORKDIR /home/MIA2526
CMD jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
