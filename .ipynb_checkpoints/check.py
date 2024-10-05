import pickle
graph = {}
file_path = r"D:\zomato_price_prediction\data.pkl"
file_path_ = r"D:\zomato_price_prediction\top_10.pkl"
file_path_14 = r"D:\zomato_price_prediction\continental_rest_top_5.pkl"

continental_rest_top_5 = pickle.load(open(file_path_14, 'rb'))
top_10 = pickle.load(open(file_path_, 'rb'))
data = pickle.load(open(file_path, 'rb'))
graph['x'] = list(top_10.values)
print(list(continental_rest_top_5['name']))
print(graph['x'])