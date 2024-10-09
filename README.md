# Library System

List of API's

#### Signup

POST - api/signup

- 1 - Librarian.
- 2 - Members.

```
{
	username: "saurabh",
	password: "password",
	user_type: 1,
	is_active: True
}
```

#### Login

POST - api/login/

```
{
	username: "saurabh",
	password: "password",
}
```

#### Librarian

POST - api/books

```
{
	title: "The Success",
	is_available: True
}
```

```
GET - api/books
{
	status: 200,
	books:[
		{
            id: 1,
			title: "The Success",
			is_available: True
		},
		{
            id: 2,
			title: "Imagination",
			is_available: True
		},
		{
            id: 3,
			title: "Goals",
			is_available: False
		}
	]
}
```

DELETE - api/books/{book_id}

PUT/PATCH - api/books/{book_id}
```
{
	title: "The Success",
	is_available: False
}
```

POST - api/members
```
{
	username: "saurabh",
	password: "password",
	user_type: 2,
	is_active: True
}
```

GET - api/members
```

```

PUT/PATCH - api/members/{member_id}
```

```

DELETE - api/members/{member_id}

GET - api/members/history
```
{
    status:200,
    members:[
        {
            id: 1,
            name: "saurabh",
            borrowed_books:[
                "The Success",
                "Goals"
            ],
            returned_books:[
                "Investment"
            ]
        },
        {
            id: 2,
            name: "shubham",
            borrowed_books:[
                "Investment",
            ],
            returned_books:[
                "Imagination"
            ]
        },
        {
            id: 3,
            name: "raj",
            borrowed_books:[
                "Imagination"
            ],
            returned_books:[
                "Goals"
            ]
        }
    ]
}
```
