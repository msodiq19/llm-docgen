import click

@click.command()
@click.option("--repo", help="GitHub repo URL or local path", required=True)
@click.option("--output", help="Output directory", default="./docs")
@click.option("--template", help="Template name", default="default")
def main(repo, output, template):
    """Generate docs for LLM projects."""
    click.echo(f"Generating docs for {repo}...")
    # TODO: Implement core logic

if __name__ == "__main__":
    main()