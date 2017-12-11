from base import *
from . import db
import utils as utils


def create_board(name):
    new_board = Board(name)
    return utils.commit_model(new_board)



def delete_board(id):
    toDelete = Board.query.filter_by(id=id).first()
    try:
        utils.delete_model(toDelete)
        return True
    except Exception:
        return False


def get_boards():
    return db.session.query(Board).order_by(Board.id).all()


def get_board_by_id(id):
    return Board.query.filter_by(id = id).first()


def add_elem(data):
    task = Element(data['description'], data['category'], data['board_id'])
    return utils.commit_model(task)


def delete_elem(id):
    toDelete = Element.query.filter_by(id=id).first()
    try:
        utils.delete_model(toDelete)
        return True
    except Exception:
        return False

def get_elem_by_id(id):
    return Element.query.filter_by(id = id).first()

def advance_elem(id):
    toAdvance = Element.query.filter_by(id=id).first()
    old_catagory = toAdvance.category
    if old_catagory == "todo":
        toAdvance.category = "inprogress"
    elif old_catagory == "inprogress":
        toAdvance.category = "done"
    db.session.commit()
    return True

def create_tag(name):
    tag = Tag(name)
    return utils.commit_model(tag)

def get_tags():
    return db.session.query(Tag).order_by(Tag.id).all()

def get_tag_by_id(id):
    return Tag.query.filter_by(id = id).first()

def add_tag_to(data):
    tag = Tag.query.filter_by(id = data['tag_id']).order_by(Tag.id).first()
    elem = Element.query.filter_by(id=data['board_element_id']).\
        order_by(Element.id).first()
    try:
        tag.board_elements.append(elem)
        db.session.commit()
        return True
    except Exception:
        return False

def remove_tag_from(data):
    tag = Tag.query.filter_by(id = data['tag_id']).order_by(Tag.id).first()
    elem = Element.query.filter_by(id=data['board_element_id']).\
        order_by(Element.id).first()
    try:
        tag.board_elements.remove(elem)
        db.session.commit()
        return True
    except Exception:
        return False
