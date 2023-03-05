import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput,Div,Spinner
from bokeh.plotting import figure

N = 200
x = np.linspace(0, 4 * np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(title="sine wave")
line = plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)

div = Div(text="<p>Select Size</p>")
spinner = Spinner(title="Line Width",low=0,high=20,step=1,value=int(line.glyph.line_width),width=200)
spinner.js_link("value",line.glyph,"line_width")

textinput = TextInput(value=line.glyph.line_color,width=200)
textinput.js_link("value",line.glyph,"line_color")

def update_data(attrname, old, new):
    a = 1
    b = 0
    w = 0
    k = freq.value
    x = np.linspace(0, 4 * np.pi, N)
    y = a * np.sin(k * x + w) + b
    source.data = dict(x=x, y=y)


freq.on_change('value', update_data)
curdoc().add_root(row(freq,spinner,textinput, plot, width=500))
curdoc().title = "Sliders, Selectors and text box"
