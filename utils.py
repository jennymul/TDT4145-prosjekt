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
