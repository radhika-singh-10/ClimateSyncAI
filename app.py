from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from flask import Response
import numpy as np 
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
import pickle
app = Flask(__name__)

# Load historical time series data for each city
def get_cities():
    cities = ['Abidjan', 'Addis Abeba', 'Ahmadabad', 'Aleppo', 'Alexandria',
       'Ankara', 'Baghdad', 'Bangalore', 'Bangkok', 'Belo Horizonte',
       'Berlin', 'Bogotá', 'Bombay', 'Brasília', 'Cairo', 'Calcutta',
       'Cali', 'Cape Town', 'Casablanca', 'Changchun', 'Chengdu',
       'Chicago', 'Chongqing', 'Dakar', 'Dalian', 'Dar Es Salaam',
       'Delhi', 'Dhaka', 'Durban', 'Faisalabad', 'Fortaleza', 'Gizeh',
       'Guangzhou', 'Harare', 'Harbin', 'Ho Chi Minh City', 'Hyderabad',
       'Ibadan', 'Istanbul', 'Izmir', 'Jaipur', 'Jakarta', 'Jiddah',
       'Jinan', 'Kabul', 'Kano', 'Kanpur', 'Karachi', 'Kiev', 'Kinshasa',
       'Lagos', 'Lahore', 'Lakhnau', 'Lima', 'London', 'Los Angeles',
       'Luanda', 'Madras', 'Madrid', 'Manila', 'Mashhad', 'Melbourne',
       'Mexico', 'Mogadishu', 'Montreal', 'Moscow', 'Nagoya', 'Nagpur',
       'Nairobi', 'Nanjing', 'New Delhi', 'New York', 'Paris', 'Peking',
       'Pune', 'Rangoon', 'Rio De Janeiro', 'Riyadh', 'Rome', 'São Paulo',
       'Saint Petersburg', 'Salvador', 'Santiago', 'Santo Domingo',
       'Seoul', 'Shanghai', 'Shenyang', 'Singapore', 'Surabaya', 'Surat',
       'Sydney', 'Taipei', 'Taiyuan', 'Tangshan', 'Tianjin', 'Tokyo',
       'Toronto', 'Umm Durman', 'Wuhan', 'Xian']
    return cities

def get_past_year():
    past_years = list(range(1850, 2014))
    return past_years

def get_future_year():
    future_years = list(range(2014, int(datetime.date.today().year+1)))
    return future_years



def load_model_acc_to_cities(city):
    city1=['Lima', 'London', 'Los Angeles', 'Luanda', 
    'Madras', 'Madrid', 'Manila', 'Mashhad', 'Melbourne', 'Mexico', 'Mogadishu']
    city2=['Bangkok' ,'Belo', 'Horizonte', 'Bogotá', 'Bombay', 'Brasília', 'Cairo', 'Calcutta', 'Cali']
    city3=['Rome', 'Salvador', 'Santo Domingo', 'Seoul', 'Shanghai']
    city4=['Berlin', 'Cape Town', 'Casablanca', 'Changchun', 'Chengdu', 'Chicago', 'Chongqing', 'Dalian']
    city5=['Harbin', 'Istanbul', 'Izmir', 'Jinan', 'Kabul', 'Kiev']
    city6=['Montreal', 'Moscow', 'Nagoya', 'Nairobi', 'Nanjing', 'New York', 'Paris', 'Peking']
    city7=['Abidjan', 'Addis Abeba', 'Ahmadabad', 'Aleppo', 'Alexandria', 'Ankara', 'Baghdad', 'Bangalore']
    city8=['Dakar', 'Dar Es Salaam', 'Delhi', 'Dhaka', 'Durban', 'Faisalabad', 'Fortaleza', 'Gizeh', 
    'Guangzhou', 'Harare']
    city9=[ 'São Paulo', 'Taiyuan', 'Tangshan', 'Tianjin', 'Tokyo', 'Toronto', 'Wuhan', 'Xian']
    city10=['Nagpur', 'New Delhi', 'Pune', 'Rangoon', 'Rio De Janeiro', 'Riyadh', 'Saint Petersburg', 
    'Santiago']
    city11=['Kano', 'Kanpur', 'Karachi', 'Kinshasa', 'Lagos', 'Lahore',  'Lakhnau']
    city12=['Ho Chi Minh City', 'Hyderabad', 'Ibadan', 'Jaipur', 'Jakarta', 'Jiddah']
    city13=['Shenyang', 'Singapore', 'Surabaya', 'Surat', 'Sydney', 'Taipei', 'Umm Durman']
    file_path=""
    num=0
    if city1.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_1.pkl"
        num=1
    elif city2.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_2.pkl"
        num=2
    elif city3.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_3.pkl"
        num=3
    elif city4.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_4.pkl"
        num=4
    elif city5.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_5.pkl"
        num=5
    elif city6.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_6.pkl"
        num=6
    elif city7.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_7.pkl"
        num=7
    elif city8.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_8.pkl"
        num=8
    elif city9.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_9.pkl"
        num=9
    elif city10.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_10.pkl"
        num=10
    elif city11.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_11.pkl"
        num=11
    elif city12.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_12.pkl"
        num=12
    elif city13.__contains__(city):
        file_path= "sarimax_models/sarimax_model_group_13.pkl"
        num=13

    print(file_path)
    with open(file_path, "rb") as pickle_file:
        file_path= pickle.load(pickle_file)
    
    return file_path,num


