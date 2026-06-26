storage_account_name = "formula1storage12345"

# Read transformed data
presentation_df = spark.read.parquet(
    f"abfss://transform@{storage_account_name}.dfs.core.windows.net/users"
)

# Write to presentation layer
presentation_df.write.mode("overwrite").parquet(
    f"abfss://presentation@{storage_account_name}.dfs.core.windows.net/users"
)

# Create presentation database
spark.sql("CREATE DATABASE IF NOT EXISTS formula1_presentation")

# Read presentation data
df = spark.read.parquet(
    f"abfss://presentation@{storage_account_name}.dfs.core.windows.net/users"
)

df.createOrReplaceTempView("users")

# Sample SQL Queries
spark.sql("SELECT * FROM users").show()

spark.sql("SELECT COUNT(*) AS total_users FROM users").show()

spark.sql("""
SELECT name, email
FROM users
""").show()

spark.sql("""
SELECT phone, COUNT(*) AS total_users
FROM users
GROUP BY phone
ORDER BY total_users DESC
""").show()

spark.sql("""
SELECT name, website
FROM users
WHERE website LIKE '%.org'
""").show()