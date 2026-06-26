from pyspark.sql.functions import col, upper, lower, trim

storage_account_name = "formula1storage12345"

# Read ingested data
df = spark.read.parquet(
    f"abfss://ingested@{storage_account_name}.dfs.core.windows.net/users"
)

# Flatten JSON
users_flattened_df = df.select(
    col("id"),
    col("name"),
    col("username"),
    col("email"),
    col("phone"),
    col("website"),
    col("address.street").alias("street"),
    col("address.suite").alias("suite"),
    col("address.city").alias("city"),
    col("address.zipcode").alias("zipcode"),
    col("company.name").alias("company_name")
)

# Save flattened data
users_flattened_df.write.mode("overwrite").parquet(
    f"abfss://ingested@{storage_account_name}.dfs.core.windows.net/users_flattened"
)

# Read flattened data
df_flattened = spark.read.parquet(
    f"abfss://ingested@{storage_account_name}.dfs.core.windows.net/users_flattened"
)

# Transform data
transform_df = (
    df_flattened
    .dropDuplicates()
    .dropna(subset=["email"])
    .withColumn("name", upper(trim("name")))
    .withColumn("email", lower(trim("email")))
    .withColumnRenamed("company_name", "company")
)

# Save transformed data
transform_df.write.mode("overwrite").parquet(
    f"abfss://transform@{storage_account_name}.dfs.core.windows.net/users"
)