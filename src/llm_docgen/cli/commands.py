import click
from pathlib import Path
from git import Repo
from typing import Optional

@click.group()
def cli():
    """LLM Documentation Generator"""

@cli.command()
@click.option("--repo", required=True, help="Git repository URL or local path")
@click.option("--output", default="docs", help="Output directory")
@click.option("--template", default="default", help="Template name")
def generate(repo: str, output: str, template: str):
    """Generate documentation from a repository"""
    try:
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        
        click.echo(f"Cloning repository from {repo}...")
        if repo.startswith("http"):
            repo_dir = clone_repository(repo, output_path)
        else:
            repo_dir = Path(repo)
        click.echo("Repository cloned successfully.")
        # Process repository here
        click.echo(f"Successfully generated docs in {output}")
        
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red", err=True)
        raise click.Abort()

def clone_repository(repo_url: str, output_dir: Path) -> Path:
    clone_dir = output_dir / "repo"
    Repo.clone_from(repo_url, clone_dir)
    return clone_dir