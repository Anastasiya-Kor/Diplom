# Импортируем необходимые библиотеки и модули
import requests
import configuration

def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)


def get_orders(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
                        params={"t": track})



