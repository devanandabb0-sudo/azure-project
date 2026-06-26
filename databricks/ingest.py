from pyspark.sql import SparkSession

storage_account_name = "formula1storage12345"

spark = SparkSession.builder.appName("UsersIngestion").getOrCreate()

# Azure ADLS Authentication
spark.conf.set(
    f"fs.azure.account.auth.type.{storage_account_name}.dfs.core.windows.net",
    "OAuth"
)

spark.conf.set(
    f"fs.azure.account.oauth.provider.type.{storage_account_name}.dfs.core.windows.net",
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.id.{storage_account_name}.dfs.core.windows.net",
    "<client-id>"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.secret.{storage_account_name}.dfs.core.windows.net",
    "<client-secret>"
)

spark.conf.set(
    f"fs.azure.account.oauth2.client.endpoint.{storage_account_name}.dfs.core.windows.net",
    "https://login.microsoftonline.com/<tenant-id>/oauth2/token"
)

# Read JSON
df = spark.read.json(
    f"abfss://raw@{storage_account_name}.dfs.core.windows.net/data_862ef7cb-427f-4390-bb32-ef4c5a860e99_a402765a-b179-452b-bef5-bf589bdc7130.json"
)

# Save to Ingested Container
df.write.mode("overwrite").parquet(
    f"abfss://ingested@{storage_account_name}.dfs.core.windows.net/users"
)