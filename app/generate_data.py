import csv

from faker import Faker
from faker_vehicle import VehicleProvider
import random
from tqdm import tqdm


def _save_to_csv(file_path, data, columns=None):
    columns = columns or []

    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    COUNT_SAMPLES = 100
    BATCH_SIZE = 20

    fake = Faker()
    fake.add_provider(VehicleProvider)

    item_id = 234324
    customer_id = 324
    items = []
    customers = []

    for _ in tqdm(range(COUNT_SAMPLES)):
        item_id += 1

        item = {
            'id': item_id,
            'title': fake.vehicle_make_model(),
            'price': round(random.randint(5, 999999) + random.random(), 2)
        }
        customer_id += 1
        customer = fake.simple_profile()
        del customer['birthdate']
        customer['id'] = customer_id

        items.append(item)
        customers.append(customer)

    # generate orders
    orders = []
    order_relations = []
    order_id = 3434
    for _ in tqdm(range(COUNT_SAMPLES)):

        customer = random.choice(customers)
        order_id += 1
        orders.append({'id': order_id})

        for _ in range(random.randint(1, 5)):
            item = random.choice(items)

            order_relation = {
                'order_id': order_id,
                'item_id': item['id'],
                'customer_id': customer['id'],
                'quantity': random.randint(1, 99)
            }
            order_relations.append(order_relation)

    # generate views
    views = []
    for _ in tqdm(range(COUNT_SAMPLES)):
        customer = random.choice(customers)

        for _ in range(random.randint(1, 5)):
            item = random.choice(items)

            view = {
                'item_id': item['id'],
                'customer_id': customer['id'],
            }
            views.append(view)

    # save to csv
    items_file_path = '../data/items.csv'
    customers_file_path = '../data/customers.csv'
    orders_file_path = '../data/orders.csv'
    order_relations_file_path = '../data/order_relations.csv'
    views_file_path = '../data/views.csv'

    _save_to_csv(items_file_path, items, items[0].keys())
    _save_to_csv(customers_file_path, customers, customers[0].keys())
    _save_to_csv(orders_file_path, orders, orders[0].keys())
    _save_to_csv(order_relations_file_path, order_relations, order_relations[0].keys())
    _save_to_csv(views_file_path, views, views[0].keys())


if __name__ == '__main__':
    main()
