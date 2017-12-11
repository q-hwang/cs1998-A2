from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load
from . import db


class Base(db.Model):
    """
    Base database model
    """
    __abstract__ = True
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default = db.func.current_timestamp())


class Board(Base):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    board_elements = db.relationship('Element')
    todo_elements = db.relationship('Element', primaryjoin =
        "and_(Element.board_id == Board.id, Element.category =='todo')")
    inprogress_elements = db.relationship('Element',primaryjoin=
    "and_(Element.board_id == Board.id, Element.category =='inprogress')")
    done_elements = db.relationship('Element', primaryjoin=
    "and_(Element.board_id == Board.id, Element.category =='done')")

    def __init__(self, name):
        self.title = name


relation = db.Table('relation', db.Model.metadata,
                    db.Column('element_id', db.Integer, db.ForeignKey('elements.id'),
                              primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'),
                              primary_key=True)
                    )


class Element(Base):
    __tablename__ = 'elements'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))
    category = db.Column(db.String(64), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
    tags = db.relationship('Tag', secondary=relation, lazy='subquery')

    def __init__(self, description, category, board_id):
        self.description = description
        self.category = category
        self.board_id = board_id



class Tag(Base):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, unique =True)
    board_elements = db.relationship('Element',
                                     secondary=relation, lazy='subquery')

    def __init__(self, name):
        self.name = name


class SimpleTagSchema(Schema):
    """
    Serializer class to convert a Elemnent model into a dictionary
    """
    id = fields.Int()
    name = fields.Str()

class TagSchema(ModelSchema):
    """
    Serializer class to convert a Elemnent model into a dictionary
    """
    class Meta(ModelSchema.Meta):
        model = Tag


class ElementSchema(ModelSchema):
    """
    Serializer class to convert a Elemnent model into a dictionary
    """
    board_id = fields.Int()
    tags = fields.List(fields.Nested(SimpleTagSchema), attribute='tags')
    class Meta(ModelSchema.Meta):
        model = Element

class BasicBoardSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class BoardSchema(BasicBoardSchema):
  """
  Serializer class to convert a Board model into a dictionary
  """
  board_elements = fields.List(fields.Int())

class CountedBoardSchema(BasicBoardSchema):
  """
  Serializer class to convert a Board model into a dictionary
  """
  todo_count = fields.Function(lambda obj:len(obj.todo_elements))
  inprogress_count = fields.Function(lambda obj:len(obj.inprogress_elements))
  done_count = fields.Function(lambda obj:len(obj.done_elements))

class FullBoardSchema(BasicBoardSchema):
  """
  Serializer class to convert a Board model into a dictionary
  """
  todo = fields.List(fields.Nested(ElementSchema), attribute='todo_elements')
  inprogress = fields.List(fields.Nested(ElementSchema)
                           , attribute='inprogress_elements')
  done = fields.List(fields.Nested(ElementSchema), attribute='done_elements')

