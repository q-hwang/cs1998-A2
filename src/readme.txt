Name: Qian Huang
NetID: qh53

================================================================================
Citations:

the set up of tables
http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many

parts of Schema 
http://marshmallow.readthedocs.io/en/latest/examples.html

================================================================================
setUp:

install requirements.txt
set up environment variables, which is in the .env and be setup use autoenv
run test.py
run run.py

================================================================================
Descriptions:
the API is mostly as specified by A2, including tag extensions
https://github.com/Cornell-PoBE/A2

Modifications:
--------------

A. For Delete a Board Element:
Instead of

DELETE /kanban/board_elements?id={board_element_id}

it is now

DELETE /kanban/board_elements?board_element_id={board_element_id}

because of the test cases are like that, and it does not hurt

B. For a standard Element:

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
  ]
}

Extensions:
-----------
A. The tag extensions in the A2 spec is done, as specified

B. Get a tag by id
GET /kanban/tags/{tag_id}

C. Get an element
GET /kanban/board_elements/{board_elements_id}

the returned data are as standard objects specified

