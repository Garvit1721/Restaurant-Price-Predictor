from flask import Flask, render_template, request
import pickle
import pandas as pd

file_pipe = r"D:\zomato_price_prediction\pipe.pkl"
file_path = r"D:\zomato_price_prediction\data.pkl"
file_path_ = r"D:\zomato_price_prediction\top_10.pkl"
file_path_1 = r"D:\zomato_price_prediction\top_5_casual.pkl"
file_path_2 = r"D:\zomato_price_prediction\top_5_cafe.pkl"
file_path_3 = r"D:\zomato_price_prediction\top_5_bakery.pkl"
file_path_4 = r"D:\zomato_price_prediction\top_5_quick_bites.pkl"
file_path_5 = r"D:\zomato_price_prediction\top_5_dessert_palor.pkl"
file_path_6 = r"D:\zomato_price_prediction\between_100_1000_top_5.pkl"
file_path_7 = r"D:\zomato_price_prediction\between_1000_2000_top_5.pkl"
file_path_8 = r"D:\zomato_price_prediction\between_2000_3000_top_5.pkl"
file_path_9 = r"D:\zomato_price_prediction\between_3000_4000_top_5.pkl"
file_path_10 = r"D:\zomato_price_prediction\between_4000_5000_top_5.pkl"
file_path_11 = r"D:\zomato_price_prediction\between_5000_6000_top_5.pkl"
file_path_12 = r"D:\zomato_price_prediction\north_indian_rest_top_5.pkl"
file_path_13 = r"D:\zomato_price_prediction\chinese_rest_top_5.pkl"
file_path_14 = r"D:\zomato_price_prediction\continental_rest_top_5.pkl"

data = pickle.load(open(file_path, 'rb'))
top_10 = pickle.load(open(file_path_, 'rb'))
top_5_casual = pickle.load(open(file_path_1, 'rb'))
top_5_cafe = pickle.load(open(file_path_2, 'rb'))
top_5_bakery = pickle.load(open(file_path_3, 'rb'))
top_5_quick_bites = pickle.load(open(file_path_4, 'rb'))
top_5_dessert_palor = pickle.load(open(file_path_5, 'rb'))
between_100_1000_top_5 = pickle.load(open(file_path_6, 'rb'))
between_1000_2000_top_5 = pickle.load(open(file_path_7, 'rb'))
between_2000_3000_top_5 = pickle.load(open(file_path_8, 'rb'))
between_3000_4000_top_5 = pickle.load(open(file_path_9, 'rb'))
between_4000_5000_top_5 = pickle.load(open(file_path_10, 'rb'))
between_5000_6000_top_5 = pickle.load(open(file_path_11, 'rb'))
north_indian_rest_top_5 = pickle.load(open(file_path_12, 'rb'))
chinese_rest_top_5 = pickle.load(open(file_path_13, 'rb'))
continental_rest_top_5 = pickle.load(open(file_path_14, 'rb'))
pipe = pickle.load(open(file_pipe, 'rb'))


