# Azure Data Engineering Project Workflow

## Overview

This project demonstrates an end-to-end Azure Data Engineering pipeline using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, and Power BI.

## Workflow

1. Upload the `users.json` file to the **ingest** container in Azure Storage.
2. Azure Data Factory reads the JSON file from the storage account.
3. Azure Databricks executes a PySpark notebook to flatten the nested JSON structure.
4. The transformed data is written as a Parquet file to the **processed** container.
5. Power BI imports the flattened data and creates interactive dashboards.

## Technologies Used

- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- PySpark
- Power BI Desktop
- Git & GitHub

## Output

- Flattened Parquet file
- Excel file for reporting
- Interactive Power BI dashboard