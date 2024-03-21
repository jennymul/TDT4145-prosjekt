def getTicketPrice(cursor, ticket_price_type):
    cursor.execute(
        "SELECT Pris FROM PrisType WHERE Type = ? LIMIT 1;", [ticket_price_type]
    )
    return cursor.fetchone()[0]


def getNextPrimaryKey(cursor, primary_key_name, table_name):
    cursor.execute(
        f"""
    SELECT MAX({primary_key_name}) FROM {table_name};
    """
    )
    primary_key = cursor.fetchone()
    if primary_key == None:
        return 1
    return primary_key[0] + 1


def printTable(column_names, rows):
    column_widths = []
    for index, name in enumerate(column_names):
        width = len(name)
        for row in rows:
            width = max(width, len(str(row[index])))
        column_widths.append(width)

    print("|", end="")
    for index, name in enumerate(column_names):
        print(" " + name.ljust(column_widths[index]) + " |", end="")
    print()

    print("|", end="")
    for width in column_widths:
        print("-" * (width + 2) + "|", end="")
    print()

    for row in rows:
        print("|", end="")
        for index, item in enumerate(row):
            print(" " + str(item).ljust(column_widths[index]) + " |", end="")
        print()
