# Requirements

The following requirements are needed to build and run the project:

- `pipenv`: needed to install the Python environment and dependencies and to run the application
- `docker`: to containerize the processes
- `docker-compose`: to run and scale the processes in a production-like environment
- `pre-commit`: to validate code changes upon commit

# Execution

Run the processes:

```shell
docker-compose up --detach
```

Watch the execution logs:

```shell
docker-compose logs --follow
```

Monitor the running processes

```shell
watch -n1 docker-compose ps
```

Scale up the consumers

```shell
docker-compose up --no-recreate --detach --scale consumer=10
```
