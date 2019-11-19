from eve import Eve

settings = {'DOMAIN': {
	'cards': {
		"resource_methods": ['GET', 'POST'],
		"item_methods": ["GET", 'PATCH', 'DELETE'],
		"schema": {
			"number": {
				"type": "string"
			},
			"cvv": {
				"type": "integer"
			},
		},
		},
	'accounts': {}
	}
}

app = Eve(settings=settings)
app.run()