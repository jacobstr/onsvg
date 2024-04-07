# OnSVG

OnSVG is a simple command line utility to convert an onshape exported DXF to an
SVG file while correcting for units.

The goal:

* I should be able to export a 20mm circle from onshape to a 20mm svg file and
  have it work on a shaper / laser cutter / whatever to yield a physical
  object of the appropriate size.

# Installation (Mac)

```bash
brew install pipx
pipx ensurepath
pipx install git@github.com:jacobstr/onsvg.git
```

This script is best installed with `pipx` because it relies on a variety of
external packages that may already be installed on your computer.

Rather that competing with versions that _other_ tools might already rely on,
`pipx` will install `onsvg` into an isolated environment so that your
system-wide installations will work.


# Particulars

* My onshape workspace units are set to MM. When onshape exports a DXF, it will
  seemingly have numbers that look like mm: exporting a 96x96 mm rectangle will
  yield some 96's in semi-human-readable dxf file.
* However, the `INSUNITS` attribute in the file that sets the dimensions is set
  to inches. Different tools have varying opinions on how they honor this
  property.
* Ultimately, the workflow from Onshape -> DXF -> SVG is unreliable. You're
  relying on onshape exporting the units correctly (it does not) and your
  converter program importing the units correctly. Additionally, at the export
  stage you've got yet another opportunity for fuckery as the various tools
  / dialogues again prompt for points/picas/mm/in/documents/artboards.

This script papers over that.
