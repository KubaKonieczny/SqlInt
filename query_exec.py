import pandas as pd



class Operations(object):

    columns = []
    tables = []

    def query_exec(self, name, columns, tables, expressions, order, where):

        if name == "select":
            if expressions is not None:
                print(expressions)
            elif columns == ['*']:
                df = pd.read_csv("Tables/" + tables[0])
                print(df.head())
            elif expressions is None and where is None and order is None:
                df = pd.read_csv("Tables/" + tables[0])
                print(columns)
                print(df.columns)
                df = df[columns]

                # df.sort_values(order, in_place=True)
                print(df.head())
            elif where is not None:
                df = pd.read_csv("Tables/" + tables[0])
                # print(where[0])
                # print(where[2][1])
                df = df[df[where[0]] == where[2][1]]
                print(df)


        elif name == 'update':
            df = pd.read_csv("Tables/" + tables)
            df.loc[:, columns] = expressions
        elif name == 'insert':
            df = pd.read_csv("Tables/" + tables)
            df.loc[len(df.index)] = [expressions]
        elif name == 'delete':
            df = pd.read_csv("Tables/" + tables)
            df.drop()







