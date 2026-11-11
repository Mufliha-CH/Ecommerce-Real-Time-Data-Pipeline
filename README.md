# Ecommerce Real-Time Data Pipeline

## Project Overview

This project demonstrates a real-time ecommerce order processing pipeline using Python, Apache Kafka, Aiven, Databricks, Delta Lake and Power BI.

The pipeline generates ecommerce orders, streams them through Kafka, processes and cleans the incoming data in Databricks, stores the results in Delta tables, and visualizes business insights through an interactive Power BI dashboard.

## Architecture

**Python → Aiven Kafka → Databricks → Delta Lake → Power BI**

## Technologies Used

- **Python:** Ecommerce order generation and Kafka producer.
- **Apache Kafka:** Real-time message streaming.
- **Aiven:** Managed Kafka service.
- **Databricks:** Data ingestion, transformation and processing.
- **PySpark:** Data cleaning and transformation.
- **Delta Lake:** Reliable storage and data management.
- **Power BI:** Interactive dashboard and business analytics.

## Project Workflow

1. **Order Generation**
   - Generate ecommerce orders using Python.
   - Include customer IDs, products, quantities, prices, timestamps and order statuses.

2. **Data Streaming**
   - Publish ecommerce orders to the Aiven Kafka topic.
   - Stream incoming messages continuously.

3. **Data Ingestion**
   - Read Kafka messages using Databricks.
   - Store raw messages in a Delta table.

4. **Data Processing**
   - Parse JSON messages.
   - Validate order statuses.
   - Remove duplicate order IDs by retaining the latest message.
   - Calculate total order amounts.
   - Extract order dates.

5. **Data Storage**
   - Store cleaned and processed orders in Delta tables.
   - Use Delta MERGE to insert new orders and update existing orders.

6. **Automation**
   - Schedule Databricks notebook execution using Databricks Jobs.
   - Process newly available Kafka messages on an hourly schedule.

7. **Data Visualization**
   - Connect Power BI to Databricks.
   - Build an interactive ecommerce dashboard to monitor sales and order performance.

## Key Features

- Real-time ecommerce order streaming.
- Automated data ingestion.
- Data cleaning and validation.
- Duplicate detection and handling.
- Dynamic order status tracking.
- Incremental data processing using Delta MERGE.
- Automated Databricks job execution.
- Interactive Power BI reporting.

## Order Statuses

The pipeline supports four order statuses:

- PLACED
- SHIPPED
- DELIVERED
- CANCELLED

## Repository Structure

```text
Ecommerce-Real-Time-Data-Pipeline/
│
├── python/
│   ├── generate_orders.py
│   └── continuous_order.py
│
├── databricks/
│   └── Ecommerce_Kafka_Connection_Test.ipynb
│
├── powerbi/
│   └── Dashboard screenshots
│
├── README.md
└── .gitignore
```

## Business Insights

The Power BI dashboard helps analyze:

- Total Revenue
- Total Orders
- Average Order Value
- Customer Performance
- Product-wise Sales
- Daily Sales Trends
- Order Status Distribution

## Learning Outcomes

Through this project, I gained practical experience in:

- Building a Kafka-based data streaming pipeline.
- Integrating Python with Apache Kafka.
- Working with Aiven managed Kafka.
- Processing streaming data using Databricks and PySpark.
- Implementing Delta Lake operations.
- Handling duplicate records and data quality.
- Automating data processing with Databricks Jobs.
- Creating interactive dashboards using Power BI.

## Security Notice

Credentials, API tokens, passwords, certificates and other sensitive configuration files are excluded from this repository.

## Project Status

Core data generation, Kafka streaming, Databricks processing and Power BI dashboard development have been implemented. Further improvements and automation are ongoing.

---

**Developed as a Data Engineering and Analytics Portfolio Project.**
