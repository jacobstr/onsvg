import click
import os
from .export import dxf_to_svg

@click.command()
@click.argument("input_dxf")
@click.option('-o', '--output_svg', default=None)
def cli(input_dxf: str, output_svg: str):
    base, ext = os.path.splitext(input_dxf)
    if output_svg is None:
        base, ext = os.path.splitext(input_dxf)
        output_svg = f"{base}.svg"
    dxf_to_svg(input_dxf, output_svg)
