from neo4j import GraphDatabase


def create_constraints(session):
    session.run(f'CREATE CONSTRAINT ON (item:Item) ASSERT item.id IS UNIQUE')
    session.run(f'CREATE CONSTRAINT ON (customer:Customer) ASSERT customer.id IS UNIQUE')
    session.run(f'CREATE CONSTRAINT ON (order:Order) ASSERT order.id IS UNIQUE')


def insert_items(session):
    session.run(f'''
        USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS FROM "file:///items.csv" AS row
        CREATE (:Item {{id: row.id, name: row.title, price: row.price}})
    ''')


def insert_customers(session):
    session.run(f'''
        USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS FROM "file:///customers.csv" AS row
        CREATE (:Customer {{id: row.id, username: row.username, name: row.name, mail: row.mail}})
    ''')


def insert_orders(session):
    session.run(f'''
       USING PERIODIC COMMIT
       LOAD CSV WITH HEADERS FROM "file:///orders.csv" AS row
       CREATE (:Order {{id: row.id}})
    ''')

    session.run(f'''
        USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS FROM "file:///order_relations.csv" AS row
        MATCH (order:Order {{id: row.order_id}})
        MATCH (customer:Customer {{id: row.customer_id}})
        MATCH (item:Item {{id: row.item_id}})
        CREATE (item)-[:BELONGS_TO {{quantity: row.quantity}}]->(order)
        MERGE (order)-[:MADE_BY]->(customer)
    ''')


def insert_views(session):
    session.run(f'''
        USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS FROM "file:///views.csv" AS row
        MATCH (customer:Customer {{id: row.customer_id}})
        MATCH (item:Item {{id: row.item_id}})
        CREATE (item)-[:VIEWED_BY]->(customer)
    ''')


def main():
    uri = "bolt://neo4j:7687"
    # uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(
        uri,
        auth=("neo4j", "password")
    )

    with driver.session() as session:
        create_constraints(session)
        insert_items(session)
        insert_customers(session)
        insert_orders(session)
        insert_views(session)


if __name__ == '__main__':
    main()
