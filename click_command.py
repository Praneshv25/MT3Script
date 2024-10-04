import click
import subprocess


@click.group()
def cli():
    pass


# Command to run the job
@cli.command()
@click.argument('model_name')
def run(model_name):
    click.echo(f"Running job for model: {model_name}")

    try:
        subprocess.run(['sbatch', f'{model_name}.sh'], check=True)
        click.echo("Job submitted successfully!")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error in job submission: {e}", err=True)


if __name__ == '__main__':
    cli()
