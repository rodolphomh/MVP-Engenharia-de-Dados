# /src/bronze/bronze_ingestion.py

from pyspark.sql import SparkSession

class Collector:
    def __init__(self, spark: SparkSession, volume_path: str, catalog: str, schema: str, table: str):
        self.spark = spark
        self.volume_path = volume_path
        self.catalog = catalog
        self.schema = schema
        self.table_name = table
        self.full_table_path = f'{self.catalog}.{self.schema}.{self.table_name}'
        
    def ingest_bronze(self) -> None:
        """
        Lê o arquivo CSV de origem da landing zone (Volume)
        e o salva na camada Bronze em formato Delta.
        """
        try:
            df = self.spark.read.csv(
                self.volume_path, 
                sep=',', 
                header=True, 
                inferSchema=True
            )
 
            # Garante que os nomes das colunas sejam compatíveis com o Delta
            clean_cols = [c.replace(' ', '_').replace('(', '').replace(')', '') for c in df.columns]
            df = df.toDF(*clean_cols)

            df.write \
                .format('delta') \
                .mode('overwrite') \
                .option('overwriteSchema', 'true') \
                .saveAsTable(self.full_table_path)

            print(f"Tabela '{self.full_table_path}' carregada com sucesso!")

        except Exception as e:
            print(f"Erro ao carregar dados para a camada bronze: {e}")

    def run(self) -> None:
        self.ingest_bronze()
        print('Ingestão da camada Bronze completa!')