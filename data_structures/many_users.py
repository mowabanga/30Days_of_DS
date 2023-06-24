users = {
    'gvnbl': {
        'first': 'gavin',
	'last': 'belson',
	'location': 'silicon valley'
    },
    'richie79': {
        'first': 'richard',
	'last': 'hendricks',
	'location': 'arizona'
    },
}

for i, j in users.items():
    print("\nUsername:", i)
    full_name = j['first'].title() + " " + j['last'].title()
    location = j['location'].title()
    print("Full name:", full_name)
    print("Location:", location)
