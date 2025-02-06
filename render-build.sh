#!/bin/bash

# Install system dependencies for SQL Server ODBC Driver
apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    curl \
    gnupg

# Download and install the Microsoft ODBC Driver 17 for SQL Server
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17