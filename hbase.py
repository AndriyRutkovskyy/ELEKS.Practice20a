import happybase as hb

HOST = 'localhost'
PORT = 9090
TABLE_NAME = 't5675773'


def put_to_hbase(inp_data):
    connection = hb.Connection(HOST, PORT)

    tables = connection.tables()
    print("HBase has tables {0}".format(tables))

    if TABLE_NAME not in tables:
        print("Creating table {0}".format(TABLE_NAME))
        connection.create_table(TABLE_NAME, {'cf:': dict()})

    table = connection.table(TABLE_NAME)

    b = table.batch()

    for key, value in inp_data.items():
        try:
            b.put(key, value)
            print("Storing values with row key '{0}'".format(key))
        except ValueError as e:
            pass
        else:
            b.send()