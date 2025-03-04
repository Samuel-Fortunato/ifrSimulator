import svg
import numpy as np
import math

_size = 512

_centerX = _size / 2
_centerY = _size / 2

_radius = _size / 2

_stroke_w = _size / 64

_big_tick_size = _size / 16
_big_spacing = _size / 64
_big_tick_number = 10
_big_tick_width = _stroke_w

_small_tick_size = _size / 32
_small_spacing = _size / 32
_small_tick_number = 50
_small_tick_width = _stroke_w / 2

_window_size_x = (1/8) * _size
_window_size_y = (3/4) * _window_size_x
_window_position_x = (3/4) * _size
_window_padding = _size / 64

_pointer_size_x = _size / 16
_pointer_size_y = _stroke_w
_arrow_size = _pointer_size_x / 2



_alt_txt_size = int(_size / 8)
_alt_txt_radius = (5/8) * _radius
_prss_txt_size = int(_window_size_x / 4)
_prss_txt_x = _window_size_x / 16


_prss_min = 925
_prss_big_scale = 5

_prss_big_tick_size = _window_size_x / 4
_prss_big_spacing_right = _window_size_x / 16
_prss_big_tick_width = _stroke_w / 4
_prss_big_tick_number = 30

_prss_small_tick_size = _window_size_x / 8
_prss_small_spacing_right = _window_size_x / 16
_prss_small_tick_width = _stroke_w / 8
_prss_small_tick_number = 150


# ---------------------------------------------//---------------------------------------------

def calculate_text_x(i):
    return _centerX + _alt_txt_radius * math.sin(i * ((2 * math.pi) / _big_tick_number))

def calculate_text_y(i):
    return _centerY - _alt_txt_radius * math.cos(i * ((2 * math.pi) / _big_tick_number))


bg_element_list = [
    svg.Defs(
        elements = [
            # pressure rectangle mask
            svg.Mask(
                id = "pressureRect",
                elements = [
                    svg.Rect(
                        x = 0, y = 0, width = _size, height = _size,
                        fill = "white",
                    ),
                    svg.Rect(
                        x = _window_position_x, y = _centerY - _window_size_y / 2 + _window_padding,
                        width = _window_size_x, height = _window_size_y,
                        fill = "black",
                    )
                ]
            )
        ]
    ),

    # background
    svg.Rect(
        x = 0, y = 0, width = _size, height = _size,
        fill = "gray",
        mask = "url(#pressureRect)"
    ),

    # altimeter circle
    svg.Circle(
        cx = _centerX, cy = _centerY, r = _radius - _stroke_w / 2,
        stroke = "white", fill = "black",
        stroke_width = _stroke_w,
        mask = "url(#pressureRect)"
    ),

    # center
    svg.Circle(
        cx = _centerX, cy = _centerY, r = _radius / 32,
        fill = "white"
    ),

    # pressure rectangle
    svg.Rect(
        x = _window_position_x, y = _centerY - _window_size_y / 2 + _window_padding,
        width = _window_size_x, height = _window_size_y,
        stroke = "white",
        stroke_width = _stroke_w / 2,
        mask = "url(#pressureRect)"
    ),

    # pressure pointer
    svg.Rect(
        x = _size - _pointer_size_x - _stroke_w - _big_spacing, y = _centerY - _pointer_size_y / 2 + _window_padding,
        width = _pointer_size_x, height = _pointer_size_y,
        fill = "white"
    ),
    svg.Polygon(
        points = [
            _size - _pointer_size_x - _stroke_w - _big_spacing,                     _centerY - _pointer_size_y / 2 + _window_padding,
            _size - _pointer_size_x - _stroke_w - _big_spacing,                     _centerY - _pointer_size_y / 2 + _window_padding + _pointer_size_y,
            _size - _pointer_size_x - _stroke_w - _big_spacing - _arrow_size,       _centerY - _pointer_size_y / 2 + _window_padding + _pointer_size_y / 2,
        ],
        fill = "white"
    )
]

