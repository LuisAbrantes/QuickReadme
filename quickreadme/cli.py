# quickreadme/cli.py

import click
from jinja2 import Environment, BaseLoader
import importlib.resources

@click.command()
def main():
    """Generates a README.md file based on user input."""
    click.echo("Welcome to QuickReadme! Let's create your README.md.")

    # Prompting user for input
    title = click.prompt('Project Title')
    description = click.prompt('Project Description')
    installation = click.prompt('Installation Instructions')
    usage = click.prompt('Usage Information')
    contribution = click.prompt('Contribution Guidelines', default='Contributions are welcome!')
    license = click.prompt('License', default='MIT')

    # Load the template content
    template_content = importlib.resources.read_text('quickreadme.templates', 'readme_template.md')

    # Set up Jinja2 environment
    env = Environment(loader=BaseLoader())
    template = env.from_string(template_content)

    # Render the content
    readme_content = template.render(
        title=title,
        description=description,
        installation=installation,
        usage=usage,
        contribution=contribution,
        license=license
    )

    # Write the README.md file
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    click.echo('README.md generated successfully!')

if __name__ == '__main__':
    main()