def graph_data(request_data):
    graph = {
        'x': [],
        'y': [],
        'x_annt': None,
        'x_label': None,
        'y_label': None,
        'title': None
    }
    if request_data == "Top 5 Casual Dining Restaurants":
        graph['x'] = list(top_5_casual['name'])
        graph['y'] = list(top_5_casual['rate'])
        graph['x_label'] = "Casual Dining Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Casual Dining Restaurants"

    elif request_data == "Top 5 Cafes":
        graph['x'] = list(top_5_cafe['name'])
        graph['y'] = list(top_5_cafe['rate'])
        graph['x_label'] = "Cafe Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Cafes"

    elif request_data == "Top 5 Bakeries":
        graph['x'] = list(top_5_bakery['name'])
        graph['y'] = list(top_5_bakery['rate'])
        graph['x_label'] = "Bakeries Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Bakeries"

    elif request_data == "Top 5 Quick Bites Restaurants":
        graph['x'] = list(top_5_quick_bites['name'])
        graph['y'] = list(top_5_quick_bites['rate'])
        graph['x_label'] = "Quick Bites Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Quick Bites Restaurants"

    elif request_data == "Top 5 Dessert Parlor":
        graph['x'] = list(top_5_dessert_palor['name'])
        graph['y'] = list(top_5_dessert_palor['rate'])
        graph['x_label'] = "Dessert Parlor Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Dessert Parlor Restaurants"

    elif request_data == "Top 5 Restaurants : range - (100-1000)":
        graph['x'] = list(between_100_1000_top_5['name'])
        graph['y'] = list(between_100_1000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : range - (1000-2000)":
        graph['x'] = list(between_1000_2000_top_5['name'])
        graph['y'] = list(between_1000_2000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : range - (2000-3000)":
        graph['x'] = list(between_2000_3000_top_5['name'])
        graph['y'] = list(between_2000_3000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : range - (3000-4000)":
        graph['x'] = list(between_3000_4000_top_5['name'])
        graph['y'] = list(between_3000_4000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : range - (4000-5000)":
        graph['x'] = list(between_4000_5000_top_5['name'])
        graph['y'] = list(between_4000_5000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : range - (5000-6000)":
        graph['x'] = list(between_5000_6000_top_5['name'])
        graph['y'] = list(between_5000_6000_top_5['rate'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Most famous restaurants chains in Bangaluru":
        chains = data['name'].value_counts()[:10]
        graph['y'] = list(chains)
        graph['x'] = list(chains.index)
        graph['y_label'] = "Number of outlets"
        graph['x_label'] = "Restaurant Name"
        graph['title'] = "Most famous restaurants chains in Bangaluru"

    elif request_data == "Types of Restaurant":
        chains = data['listed_in(type)'].value_counts()[:10]
        graph['y'] = list(chains)
        graph['x'] = list(chains.index)
        graph['x_label'] = "Number of outlets"
        graph['title'] = "Types of Restaurant"
        graph['y_label'] = "Type of Restaurant"

    elif request_data == "Top 5 Restaurants : North Indian":
        graph['x'] = list(north_indian_rest_top_5['name'])
        graph['y'] = list(north_indian_rest_top_5['rate'])
        graph['x_annt'] = list(north_indian_rest_top_5['votes'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : Chinese":
        graph['x'] = list(chinese_rest_top_5['name'])
        graph['y'] = list(chinese_rest_top_5['rate'])
        graph['x_annt'] = list(chinese_rest_top_5['votes'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    elif request_data == "Top 5 Restaurants : Continental":
        graph['x'] = list(continental_rest_top_5['name'])
        graph['y'] = list(continental_rest_top_5['rate'])
        graph['x_annt'] = list(continental_rest_top_5['votes'])
        graph['x_label'] = "Restaurants Name"
        graph['y_label'] = "Ratings"
        graph['title'] = "Top 5 Restaurants"

    return graph


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
    if request.method == 'POST':
        graph_needed = request.form.get('graph_needed')
        graph_data_ = graph_data(graph_needed)
    else :
        graph_data_ = "Top 5 Casual Dining Restaurants"
    return render_template('index.html', data=graph_data_,zip=zip)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        online_order = request.form.get('Online Order')
        book_table = request.form.get('Table Book')
        rate = request.form.get('Ratings')
        votes = request.form.get('Votes')
        location = request.form.get('Location')
        rest_type = request.form.get('Restaurant Type')
        cuisines = request.form.get('Cuisines')

        data = pd.DataFrame({
            'online_order': [online_order],
            'book_table': [book_table],
            'rate': [rate],
            'votes': [votes],
            'location': [location],
            'rest_type': [rest_type],
            'cuisines': [cuisines]
        })

        pred_price = pipe.predict(data)
        return render_template('predict.html', result=pred_price)

    return render_template('predict.html', result=None)


if __name__ == "__main__":
    app.run(debug=True)





