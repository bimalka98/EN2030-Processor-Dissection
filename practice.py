print('Hello world!')
def createTable(num_rows, num_cols):
    with open('output.tex','a') as out:


        #beginning of a table environment declaration

        out.write('\\begin{table}[!h]\n')
        out.write('\\begin{tabular}{' +'c '*num_cols+ '}\n')

        #table CONTENT
        for row in range(num_rows):
            out.write('&\t'*(num_cols-1) + '\\\\'+'\n')


        #end of a table environment
        out.write('\\end{tabular}\n')
        out.write('\\end{table}')

createTable(5,3)
