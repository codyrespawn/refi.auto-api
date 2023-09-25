from marshmallow import Schema, fields, validates


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PasswordUpdateSchema(Schema):
    current_password = fields.Str(
        required=True, validate=validates.Length(min=8))
    new_password = fields.Str(required=True, validate=validates.Length(min=8))
