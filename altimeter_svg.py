import cairo
import math

with cairo.SVGSurface("altimeter_bg.svg", 512, 512) as surface:

    context = cairo.Context(surface)

    context.arc(256, 256, 252, 0, 2 * math.pi)

    context.set_line_width(8)
    context.set_source_rgba(1, 0, 0, 1)
    context.stroke()

print("File Saved")
