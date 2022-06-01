import pandas as pd



class Operations(object):

    columns = []
    tables = []

    def query_exec(self, name, columns, tables, expressions, order, where):

        if name == "select" and expressions is None:
            df = pd.read_csv("Tables/"+tables[0])
            print(columns)
            print(df.columns)
            df = df[columns]

            #df.sort_values(order, in_place=True)
            print(df.head())
        elif name == "select" and expressions is not None :
            print(expressions)

        elif name == 'update':
            df = pd.read_csv("Tables/" + tables)
            df.loc[:, columns] = expressions
        elif name == 'insert':
            df = pd.read_csv("Tables/" + tables)
            df.loc[len(df.index)] = [expressions]
        elif name == 'delete':
            df = pd.read_csv("Tables/" + tables)
            df.drop()







