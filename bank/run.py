from flask import Flask, render_template
import pandas as pd
import plotly
import json
import plotly.express as px

app = Flask(__name__)

data = pd.read_csv("bank.csv") 


@app.route("/")
def index():

    plot = px.pie(data, names='education', title='EDUCATION')
    plotly_plot = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

    plot1 = px.pie(data, names ='job', title ='JOB')
    plotly_plot1 = json.dumps(plot1, cls=plotly.utils.PlotlyJSONEncoder)
    
    plot2 = px.histogram(data, x="marital", title = 'MARITAL') 
    plotly_plot2 = json.dumps(plot2, cls=plotly.utils.PlotlyJSONEncoder)

    plot3 = px.histogram(data, x="housing", title = 'HOUSING') 
    plotly_plot3 = json.dumps(plot3, cls=plotly.utils.PlotlyJSONEncoder)

    plot4 = px.histogram(data, x="loan", title = 'LOAN') 
    plotly_plot4 = json.dumps(plot4, cls=plotly.utils.PlotlyJSONEncoder)

    plot5 = px.imshow(data)
    plotly_plot5 = json.dumps(plot5, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("home.html",plotly_plot = plotly_plot, plotly_plot1 = plotly_plot1, plotly_plot2 = plotly_plot2, plotly_plot3 = plotly_plot3, plotly_plot4 = plotly_plot4, plotly_plot5 = plotly_plot5)
 


if __name__ == "__main__":
    app.directory='./'
    app.run(host='127.0.0.1', port=5000)
