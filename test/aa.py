import click


@click.command()
@click.option("--test", default=1, help="number of greetings")
@click.argument("name")
def hello(test, name):
    print(test)
    for x in range(test):
        click.echo("Hello %s!" % name)


if __name__ == "__main__":
    hello()
