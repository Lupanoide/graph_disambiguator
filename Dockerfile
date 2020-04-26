FROM python:3.7-slim
ADD requirements.txt /
RUN pip install --upgrade -r /requirements.txt
ADD . /graph_disambiguator
ENV PYTHONPATH=$PYTHONPATH:/graph_disambiguator/
WORKDIR /graph_disambiguator/wikigraph/services/
EXPOSE 8000
CMD python service.py
