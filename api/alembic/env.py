
import os
from dotenv import load_dotenv
load_dotenv(f"config/.env.{os.environ.get('APP_ENV', 'dev')}")


from logging.config import fileConfig
import sys
from pathlib import Path

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

sys.path.append(str(Path(__file__).parent.parent))

from database import Base
from config.config import DbSettings

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

dbsettings = DbSettings()
SQLALCHEMY_DATABASE_URL = f"postgresql://{dbsettings.POSTGRES_USER}:{dbsettings.POSTGRES_PASSWORD}@{dbsettings.POSTGRES_HOSTNAME}:{dbsettings.DATABASE_PORT}/{dbsettings.POSTGRES_DB}"

target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        {
            "sqlalchemy.url": SQLALCHEMY_DATABASE_URL,
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
