import random
from flask import Flask
from ..end_to_end_scripts.helper_functions import GPTL_Timing, get_plot_test 
from bokeh.plotting import figure, output_file, save
import json
from flask import Flask, render_template 
from bokeh.embed import components 
from bokeh.plotting import figure 

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8
# from bokeh.util.strings import encode_utf8

app = Flask(__name__, template_folder="templates")

@app.route("/timeline")
def hello_world():
    p = get_plot_test()
    # output_file(filename="bokeh_saved_test.html")
    # save(p)
    
    script, div = components(p)
    return render_template(template_name_or_list="timeline_chart.html", script=script, div=div)
    return json.dumps(json_item(p, "myplot"))
    return "<p>Hello, World!</p>"

# Root endpoint 
@app.route('/') 
def homepage(): 
  
    # First Chart - Scatter Plot 
    p1 = figure(height=350, sizing_mode="stretch_width") 
    p1.circle( 
        [i for i in range(10)], 
        [random.randint(1, 50) for j in range(10)], 
        size=20, 
        color="navy", 
        alpha=0.5
    ) 
  
    # Second Chart - Line Plot 
    language = ['Python', 'JavaScript', 'C++', 'C#', 'Java', 'Golang'] 
    popularity = [85, 91, 63, 58, 80, 77] 
  
    p2 = figure( 
        x_range=language, 
        height=350, 
        title="Popularity", 
    ) 
    p2.vbar(x=language, top=popularity, width=0.5) 
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0
  
    # Third Chart - Line Plot 
    p3 = figure(height=350, sizing_mode="stretch_width") 
    p3.line( 
        [i for i in range(10)], 
        [random.randint(1, 50) for j in range(10)], 
        line_width=2, 
        color="olive", 
        alpha=0.5
    ) 
  
    script1, div1 = components(p1) 
    script2, div2 = components(p2) 
    script3, div3 = components(p3) 
  
    # Return all the charts to the HTML template 
    return render_template( 
        template_name_or_list='charts.html', 
        script=[script1, script2, script3], 
        div=[div1, div2, div3], 
    ) 

# @app.route('/bokeh')
# def bokeh():

#     # init a basic bar chart:
#     # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
#     fig = figure(width=600, height=600)
#     fig.vbar(
#         x=[1, 2, 3, 4],
#         width=0.5,
#         bottom=0,
#         top=[1.7, 2.2, 4.6, 3.9],
#         color='navy'
#     )

#     # grab the static resources
#     js_resources = INLINE.render_js()
#     css_resources = INLINE.render_css()

#     # render template
#     script, div = components(fig)
#     html = render_template(
#         'index.html',
#         plot_script=script,
#         plot_div=div,
#         js_resources=js_resources,
#         css_resources=css_resources,
#     )
#     return encode_utf8(html)

# Main Driver Function 
if __name__ == '__main__': 
    # Run the application on the local development server 
    app.run() 