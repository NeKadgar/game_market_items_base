from utils.validators import ArgumentsSchema

all_items_schema = ArgumentsSchema()
all_items_schema.add_argument("offset", int)
all_items_schema.add_argument("limit", int)
