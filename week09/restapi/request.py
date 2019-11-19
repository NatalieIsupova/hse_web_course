import requests
from pprint import pprint

if __name__ == "__main__":
	j = requests.get('http://localhost:5000/cards').json()
	card = j.get('_items', [{}])[0]

	card_id = card.get('_id')
	card_cvv = card.get('cvv')
	card_etag = card.get('_etag')

	payload = {"cvv": card_cvv + 1}
	headers = {"If-Match": card_etag}
	p = requests.patch(f'http://localhost:5000/cards/{card_id}', data=payload, headers=headers).json()

	pprint(p)
