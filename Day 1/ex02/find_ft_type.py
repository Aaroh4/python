def all_thing_is_obj(object: any) -> int:
	if (type(object) == list):
		print("List :", type(object))
		return (42)
	elif (type(object) == tuple):
		print("Tuple :", type(object))
		return (42)
	elif (type(object) == set):
		print("set :", type(object))
		return (42)
	elif (type(object) == dict):
		print("Dict :", type(object))
		return (42)
	elif (type(object) == str):
		print(object, "is in the kitchen :", type(object))
		return (42)
	print("Type not found")
	return (42)
