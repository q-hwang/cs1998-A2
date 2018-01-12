# Kanban Board

This project is an API for a [`Kanban Board`](https://leankit.com/learn/kanban/kanban-board/) 
Original assignment: https://github.com/Cornell-PoBE/A2

## Learning Objectives

* `Python` as a language and `Flask` as a framework
* [`JSON`](http://www.json.org/) as a means of sending and receiving data
* `HTTP` requests / responses
* `MySQL` system configuration and usage
* `SQL-esque` data-modeling
* [`ORM`](http://flask-sqlalchemy.pocoo.org/2.1/) usage and data-modeling
* `SQL` querying
* Object serialization
* Writing an `API` to fit a specification given by front-end

## Table of Contents

* [System Configuration](#system-configuration)
* [Functionality](#functionality)
* [Testing](#testing)
* [Reference](#reference)

## System Configuration

Install requirements.txt 
Install  `MySQL` and create a database with newuser acount
Setup environment variables manually or use [`autoenv`](https://github.com/kennethreitz/autoenv). In my project, I have setup the `.env` as:

export APP_SETTINGS=config.DevelopmentConfig
export DB_USERNAME=newuser
export DB_PASSWORD=a
export DB_HOST=localhost
export DB_NAME=pobe_a2_db

They should be changed accordingly.

## Functionality

#### Create a Board
*Request:* `POST /kanban/boards?title={board_title}`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "board": {
      "board_elements": [],
      "created_at": "2017-05-15T22:43:32+00:00",
      "id": 1,
      "title": "My Awesome Board",
      "updated_at": "2017-05-15T22:43:32+00:00"
    }
  }
}
````

#### Delete a Board
*Request:* `DELETE /kanban/boards?id={board_id}`

*Response:*
````javascript
{
  "success": true
}
````

#### Get Boards
*Request:* `GET /kanban/boards`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "boards": [
      {
        "created_at": "2017-05-15T22:43:32+00:00",
        "id": 1,
        "title": "My Awesome Board",
        "updated_at": "2017-05-15T22:43:32+00:00",
        "todo_count": 1,
        "inprogress_count": 3,
        "done_count": 5
      },
      // More boards ..
    ]
  }
}
````

#### Get Board By ID
*Request:* `GET /kanban/boards/{board_id}`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "board": {
      "id": 1,
      "title": "My Awesome Board",
      "created_at": "2017-05-15T22:43:32+00:00",
      "updated_at": "2017-05-15T22:43:32+00:00",
      "todo": [
        // todo board_elements, see structure below
      ],
      "inprogress": [
        // inprogress board_elements, see structure below
      ],
      "done": [
        // done board_elements, see structure below
      ]
    }
  }
}
````

#### Create a Board Element
*Request:* `POST /kanban/board_elements?board_id={board_id}&description={description}&category={todo|inprogress|done}`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "board_element": {
      "id": 1,
      "board_id": 2,
      "category": "todo",
      "created_at": "2017-05-15T22:43:32+00:00",
      "updated_at": "2017-05-15T22:43:32+00:00",
      "description": "A Todo Task, I should get this done!",
      "tags": [
        {
	  "id": 0,
  	  "name": hello
    	},
    	{
    	  "id": 1,
    	  "name": world
    	}
	,
      	// More tags ..
       ]
  }
}
````

#### Get a Board Element By ID
*Request:* `GET /kanban/board_elements?{board_element_id}`

*Response:*
As create

#### Delete a Board Element
*Request:* `DELETE /kanban/board_elements?board_element_id={board_element_id}`

*Response:*
````javascript
{
  "success": true
}
````

#### Advance a Board Element
A.k.a. make a `todo` board element an `inprogress` board element, or an `inprogress`
board element a `done` board element.

*Request:* `POST /kanban/board_elements/advance?id={board_element_id}`

*Response:*
````javascript
{
  "success": true
}
````

#### Create a Tag
*Request:* `POST /kanban/tags?name={name}`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "tag": {
      "board_elements": [],
      "created_at": "2017-05-15T22:50:28+00:00",
      "id": 4,
      "name": "exercise",
      "updated_at": "2017-05-15T22:50:28+00:00"
    }
  }
}
````

#### Get All Tags
*Request:* `GET /kanban/tags`

*Response:*
````javascript
{
  "success": true,
  "data": {
    "tags": [
      {
        "board_elements": [],
        "created_at": "2017-05-15T22:50:28+00:00",
        "id": 1,
        "name": "exercise",
        "updated_at": "2017-05-15T22:50:28+00:00"
      },
      {
        "board_elements": [
          4, 5 // just indexes of the board elements that have this tag associated with them
        ],
        "created_at": "2017-05-15T22:50:28+00:00",
        "id": 2,
        "name": "exercise",
        "updated_at": "2017-05-15T22:50:28+00:00"
      }
    ]
  }
}
````

#### Get a Tag By ID
*Request:* `GET /kanban/tags/{tag_id}`

*Response:*
As create

#### Add Tag to Board Element
*Request:* `POST /kanban/tags/add?tag_id={tag_id}&board_element_id={board_element_id}`

*Response:*
````javascript
{
  "success": true
}
````

#### Remove Tag from Board Element
*Request:* `DELETE /kanban/tags/remove?tag_id={tag_id}&board_element_id={board_element_id}`

*Response:*
````javascript
{
  "success": true
}
````

## Testing

The blackbox tests for each API functionality are in test.py

## References

the set up of tables 
http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many

Schema
http://marshmallow.readthedocs.io/en/latest/examples.html
