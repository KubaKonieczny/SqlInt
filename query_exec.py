import pandas as pd
import itertools

class Operations(object):

    columns = []
    tables = []

    def query_exec(self, name, columns, tables, expressions, order, where):

        if name == "select":
            df = pd.read_csv("Tables/" + tables[0])
            if where is not None:
                # df = pd.read_csv("Tables/" + tables[0])
                where = [item for sublist in [[item] if type(item) is not list else item for item in where] for item in sublist]
                print(where)
                print(where[2])

                i = 0
                b = ''

                while i < len(where):
                    if where[i + 1] == '=':
                        if b == 'OR':
                            df2 = df[df[where[i]] == where[i + 2]]
                            df = pd.concat([df2, df]).drop_duplicates()
                        else:
                            df = df[df[where[i]] == where[i + 2]]
                    elif where[i + 1] == '>':
                        if b == 'OR':
                            df2 = df[df[where[i]] > where[i + 2]]
                            df = pd.concat([df2, df]).drop_duplicates()
                        else:
                            df = df[df[where[i]] > where[i + 2]]
                    elif where[i + 1] == '<':
                        if b == 'OR':
                            df2 = df[df[where[i]] < where[i + 2]]
                            df = pd.concat([df2, df]).drop_duplicates()
                        else:
                            df = df[df[where[i]] < where[i + 2]]

                    if i + 3 < len(where):
                        b = where[i + 3]

                    i = i + 4

            if expressions is not None:
                print(expressions)
            elif columns == ['*']:
                pass
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
                    df.loc[df[where[0]] == where[2], columns] = expressions
                elif where[1] == '>':
                    df.loc[df[where[0]] > where[2], columns] = expressions
                elif where[1] == '<':
                    df.loc[df[where[0]] < where[2], columns] = expressions
                print(df.head(5))
                df.to_csv("Tables/" + tables, index=False)

        elif name == 'insert':
            if columns is None:
                df = pd.read_csv("Tables/" + tables)
                print(list(expressions))
                df.loc[len(df.index)] = expressions
                print(df)
                df.to_csv("Tables/" + tables, index=False)
            else:
                df = pd.read_csv("Tables/" + tables)
                print(list(expressions))
                df.loc[len(df.index), columns] = expressions
                print(df)
                df.to_csv("Tables/" + tables, index=False)
        elif name == 'delete':

            if where is None:
                df = pd.read_csv("Tables/" + tables[0])
                df.drop(df.index, inplace=True)
                df.to_csv("Tables/" + tables[0], index=False)

            else:
                df = pd.read_csv("Tables/" + tables[0])
                if where[1] == '=':
                    df.drop(df[df[where[0]] == where[2]].index, inplace=True)
                elif where[1] == '>':
                    df.drop(df[df[where[0]] > where[2]].index, inplace=True)
                elif where[1] == '<':
                    df.drop(df[df[where[0]] < where[2]].index, inplace=True)
                print(df.head(5))
                df.to_csv("Tables/" + tables[0], index=False)

    # def flatten(self, table):
    #     rt = []
    #     for i in table:
    #         if isinstance(i, list):
    #             rt.extend(flatten(i))
    #         else:
    #             rt.append(i)
    #     return rt




