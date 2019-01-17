
import happybase as hb

data = {"0":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"1":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"2":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"3":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"4":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"5":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"6":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"7":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"8":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"9":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"10":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"11":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"12":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"13":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"14":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"15":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"16":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"17":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"18":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"19":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"20":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"21":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"22":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"23":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"24":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"25":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"26":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"27":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"28":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"},"29":{"Iris-setosa":"0.00","Iris-versicolor":"0.50","Iris-virginica":"0.50"}}

table = 'iris_results_10'

connection = hb.Connection('localhost')
tables = connection.tables()
print(tables)

if table not in tables:
    print("Table {} was created!".format(table))
    connection.create_table(table, {'Iris-setosa': dict(), 'Iris-versicolor': dict(), 'Iris-virginica': dict(),})

res_table = connection.table(table)

#b = res_table.batch()

for key, value in data.items():
    res_table.put(key, {"Iris-setosa": "0.00", "Iris-versicolor": "0.50", "Iris-virginica": "0.50"})

#try:
#    for key, value in data.items():
#        b.put(key, value)
#        print(key, value)
#    b.send()
#    raise ValueError("Somethings went wrong!!!")
#except ValueError as e:
#    pass
#else:
#    b.send()
