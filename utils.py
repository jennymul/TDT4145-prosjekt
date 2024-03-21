def getTicketPrice(cursor, ticket_price_type):
    cursor.execute("SELECT Pris FROM PrisType WHERE Type = ? LIMIT 1;", [ticket_price_type])
    return cursor.fetchone()[0]

def getNextPrimaryKey(cursor, primary_key_name, table_name):
    cursor.execute(f"""
    SELECT MAX({primary_key_name}) FROM {table_name};
    """)
    primary_key = cursor.fetchone()
    if primary_key == None:
        return 0
    return primary_key[0] + 1

def printTable(column_names, rows):
    column_widths = [len(column) for column in column_names]
    for row in rows:
        for i, item in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(item)))

    row_format = '| ' + ' | '.join(['{:<%d}' % width for width in column_widths]) + ' |'

    print(row_format.format(*column_names))

    print('|', end='')
    for column_width in column_widths:
        print('-' * (column_width + 2), end='|')
    print()

    for row in rows:
        print(row_format.format(*[str(item) for item in row]))

