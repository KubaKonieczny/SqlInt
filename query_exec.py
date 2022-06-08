import pandas as pd



class Operations(object):

    columns = []
    tables = []

    def query_exec(self, name, columns, tables, expressions, order, where):

        if name == "select":
            df = pd.read_csv("Tables/" + tables[0])
            if where is not None:
                # df = pd.read_csv("Tables/" + tables[0])
                #print(where[2])
                print(where[2])
                if where[1] == '=':
                    df = df[df[where[0]] == where[2][0]]
                elif where[1] == '>':
                    df = df[df[where[0]] > where[2][0]]
                elif where[1] == '<':
                    df = df[df[where[0]] < where[2][0]]

            if expressions is not None:
                print(expressions)
            elif columns == ['*']:
                pass
                #print(df.head())
            else:
                # df = pd.read_csv("Tables/" + tables[0])
                # print(columns)
                # print(df.columns)
                df = df[columns]

                # df.sort_values(order, in_place=True)
                #print(df.head())

            print(df)

        elif name == 'update':
            df = pd.read_csv("Tables/" + tables)
            print(expressions)
            if where is None:
                df.loc[:, columns] = expressions[0]
                print(df.head(5))
                df.to_csv("Tables/" + tables, index_col=False)

            if where is not None:
                # df = pd.read_csv("Tables/" + tables[0])
                #print(where[2])
                print(where[2])
                if where[1] == '=':
                    df.loc[df[where[0]] == where[2][0], columns] = expressions
                elif where[1] == '>':
                    df.loc[df[where[0]] > where[2][0], columns] = expressions
                elif where[1] == '<':
                    df.loc[df[where[0]] < where[2][0], columns] = expressions
                print(df.head(5))
                df.to_csv("Tables/" + tables, index_col=False)

        elif name == 'insert':
            df = pd.read_csv("Tables/" + tables)
            df.loc[len(df.index)] = expressions
            print(df)
            df.to_csv("Tables/" + tables, index_col=False)
        elif name == 'delete':
            df = pd.read_csv("Tables/" + tables)
            df.drop()








