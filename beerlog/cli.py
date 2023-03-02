from typing import Optional
import typer
from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Add a new Beer to the Database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer add to the database")
    

@main.command("list")
def list_beers(style: Optional[str] = None):
    """List Beers in Database"""
    beer = get_beers_from_database()
    print(beer)