
This project demonstrates Linux + Docker + Prometheus + Grafana + PostgreSQL + Python + Ollama + RAG + ChromaDB working together as a complete AIOps (AI for IT Operations) solution.


Project Objective

The goal of this project is to build an AI-Powered Incident Management System that can:

Monitor server health (CPU, Memory, Disk)
Detect issues automatically
Generate alerts
Store incidents in PostgreSQL
Use AI (Ollama) to analyze incidents
Suggest troubleshooting steps using RAG
Display everything in Grafana
Overall Workflow
Plain Text
Ubuntu VM
│
▼
Node Exporter
│
▼
Prometheus
│
▼
Grafana Dashboard
│
▼
Alert Trigger
│
▼
PostgreSQL
│
▼
RAG Knowledge Base
│
▼
Ollama LLM
│
▼
AI Recommendation
Tools Used
1. Docker
Purpose

Used to run all services as containers.

Containers:

Plain Text
Grafana
Prometheus
Node Exporter
PostgreSQL

Commands:

Shell
docker ps
docker run
docker restart
2. Node Exporter
Purpose

Collects Linux server metrics.

Examples:

Plain Text
CPU Usage
Memory Usage
Disk Usage
Network Usage
Filesystem Usage

Node Exporter acts like a sensor on the server.

Plain Text
Ubuntu VM
↓
Node Exporter

Port:

Plain Text
9100
3. Prometheus
Purpose

Collects metrics from Node Exporter.

Example:

Plain Text
CPU = 90%
Memory = 80%
Disk = 70%

Prometheus stores time-series data.

Plain Text
Node Exporter
↓
Prometheus

Port:

Plain Text
9090
4. Grafana
Purpose

Creates dashboards and alerts.

Shows:

Plain Text
CPU Utilization
Memory Utilization
Disk Utilization
Incidents
AI Recommendations

Port:

Plain Text
3000
5. PostgreSQL
Purpose

Stores incident records.

Example:

Plain Text
Incident ID
Severity
Alert Name
Description
AI Recommendation
Timestamp

Example Table:

SQL
incidents
Plain Text
1 | High CPU | Critical
2 | Memory Alert | Warning
6. Ollama
Purpose

Runs AI models locally.

Example models:

Plain Text
llama3
mistral
phi3

Commands:

Shell
ollama serve
ollama pull llama3
7. RAG (Retrieval Augmented Generation)
Purpose

Provides AI with company troubleshooting documents.

Without RAG:

Plain Text
AI guesses answer

With RAG:

Plain Text
AI reads runbooks first

Example files:

Plain Text
cpu-troubleshooting.txt
memory-troubleshooting.txt
disk-recovery.txt
postgres-recovery.txt
8. ChromaDB
Purpose

Stores document embeddings.

Example:

Plain Text
Runbook
↓
Embedding
↓
ChromaDB

AI searches ChromaDB before answering.

9. Python
Purpose

Acts as the glue between components.

Responsibilities:

Plain Text
Read alerts
Query PostgreSQL
Query ChromaDB
Call Ollama
Store recommendations

Files:

Plain Text
app.py
rag.py
ingest.py
Example Incident Flow
Step 1

CPU reaches:

Plain Text
95%
Step 2

Node Exporter collects metric.

Plain Text
CPU = 95%
Step 3

Prometheus scrapes metric.

Plain Text
CPU = 95%
Step 4

Grafana alert triggers.

Plain Text
High CPU Alert
 
Step 5

Python application receives alert.

Step 6

Incident stored in PostgreSQL.

Plain Text
Incident ID: 101
Severity: Critical
Step 7

RAG searches documents.

Plain Text
cpu-troubleshooting.txt
Step 8

Ollama generates recommendation.

Example:

Plain Text
Root Cause:
CPU utilization exceeded threshold.
 
Resolution:
1. Check top processes
2. Restart affected service
3. Scale resources if required
Step 9

Response stored in PostgreSQL.

Plain Text
AI Recommendation Added
Step 10

Grafana dashboard displays:

Plain Text
Incident
Severity
Recommendation
Status
Final Dashboard Components
Monitoring Dashboard
Plain Text
CPU Usage %
Memory Usage %
Disk Usage %
Network Usage %
Incident Dashboard
Plain Text
Total Incidents
Open Incidents
Closed Incidents
Critical Incidents
AI Dashboard
Plain Text
AI Recommendations
Incident History
Recent Alerts
Knowledge Base Results
What You Demonstrate in This Project

✅ Docker Administration

✅ Linux Monitoring

✅ Prometheus

✅ Grafana

✅ PostgreSQL

✅ Python Automation

✅ AI/LLM Integration

✅ Ollama

✅ RAG Implementation

✅ Incident Management

✅ End-to-End DevOps + AI Project

This is essentially a mini AIOps platform, where infrastructure monitoring, alerting, databases, AI, and RAG all work together to automatically analyze and help resolve production incidents.