def load_plot(df):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    print(df)
    xs = 0
    ys = 1
    axis.plot(xs, ys)
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

    
@app.route('/', methods=['GET', 'POST'])
def index():
    past_cities = future_cities =  get_cities()
    past_years = get_past_year()
    future_years = get_future_year()
    if request.method == 'POST':
        selected_past_city = request.form.get('past_city')
        selected_future_city = request.form.get('future_city')
        selected_future_year = request.form.get('future_year')
        selected_past_year = request.form.get('past_year')
        return render_template('index.html', 
        past_cities = past_cities, selected_past_city=selected_past_city,
        future_cities=future_cities,  selected_future_city = selected_future_city,
        past_years=past_years, selected_past_year=selected_past_year, 
        future_years=future_years, selected_future_year=selected_future_year,
        html_code=None)
    
    return render_template('index.html', 
        past_cities = past_cities, selected_past_city=None,
        future_cities=future_cities,  selected_future_city = None,
        past_years=past_years, selected_past_year=None, 
        future_years=future_years, selected_future_year=None,html_code=None)

# Create API endpoint to handle model requests
@app.route('/predict_past_temperature', methods=['POST'])
def predict_past_temperature():
    city = request.json['past_city']
    year = request.json['past_year']
    past_year = 2024 
    model,num=load_model_acc_to_cities(city) 
    print(model,num)
    past_year = int(year) 
    past_dates = pd.date_range(start=str(past_year), end=str(past_year + 1), freq='M')
    forecast_periods = len(past_dates)
    forecast = model.fit().get_forecast(steps=forecast_periods)
    forecast_mean = forecast.predicted_mean
    forecast_ci = forecast.conf_int()
    forecast_mean_series = pd.Series(forecast_mean, index=past_dates)
    forecast_mean_series
    res = {}
    for i in range(0,len(forecast_mean_series)):
        res[past_dates[i].date().strftime('%Y-%m-%d')]=forecast_mean_series[i]

    # Return response as JSON
    return res

@app.route('/predict_future_temperature', methods=['POST'])
def predict_future_temperature():
    city = request.json['future_city']
    year = request.json['future_year']
    model,num=load_model_acc_to_cities(city) 
    print(model,num)
    future_year = int(year) 
    print(year)
    future_dates = pd.date_range(start=str(future_year), end=str(future_year + 1), freq='M')
    forecast_periods = len(future_dates)
    forecast = model.fit().get_forecast(steps=forecast_periods)
    forecast_mean = forecast.predicted_mean
    forecast_ci = forecast.conf_int()
    forecast_mean_series = pd.Series(forecast_mean, index=future_dates)
    res = {}
    for i in range(0,len(forecast_mean_series)):
        res[future_dates[i].date().strftime('%Y-%m-%d')]=forecast_mean_series[i]
    
    
    # Return response as JSON
    return res
@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory('static', filename)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
