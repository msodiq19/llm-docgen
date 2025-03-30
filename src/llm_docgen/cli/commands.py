import click
from pathlib import Path
from git import Repo
from typing import Optional
import ast
from llm_docgen.parsers.python_parser import CodeAnalyzer
from llm_docgen.templating.renderer import render_template


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
        
        # Process the repository to generate documentation
        documentation_data = process_repository(repo_dir)
        
        # Render the documentation using the specified template
        rendered_docs = render_template(template, documentation_data)
        
        # Save the rendered documentation to the output directory
        output_file = output_path / f"{template}.md"  # Example output file name
        with open(output_file, "w") as f:
            f.write(rendered_docs)
        
        click.echo(f"Successfully generated docs in {output}")
        
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red", err=True)
        raise click.Abort()

def clone_repository(repo_url: str, output_dir: Path) -> Path:
    repo_name = Path(repo_url).name  # Extract the repository name from the URL
    clone_dir = output_dir / repo_name  # Use the repository name for the clone directory
    Repo.clone_from(repo_url, clone_dir)
    return clone_dir

def process_repository(repo_dir: Path) -> dict:
    """Process the repository to extract documentation data."""
    # Initialize your data structure
    documentation_data = {
        "project_name": repo_dir.name,
        "classes": [],
        "functions": []
    }

    # Iterate through Python files in the repository
    for py_file in repo_dir.rglob("*.py"):
        print(f"Processing file: {py_file}")
        with open(py_file, "r") as f:
            code = f.read()
            # Use your CodeAnalyzer to parse the code
            analyzer = CodeAnalyzer()
            analyzer.visit(ast.parse(code))
            documentation_data["classes"].extend(analyzer.classes)
            documentation_data["functions"].extend(analyzer.functions)

    # Check if any classes or functions were detected
    if not documentation_data["classes"] and not documentation_data["functions"]:
        print("Warning: No classes or functions detected in the repository.")
    
    return documentation_data