# small ticks
small_ticks_list = [
    svg.Rect(
        x = _centerX - _small_tick_width / 2,
        y = _stroke_w + _small_spacing,

        width = _small_tick_width, height = _small_tick_size,
        fill = "white",
        transform = svg.Rotate(i, _centerX, _centerY)
    )

    for i in np.linspace(0, 360, _small_tick_number + 1)
]
bg_element_list.extend(small_ticks_list)

# big ticks
big_ticks_list = [
    svg.Rect(
        x = _centerX - _big_tick_width / 2,
        y = _stroke_w + _big_spacing,

        width = _big_tick_width, height = _big_tick_size,
        fill = "white",
        transform = svg.Rotate(i, _centerX, _centerY)
    )

    for i in np.linspace(0, 360, _big_tick_number + 1)
]
bg_element_list.extend(big_ticks_list)

# numbers
bg_text_list = [
    svg.Text(
        x = calculate_text_x(i) - _alt_txt_size / 4, y = calculate_text_y(i) + _alt_txt_size / 2,
        fill = "white",
        style = f"font-size: {_alt_txt_size}px;",
        text = str(i)
    )

    for i in range(_big_tick_number)
]
bg_element_list.extend(bg_text_list)


bg_canvas = svg.SVG(
    width = _size,
    height = _size,
    elements = bg_element_list,
)

# ---------------------------------------------//---------------------------------------------

prss_element_list = [
    # background
    svg.Rect(
        x = 0, y = 0,
        width = _window_size_x, height = _size
    )
]

prss_small_tick = [
    svg.Rect(
        x = _window_size_x - _prss_small_spacing_right - _prss_small_tick_size, y = i * _size / _prss_small_tick_number,
        width = _prss_small_tick_size, height = _prss_small_tick_width,
        fill = "white"
    )

    for i in range(_prss_small_tick_number)
]
prss_element_list.extend(prss_small_tick)

prss_big_tick = [
    svg.Rect(
        x = _window_size_x - _prss_big_spacing_right - _prss_big_tick_size, y = i * _size / _prss_big_tick_number,
        width = _prss_big_tick_size, height = _prss_big_tick_width,
        fill = "white"
    )

    for i in range(_prss_big_tick_number)
]
prss_element_list.extend(prss_big_tick)

prss_txt_list = [
    svg.Text(
        x = _prss_txt_x, y = (i * _size / _prss_big_tick_number) + _prss_txt_size / 2 - _prss_big_tick_width / 2,
        fill = "white",
        style = f"font-size: {_prss_txt_size}px ;",
        text = str(_prss_min + _prss_big_scale * i)
    )

    for i in range(_prss_big_tick_number)
]
prss_element_list.extend(prss_txt_list)

prss_canvas = svg.SVG(
    width = _window_size_x,
    height = _size,
    elements = prss_element_list,
)

# ---------------------------------------------//---------------------------------------------

hand1_element_list = [

]


hand1_canvas = svg.SVG(
    width = 1,
    height = 1,
    elements = hand1_element_list,
)

# ---------------------------------------------//---------------------------------------------

hand2_element_list = [

]

hand2_canvas = svg.SVG(
    width = 1,
    height = 1,
    elements = hand2_element_list,
)


# ---------------------------------------------//---------------------------------------------

hand3_element_list = [

]

hand3_canvas = svg.SVG(
    width = 1,
    height = 1,
    elements = hand3_element_list,
)

# ---------------------------------------------//---------------------------------------------

with open("altimeter_bg.svg", "w") as file:
    file.write(bg_canvas.as_str())

with open("altimeter_prss.svg", "w") as file:
    file.write(prss_canvas.as_str())

with open("altimeter_hand1.svg", "w") as file:
    file.write(hand1_canvas.as_str())

with open("altimeter_hand2.svg", "w") as file:
    file.write(hand2_canvas.as_str())

with open("altimeter_hand3.svg", "w") as file:
    file.write(hand3_canvas.as_str())
