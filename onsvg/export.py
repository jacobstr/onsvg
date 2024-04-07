import ezdxf
import sys
import os
from ezdxf.addons.drawing import Frontend, RenderContext, pymupdf, layout, config, svg
from ezdxf import units, bbox

def dxf_to_svg(dxf_file: str, svg_file: str):
    # Load the DXF file
    doc = ezdxf.readfile(dxf_file)

    # Set units in the file to mm.
    doc.units = units.MM

    # This is all largely lifted from the ezdxf docs on exporting SVGs
    # with the notable change to use the automatic extents detection.
    # See: https://ezdxf.readthedocs.io/en/stable/tutorials/image_export.html
    msp = doc.modelspace()
    # 1. create the render context
    context = RenderContext(doc)
    # 2. create the backend
    backend = svg.SVGBackend()
    # 3. create the frontend
    frontend = Frontend(context, backend)
    # 4. draw the modelspace
    frontend.draw_layout(msp)

    # Use automatic layout Page(0,0) - to set the extents of the file automatically.
    # An alternative, or equivalent approach to determining the height and width
    # of a DXF from a top-down view:
    #
    #  extz = bbox.extents(msp)
    #  width = extz.extmin[0] - extz.extmax[0]
    #  height = extz.extmin[0] - extz.extmax[0]
    #
    # If you set a layout size here manually, then you'll end up rescaling all of your values.
    # For example, if the extents of a square in your import DXF are 100x100 and you
    # set a layout of 1000x1000 - perhaps because you want to leave room for everything - you'll
    # just end up 10x'ing the resulting size of your object.
    page = layout.Page(0, 0, layout.Units.mm, margins=layout.Margins.all(2))

    # 6. get the SVG rendering as string - this step is backend dependent
    svg_string = backend.get_string(page,settings=layout.Settings(scale=1, fit_page=False))
    with open(svg_file, "wt", encoding="utf8") as fp:
        fp.write(svg_string)
