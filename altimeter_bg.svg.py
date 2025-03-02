import cairo
import math

surfaceSize = 512
surfaceX = surfaceSize
surfaceY = surfaceSize
centerX = surfaceX / 2
centerY = surfaceY / 2

radius = surfaceSize / 2
bigTick = surfaceSize / 16

lineWidth = surfaceSize / 32

def draw():
    with cairo.SVGSurface("altimeter_bg.svg", surfaceX, surfaceY) as surface:

        ctx = cairo.Context(surface)

        # Background
        ctx.set_source_rgb(0, 0, 0)

        ctx.move_to(0, 0)
        ctx.line_to(surfaceX, 0)
        ctx.line_to(surfaceX, surfaceY)
        ctx.line_to(0, surfaceY)
        ctx.close_path()

        ctx.fill()

        # Circle
        ctx.arc(centerX, centerY, radius - lineWidth/2, 0, 2 * math.pi)

        ctx.set_line_width(lineWidth)
        ctx.set_source_rgb(0, 0, 0.6)
        ctx.stroke_preserve()
        ctx.set_source_rgb(0.4, 0.4, 0.4)
        ctx.fill()

        # Ticks
        ctx.translate(centerX, centerY)

        ctx.move_to(0, radius)
        ctx.line_to(0, radius - bigTick)
        ctx.set_line_width(lineWidth)
        ctx.set_source_rgb(1, 1, 1)
        ctx.stroke()

    print("File Saved")

if (__name__ == "__main__"):
    draw();
