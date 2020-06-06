print('Hello world!')
def createTable(num_cols):
    with open('output.txt','a') as out:
        out.write('\begin{table}[!h]')
        out.write('\begin/{tabular/}/{' +'c '*num_cols+ '/}')


createTable(3)
