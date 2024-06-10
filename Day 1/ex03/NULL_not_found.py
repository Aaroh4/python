def NULL_not_found(object: any) -> int:
	if (not object and object is None):
		print("Nothing:", object, type(object))
		return (0)
	elif (object != object and type(object) == float):
		print("Cheese", object, type(object))
		return (0)
	elif (not object and type(object) == int):
		print("Zero:", object, type(object))
		return (0)
	elif (not object and type(object) == str):
		print("Empty:", object, type(object))
		return (0)
	elif (not object and type(object) == bool):
		print("Fake:", object, type(object))
		return (0)
	else:
		print("Type not Found")
		return (1)
