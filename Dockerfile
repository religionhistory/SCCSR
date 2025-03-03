FROM --platform=linux/amd64 rocker/geospatial:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# 1) Basic system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    build-essential \
    libgeos-dev \
    postgresql-client \
    tzdata \
  && rm -rf /var/lib/apt/lists/*

# 2) Install Python 3.11
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-pip

# 3) Create a venv so we can pip install
RUN python3.11 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 4) Upgrade pip
RUN pip install --upgrade pip

# 5) **Pin** numpy<2, then install PyGEOS + others
#    This ensures PyGEOS compiles against Numpy 1.x
RUN pip install "numpy<2"
RUN pip install \
    pandas \
    geopandas \
    shapely \
    networkx \
    pygeos

# 6) Install R packages
RUN install2.r --error --skipinstalled \
    rnaturalearth \
    rnaturalearthdata

WORKDIR /app
COPY . /app
CMD ["bash"]
