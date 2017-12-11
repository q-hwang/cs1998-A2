from flask import request, jsonify, json
from . import daos, app
from base import *

board_schema = BoardSchema()
element_schema = ElementSchema()
tag_schema = TagSchema()
counted_board_schema = CountedBoardSchema()
full_board_schema = FullBoardSchema()

def to_json(data = None, success = True):
    content = {'success': success}
    if data != None :
        content['data'] = data
    return jsonify(content)

@app.route('/kanban/boards', methods=['POST'])
def create_board():
    name = request.args.get('title')
    board = daos.create_board(name)
    return to_json({"board": board_schema.dump(board).data})


@app.route('/kanban/boards', methods=['DELETE'])
def delete_board():
    id = request.args.get('id')
    success = daos.delete_board(id)
    return to_json(success = success)

@app.route('/kanban/boards', methods=['GET'])
def get_boards():
    all = daos.get_boards()
    return to_json(
        {'boards': [counted_board_schema.dump(board).data for board in all]})

@app.route('/kanban/boards/<id>', methods=['GET'])
def get_board_byID(id):
    board = daos.get_board_by_id(id)
    return to_json({'board':full_board_schema.dump(board).data})


@app.route('/kanban/board_elements', methods=['POST'])
def create_element():
    elem = daos.add_elem(request.args)
    return to_json({"board_element":element_schema.dump(elem).data})


@app.route('/kanban/board_elements', methods=['DELETE'])
def delete_element():
    id = request.args.get('board_element_id')
    success = daos.delete_elem(id)
    return to_json(success = success)

@app.route('/kanban/board_elements/<id>', methods=['GET'])
def get_element_byID(id):
    elem = daos.get_elem_by_id(id)
    return to_json({'board_element':element_schema.dump(elem).data})

@app.route('/kanban/board_elements/advance', methods=['POST'])
def advance_element():
    id = request.args.get('id')
    success = daos.advance_elem(id)
    return to_json(success = success)

@app.route('/kanban/tags', methods=['POST'])
def create_tag():
    try:
        tag = daos.create_tag(request.args.get('name'))
        return to_json({"tag":tag_schema.dump(tag).data})
    except Exception:
        return to_json(success = False)

@app.route('/kanban/tags/<id>', methods=['GET'])
def get_tag_byID(id):
    tag = daos.get_tag_by_id(id)
    return to_json({'tag':tag_schema.dump(tag).data})


@app.route('/kanban/tags', methods=['GET'])
def get_tags():
    tags = daos.get_tags()
    return to_json({"tags":
                        [tag_schema.dump(tag).data for tag in tags]})


@app.route('/kanban/tags/add', methods=['POST'])
def add_tag_to_element():
    success = daos.add_tag_to(request.args)
    return to_json(success = success)


@app.route('/kanban/tags/add', methods=['DELETE'])
def delete_tag_from_element():
    success = daos.remove_tag_from(request.args)
    return to_json(success = success)
