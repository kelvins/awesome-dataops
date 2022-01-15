# Awesome DataOps [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome DataOps tools.

- [Awesome DataOps](#awesome-dataops)
    - [Data Catalog](#data-catalog)
    - [Data Exploration](#data-exploration)
    - [Data Ingestion](#data-ingestion)
    - [Data Lake](#data-lake)
    - [Data Platform](#data-platform)
    - [Data Processing](#data-processing)
        - [Batch Processing](#batch-processing)
        - [Stream Processing](#stream-processing)
    - [Data Quality](#data-quality)
    - [Data Serialization](#data-serialization)
    - [Data Visualization](#data-visualization)
    - [Data Warehouse](#data-warehouse)
    - [Data Workflow](#data-workflow)
    - [Database](#database)
        - [Columnar Database](#columnar-database)
        - [Document-Oriented Database](#document-oriented-database)
        - [Graph Database](#graph-database)
        - [Key-Value Database](#key-value-database)
        - [Relational Database](#relational-database)
        - [Time Series Database](#time-series-database)
        - [Vector Database](#vector-database)
    - [File System](#file-system)
    - [Logging and Monitoring](#logging-and-monitoring)
    - [SQL Query Engine](#sql-query-engine)
- [Resources](#resources)
    - [Articles](#articles)
    - [Books](#books)
    - [Events](#events)
    - [Other Lists](#other-lists)
    - [Slack](#slack)
- [Contributing](#contributing)

---

## Data Catalog

*Tools related to data cataloging.*

* [Amundsen](https://www.amundsen.io/) - Data discovery and metadata engine for improving the productivity when interacting with data.
* [Apache Atlas](https://atlas.apache.org) - Provides open metadata management and governance capabilities to build a data catalog.
* [CKAN](https://github.com/ckan/ckan) - Open-source DMS (data management system) for powering data hubs and data portals.
* [DataHub](https://github.com/linkedin/datahub) - LinkedIn's generalized metadata search & discovery tool.
* [Magda](https://github.com/magda-io/magda) - A federated, open-source data catalog for all your big data and small data.
* [Metacat](https://github.com/Netflix/metacat) - Unified metadata exploration API service for Hive, RDS, Teradata, Redshift, S3 and Cassandra.
* [OpenMetadata](https://open-metadata.org/) - A Single place to discover, collaborate and get your data right.

## Data Exploration

*Tools for performing data exploration.*

* [Apache Zeppelin](https://zeppelin.apache.org/) - Enables data-driven, interactive data analytics and collaborative documents.
* [BambooLib](https://github.com/tkrabel/bamboolib) -  An intuitive GUI for Pandas DataFrames.
* [Google Colab](https://colab.research.google.com) - Hosted Jupyter notebook service that requires no setup to use.
* [Jupyter Notebook](https://jupyter.org/) - Web-based notebook environment for interactive computing.
* [JupyterLab](https://jupyterlab.readthedocs.io) - The next-generation user interface for Project Jupyter.
* [Jupytext](https://github.com/mwouts/jupytext) - Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts.
* [Polynote](https://polynote.org/) - The polyglot notebook with first-class Scala support.

## Data Ingestion

*Tools for performing data ingestion.*

## Data Lake

*Tools related to storing data in data lakes.*

* [LakeFS](https://github.com/treeverse/lakeFS) - Open source tool that transforms your object storage into a Git-like repository.

## Data Workflow

*Tools related to data workflow/pipeline.*

* [Airflow](https://github.com/apache/airflow) - A platform to programmatically author, schedule, and monitor workflows.
* [Azkaban](https://github.com/azkaban/azkaban) - Batch workflow job scheduler created at LinkedIn to run Hadoop jobs.
* [Dagster](https://github.com/dagster-io/dagster) - An orchestration platform for the development, production, and observation of data assets.
* [Luigi](https://github.com/spotify/luigi) - Python module that helps you build complex pipelines of batch jobs.
* [Prefect](https://docs.prefect.io/) - A workflow management system, designed for modern infrastructure.

## Data Platform

*Tools with multiple purposes related to data operations.*

* [Dremio](https://www.dremio.com/) - Power high-performing BI dashboards and interactive analytics directly on data lake.

## Data Processing

*Tools related to data processing (batch and stream).*

### Batch Processing

### Stream Processing

## Data Quality

*Tools for ensuring data quality.*

* [Cerberus](https://github.com/pyeve/cerberus) - Lightweight, extensible data validation library for Python.
* [Great Expectations](https://greatexpectations.io) - A Python data validation framework that allows to test your data against datasets.
* [JSON Schema](https://json-schema.org/) - A vocabulary that allows you to annotate and validate JSON documents.

## Data Serialization

*Tools related to serializing data.*

* [Avro]()
* [Delta Lake]()
* [Parquet]()
* [Snappy]()

## Data Visualization

*Tools for performing data visualization (DataViz).*

* [Count](https://count.co) - SQL/drag-and-drop querying and visualisation tool based on notebooks.
* [Dash](https://github.com/plotly/dash) - Analytical Web Apps for Python, R, Julia, and Jupyter.
* [Data Studio](https://datastudio.google.com) - Reporting solution for power users who want to go beyond the data and dashboards of GA.
* [HUE](https://github.com/cloudera/hue) - A mature SQL Assistant for querying Databases & Data Warehouses.
* [Lux](https://github.com/lux-org/lux) - Fast and easy data exploration by automating the visualization and data analysis process.
* [Metabase](https://www.metabase.com/) - The simplest, fastest way to get business intelligence and analytics to everyone.
* [Redash](https://redash.io/) - Connect to any data source, easily visualize, dashboard and share your data.
* [Superset](https://github.com/apache/superset) - A modern data exploration and data visualization platform.
* [Tableau](https://www.tableau.com) - Powerful and fastest growing data visualization tool used in the business intelligence industry.

## Data Warehouse

*Tools related to storing data in data warehouses (DW).*

* [Hive](https://github.com/apache/hive) - Facilitates reading, writing, and managing large datasets residing in distributed storage.

## Database

*Database tools for storing data.*

### Columnar Database

* [Cassandra](https://github.com/apache/cassandra) - Open source column based DBMS designed to handle large amounts of data.
* [Druid](https://github.com/apache/druid) - Designed to quickly ingest massive quantities of event data, and provide low-latency queries.
* [HBase](https://github.com/apache/hbase) - An open-source, distributed, versioned, column-oriented store.
* [Scylla](https://github.com/scylladb/scylla) - Designed to be compatible with Cassandra while achieving significantly higher throughputs and lower latencies.

### Document-Oriented Database

* [CouchDB](https://github.com/apache/couchdb) - An open-source document-oriented NoSQL database, implemented in Erlang.
* [Elasticsearch](https://github.com/elastic/elasticsearch) - A distributed document oriented database with a RESTful search engine.
* [MongoDB](https://github.com/mongodb/mongo) - A cross-platform document-oriented database that uses JSON-like documents with optional schemas.
* [RethinkDB](https://github.com/rethinkdb/rethinkdb) - The first open-source scalable database built for realtime applications.

### Graph Database

* [ArangoDB](https://github.com/arangodb/arangodb) - A scalable open-source multi-model database natively supporting graph, document and search.
* [Neo4j](https://github.com/neo4j/neo4j) - A high performance graph store with all the features expected of a mature and robust database.
* [Titan](https://github.com/thinkaurelius/titan) - A highly scalable graph database optimized for storing and querying large graphs.

### Key-Value Database

* [Accumulo](https://github.com/apache/accumulo) - A sorted, distributed key/value store that provides robust, scalable data storage and retrieval.
* [etcd](https://github.com/etcd-io/etcd) - Distributed reliable key-value store for the most critical data of a distributed system.
* [Memcached](https://github.com/memcached/memcached) - A high performance multithreaded event-based key/value cache store.
* [Redis](https://github.com/redis/redis) - An in-memory key-value database that persists on disk.

### Relational Database

* [CockroachDB](https://github.com/cockroachdb/cockroach) - A cloud-native distributed SQL database designed to build, scale, and manage data-intensive applications.
* [Crate](https://github.com/crate/crate) - A distributed SQL database that makes it simple to store and analyze massive amounts of data.
* [MariaDB](https://github.com/MariaDB/server) - A replacement of MySQL with more features, new storage engines, fewer bugs, and better performance.
* [MySQL](https://github.com/mysql/mysql-server) - One of the most popular open source transactional databases.
* [PostgreSQL](https://github.com/postgres/postgres) - An advanced RDBMS that supports an extended subset of the SQL standard.
* [RQLite](https://github.com/rqlite/rqlite) - A lightweight, distributed relational database, which uses SQLite as its storage engine.

### Time Series Database

* [Akumuli](https://github.com/akumuli/Akumuli) - Can be used to capture, store and process time-series data in real-time.
* [InfluxDB](https://github.com/influxdata/influxdb) - Scalable datastore for metrics, events, and real-time analytics.
* [QuestDB](https://github.com/questdb/questdb) - An open source SQL database designed to process time series data, faster.
* [TimescaleDB](https://github.com/timescale/timescaledb) - Open-source time-series SQL database optimized for fast ingest and complex queries.

### Vector Database

* [Milvus](https://github.com/milvus-io/milvus/) - An open source embedding vector similarity search engine powered by Faiss, NMSLIB and Annoy.
* [Pinecone](https://www.pinecone.io) - Managed and distributed vector similarity search used with a lightweight SDK.

## File System

*Tools related to file system and data storage.*

* [GCS]()
* [HDFS]()
* [MinIO]()
* [S3]()
* [Swift]()

## Logging and Monitoring

*Tools used for logging and monitoring data workflows.*

* [Grafana](https://github.com/grafana/grafana) - Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, InfluxDB and many more.
* [Loki](https://github.com/grafana/loki) - A horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.
* [Prometheus](https://github.com/prometheus/prometheus) - A monitoring system and time series database.

## SQL Query Engine

*Tools for parallel processing SQL statements.*

* [Drill](https://github.com/apache/drill) - Schema-free SQL Query Engine for Hadoop, NoSQL and Cloud Storage.
* [Impala](https://github.com/apache/impala) - Lightning-fast, distributed SQL queries for petabytes of data.
* [Presto](https://github.com/prestodb/presto) - A distributed SQL query engine for big data.
* [Trino](https://github.com/trinodb/trino) - A fast distributed SQL query engine for big data analytics.

---

# Resources

Where to discover new tools and discuss about existing ones.

## Articles

## Books

* [Data Mesh: Delivering Data-Driven Value at Scale](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (O'Reilly)
* [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/) (O'Reilly)
* [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) (O'Reilly)
* [Getting Started with Impala](https://www.oreilly.com/library/view/getting-started-with/9781491905760/) (O'Reilly)
* [Learning and Operating Presto](https://www.oreilly.com/library/view/learning-and-operating/9781492095125/) (O'Reilly)
* [Learning Spark: Lightning-Fast Data Analytics](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (O'Reilly)
* [Spark in Action](https://www.oreilly.com/library/view/spark-in-action/9781617295522/) (O'Reilly)
* [Spark: The Definitive Guide](https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/) (O'Reilly)

## Events

## Other Lists

* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
* [DataOps Resource](https://github.com/chen1649chenli/dataOpsResource)

## Slack

* [Delta Lake Workspace](https://delta-users.slack.com/ssb/redirect)
* [Trino Workspace](https://trinodb.slack.com/ssb/redirect)

---

# Contributing

All contributions are welcome! Please take a look at the [contribution guidelines](https://github.com/kelvins/awesome-dataops/blob/main/CONTRIBUTING.md) first.
