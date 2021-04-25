from os import listdir
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

routes_list = [route.split('.')[0]
               for route in listdir(BASE_DIR)
               if '.py' in route and route != __file__.split('/')[-1]]

def web_routes(route):
    routes =[]
    for route_name in routes_list:
        routes_path = 'server.routes.'+route_name
        api_routes = __import__(routes_path, fromlist=[None])
        routes.extend(api_routes.routes(route))
    return routes
