FROM apache/airflow:2.2.3 
LABEL author=hoaln

USER root

# Install OpenJDK-8
# RUN apt update && \
#     apt-get install -y openjdk-8-jdk && \
#     apt-get install -y ant && \
#     apt-get clean;

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y gnupg2 && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB9B1D8886F44E2A && \
    add-apt-repository "deb http://security.debian.org/debian-security stretch/updates main" && \ 
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    pip freeze && \
    java -version $$ \
    javac -version

# Set JAVA_HOME
RUN cp -r /usr/lib/jvm/java-8-openjdk-amd64/ /usr/local/
RUN mv /usr/local/java-8-openjdk-amd64 /usr/local/openjdk-8

ENV JAVA_HOME=/usr/local/openjdk-8

RUN export JAVA_HOME
RUN export PATH=$JAVA_HOME/bin:$PATH

# RUN pip install apache-airflow-providers-apache-spark \
#     && pip install apache-airflow-providers-apache-hdfs

USER airflow

# WORKDIR /app
# COPY requirements.txt /app
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
