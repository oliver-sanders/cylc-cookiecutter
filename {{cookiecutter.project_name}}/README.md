# {{ cookiecutter.project_name }}

{% set rose = cookiecutter.use_rose_configurations == 'yes' -%}

This is a simple example Cylc workflow{% if rose %} with Rose{% endif %}.


## Requirements

To run this workflow you will need to install Cylc{% if rose %} and Rose{% endif %}.

| Conda | Pip |
| ---   | --- |
{%- if rose %}
| `conda install cylc-flow metomi-rose` | `pip install cylc-flow metomi-rose` |
{%- else %}
| `conda install cylc-flow` | `pip install cylc-flow` |
{%- endif %}


## Running

To run the workflow run:

```console
$ cylc vip .
```

To see which workflows you are running run:

```console
$ cylc scan
```


## Stopping

To stop a workflow run:

```bash
cylc stop <workflow-id>         # wait for active tasks to finish, then shut down
cylc stop <workflow-id> --kill  # kill active tasks, then shut down
cylc stop <workflow-id> --now   # leave active tasks running and shut down
```

You can restart the workflow later, Cylc will pick up where it left off:

```bash
cylc play <workflow-id>
```


## Deleting

Once you are finished with an installation of a workflow, remove it by running:

```bash
cylc clean <workflow-id>
```


## Developing

You can validate the workflow configuration by running:

```
cylc validate <workflow-id>
```

And you can check the configuration file style by running:

```
cylc lint <workflow-id>
```

For more information on writing workflows see the
[user guide](https://cylc.github.io/cylc-doc/stable/html/user-guide/writing-workflows/index.html).

There is also a
[workflow design guide](https://cylc.github.io/cylc-doc/stable/html/workflow-design-guide/index.html).
