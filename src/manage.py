#! /usr/bin/env python
import os
from pathlib import Path
import uvicorn
import click
import subprocess
import signal
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config.settings import config

# CONSTANTS
DOCKER_PATH = os.path.join(Path.cwd().parent, "docker")


@click.group()
def cli():
    pass


## HELPER METHODS
def get_docker_compose_file():
    # TODO: read it from env
    compose_file = "dev"
    return os.path.join(DOCKER_PATH, f"{compose_file}.yml")


def run_sql(statements):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOSTNAME"),
        port=os.getenv("POSTGRES_PORT"),
    )

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    for statement in statements:
        cursor.execute(statement)

    cursor.close()
    conn.close()


@cli.command()
def init_postgres():
    try:
        run_sql([f"CREATE DATABASE {os.getenv('POSTGRES_DB')}"])
    except psycopg2.errors.DuplicateDatabase:
        print(
            (
                f"The database {os.getenv('POSTGRES_DB')} already",
                "exists and will not be recreated",
            )
        )


def docker_compose_cmdline(commands_string=None):
    compose_file = get_docker_compose_file()

    if not os.path.isfile(compose_file):
        raise ValueError(f"The file {compose_file} does not exist")

    command_line = [
        "docker-compose",
        "-f",
        compose_file,
    ]

    if commands_string:
        command_line.extend(commands_string.split(" "))

    return command_line


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("subcommand", nargs=-1, type=click.Path())
def compose(subcommand):
    cmdline = docker_compose_cmdline() + list(subcommand)
    print(cmdline)
    print("compose file ")

    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


@cli.command()
def runserver():
    uvicorn.run(
        host="0.0.0.0",
        port=8000,
        app="config.server:app",
        reload=True if config.ENVIRONMENT != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    cli()
