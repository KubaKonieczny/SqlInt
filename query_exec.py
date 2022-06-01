import pandas as pd



class Operations(object):

    columns = []
    tables = []

    def query_exec(self, name, columns, tables, expressions, order, where):

        if name == "select" and expressions == None:
            df = pd.read_csv("Tables/"+tables)
            df = df[columns]
            #df.sort_values(order, in_place=True)
            print(df.head())
        elif name == "select" and expressions != None:
            print(expressions)







