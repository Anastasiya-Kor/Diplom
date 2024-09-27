import sender_stand_request
import data

def get_orders_track():
    orders_response = sender_stand_request.post_new_orders(data.orders_body)
    orders_track = orders_response.json()["track"]
    return orders_track


# Тест
def test_assert():
    orders_track = get_orders_track()
    print("Номер заказа ", orders_track)
    orders_response2= sender_stand_request.get_orders(orders_track)

    # Проверяется, что код ответа равен 200
    assert orders_response2.status_code==200
    orders_params = orders_response2.json()
    print("Параметры заказа:", orders_params)


