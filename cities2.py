# Script: Creates a Flask site with a form to input the type of analysis and returns the results
#           of that analysis. It is only partially successful.
#         The analysis uses geopandas to analyze the size of the shapefile's attribute table, create a list of the
#           states in the shapefile, or to list the times each state appears in the shapefile.
#         The attribute table size is the only analysis that returns a result in this script. We think that is because
#           it returns a tuple which is easily passed to the html file, where the others return more complex data
#           types that FLask is unable to pass to html and thus creates an error.
# Requires: cities2form.html and cities2returns.html

# Import necessary libraries
from flask import Flask
from flask import request
from flask import render_template
import geopandas
from numpy import ndarray

# Creates Flask website
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("cities2form.html")  # This should be the name of your HTML file


@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['Analysis']
    cities = r'C:\filepath\USA_Major_Cities.shp'
    df_cities = geopandas.read_file(cities)
    if text1 == "Size":
        size = df_cities.shape
        return render_template("cities2returns.html", N="Array size", C=size)
    elif text1 == "State List": # This function didn't return anything to html.
        state_list_raw = (df_cities.ST.unique())
        state_list = state_list_raw.sort()
        ST_list = ndarray.tolist(state_list)
        return render_template("cities2returns.html", N="State List", C=ST_list)
    elif text1 == "State Count": # This function didn't return anything to html.
        state_counts = df_cities.ST.value_counts()
        return render_template("cities2returns.html", N="State Count", C=state_counts)

if __name__ == '__main__':
    app.run()