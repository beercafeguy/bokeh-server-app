import random

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure

app = Flask(__name__)

@app.route('/')
def homepage():
    # First Chart - Scatter Plot of squares
    x = [i for i in range(10)]
    y = [i * i for i in x]
    p1 = figure(height=350, sizing_mode="stretch_width",title='Square chart')
    p1.xaxis.axis_label = 'number'
    p1.yaxis.axis_label = 'square'
    p1.circle(
        x,
        y,
        size=20,
        color="red",
        alpha=0.7
    )

    # Second Chart - Bar Plot
    countries = ['India', "Pakistan", 'Bangladesh', 'Japan']
    population = [142, 23, 17, 12]

    p2 = figure(
        x_range=countries,
        height=350,
        title="Population By Country",
    )
    p1.xaxis.axis_label = 'Country Name'
    p1.yaxis.axis_label = 'Population'
    p2.vbar(x=countries, top=population, width=0.5)
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0

    script1, div1 = components(p1)
    script2, div2 = components(p2)

    # Return all the charts to the HTML template
    return render_template(
        template_name_or_list='index.html',
        script=[script1, script2],
        div=[div1, div2],
    )


# Main Driver Function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run()
