from server.routes.users import user_routes

def web_routes(route):
    return [
    *user_routes(route)
    ]
    