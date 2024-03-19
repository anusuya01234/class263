from flask import Flask, render_template, request # importing the flask library to run our web app
import requests
#nitializing Flask using the Flask function.
app = Flask(__name__) # __name__ is to define how you want to run your program. Such as presently we want to run our web application using flask.
#@app. route decorator tells the computer to execute the program in an internet browser of the computer
@app.route("/")
def visitors():

    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable. This method displays the HTML page along with data that we want to display on the web.
    return render_template("index.html", count=visitors_count) #Here is the attribute name which we have mentioned in the p tag of the HTML file.
#get weather data using weather API.
@app.route('/', methods=['POST'])
def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    latitude = request.form['latitude'] #requesting text from the HTML page.
    longitude = request.form['longitude']

    api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude #appending coordinates(which are entered by the user and stored in a text variable) to the API URL.

    response = requests.get(api_url) #send a request at the api_url using request.get() and store the response in response variable.
    weather_data = response.json() #convert the string response to JSON and store it in weather_data
    print(weather_data) #This will print the weather stats.
    return render_template("index.html", weather=weather_data, count=visitors_count) #return weather_data as weather and visitors count data at HTML page. weather is the attribute name which we have mentioned in the table tag of the HTML file

if __name__ == "__main__":
    app.run()
