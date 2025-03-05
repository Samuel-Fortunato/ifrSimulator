import svg
import os

from altimeter_constants import *
from color_palette import COLOR_PALETTE as colors

prss_element_list = [
    # background
    svg.Rect(
        x = 0, y = 0,
        width = window_size_x, height = size
    )
]

prss_small_tick = [
    svg.Rect(
        x = window_size_x - prss_small_spacing_right - prss_small_tick_size, y = i * size / prss_small_tick_number,
        width = prss_small_tick_size, height = prss_small_tick_width,
        fill = colors["instrument-hilt"]
    )

    for i in range(prss_small_tick_number)
]
prss_element_list.extend(prss_small_tick)

prss_big_tick = [
    svg.Rect(
        x = window_size_x - prss_big_spacing_right - prss_big_tick_size, y = i * size / prss_big_tick_number,
        width = prss_big_tick_size, height = prss_big_tick_width,
        fill = colors["instrument-hilt"]
    )

    for i in range(prss_big_tick_number)
]
prss_element_list.extend(prss_big_tick)

prss_txt_list = [
    svg.Text(
        x = prss_txt_x, y = (i * size / prss_big_tick_number) + prss_font_size / 2 - prss_big_tick_width / 2,
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {prss_font_size}px;",
        text = str(prss_min + prss_big_scale * i)
    )

    for i in range(prss_big_tick_number)
]
prss_element_list.extend(prss_txt_list)





prss_canvas = svg.SVG(
    width = window_size_x,
    height = size,
    elements = prss_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(prss_canvas.as_str())

print(f"SVG file saved at: {output_file}")
