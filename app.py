import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from flask import Flask, render_template, request

app = Flask(__name__,template_folder="templates")

# Load model
model = pickle.load(open('arima_model.pkl', 'rb')) 

@app.route('/')
def home(): # default home screen
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        # Get the selected month from the form
        selected_month = request.form.get('month')

        month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        }
        # Create a date range for 2022
        start_date = pd.to_datetime('2022-01-01')
        date_range_2022 = pd.date_range(start=start_date, periods=12, freq='M')

        # Make predictions for each month of 2022
        predictions = model.forecast(steps=12)
        total_predictions = sum(predictions)

        # Get the predicted receipt count for the selected month
        selected_month_index = int(selected_month) - 1
        selected_month_prediction = round(predictions[selected_month_index], 2)

        # Create a plot of the predictions
        plt.figure(figsize=(12, 6))
        plt.plot(date_range_2022, predictions, label='Predicted Data', marker='o')
        plt.title('Monthly Receipt Counts Predictions for 2022')
        plt.xlabel('Month')
        plt.ylabel('Receipt Counts')
        plt.legend()
        plt.grid(True)

        # Set x-axis ticks to display each month individually
        plt.xticks(date_range_2022, [month.strftime('%B') for month in date_range_2022], rotation=30)

        # Save the plot as an image
        plt.savefig('static/prediction_plot.png')
        plt.close()

        # Render the plot and selected month prediction on the HTML template
        return render_template('output.html', selected_month=month_dict[int(selected_month)], \
                                              selected_month_prediction="{:,}".format(int(selected_month_prediction)),\
                                              total_predictions = "{:,}".format(int(total_predictions)))

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
