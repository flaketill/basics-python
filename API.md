# REST API (RESTful)
## Best practices
### Resources

* The **/posts** resource contains information about posts
* The **/comments** resource contains comments related to posts.

> This Rest API comes with a set of resources:

* /posts	100 posts
* /comments	500 comments

### Routes

> All HTTP methods are supported. You can use http or https for your requests.

Returns a list of all available publications:
* GET	/posts (Returns a list of all available publications)

Returns data of post id 1:
* GET	/posts/1

Returns a list of all available publications:
* GET	/comments (Returns a list of all available comments)

Returns data of comment with id 1:
* GET	/comments/1

Create an post:

* POST	/posts

Update an post with id 1:

* PUT	/posts/1
* PATCH	/posts/1

Remove an post with id 1:
* DELETE	/posts/1

### Scenario: HTTP methods are supported

#### Posts

**[GET] Retrieve all posts**

**Request:**

> [GET] http://armandoibarra.com/api/v1/posts
> Accept: application/json

**Response:**

> Status code: 200 (OK)
> Content-type: application/json

```sh
[
    {
        "id": 1,
        "title": "Post 1"
    },
    {
        "id": 2,
        "title": "Post 2"
    },
    {
        "id": 3,
        "title": "Post 3"
    }
]
```

**[POST] Create an post**

**Request:**

> [POST] http://armandoibarra.com/api/v1/posts
> Accept: application/json

[Body] 

```sh
{ 
	"id": 4, 
	"title": "Post 4"
}
```

**Response:**

> Status code: 201 (Created)
> Content-type: application/json

```sh
{ 
	"id": 4, 
	"title": "Post 4"
}
```


**[PUT] Update an post**

**Request:**

> [PUT] http://armandoibarra.com/api/v1/posts/4
> Accept: application/json

[Body]

```sh
{
    "id": 4,
    "title": "This is a post with id 4"
}
```

**Response:**

> Status code: 201 (Created)
> Content-type: application/json

```sh
{ 
	"id": 4, 
	"title": "This is a post with id 4"
}
```

** [DELETE] Remove an posts **

**Request:**

> [DELETE] http://armandoibarra.com/api/v1/posts/4
> Accept: application/json

**Response:**

> Status code: 200 (OK)
> Content-type: application/json

```sh
{}
```


#### Comments


**[GET] Retrieve all comments**

**Request:**

> [GET] http://armandoibarra.com/api/v1/comments
> Accept: application/json

**Response:**

> Status code: 200 (OK)
> Content-type: application/json

```sh
[
    {
        "id": 1,
        "body": "comment 1"
    },
    {
        "id": 2,
        "body": "comment 2"
    },
    {
        "id": 3,
        "body": "comment 3"
    }
]
```


**[POST] Create an comment**

**Request:**

> [POST] http://armandoibarra.com/api/v1/comments
> Accept: application/json

[Body] 

```sh
{ 
	"id": 4, 
	"body": "comment 4"
}
```

**Response:**
> Status code: 201 (Created)
> Content-type: application/json

```sh
{ 
	"id": 4, 
	"body": "comment 4"
}
```

**[PUT] Update an comment**

**Request:**

> [PUT] http://armandoibarra.com/api/v1/comments/4
> Accept: application/json

[Body]

```sh
{
    "id": 4,
    "body": "This is a comment with id 4"
}
```

**Response:**

> Status code: 201 (Created)
> Content-type: application/json

```sh
{ 
	"id": 4, 
	"body": "This is a comment with id 4"
}
```

** [DELETE] Remove an comments **

**Request:**

> [DELETE] http://armandoibarra.com/api/v1/comments/4
> Accept: application/json

**Response:**

> Status code: 200 (OK)
> Content-type: application/json

```sh
{}
```