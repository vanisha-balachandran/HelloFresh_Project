from peewee import *

psql_db = PostgresqlDatabase(
    'HelloFreshDB',
    user='postgres',
    password='srisai@2005',
    host='localhost',
)


class BaseModel(Model):

    class Meta:
        database = psql_db
        db_table = 'Recipes_table'
        table_alias = 'c'


class Recipes_table(BaseModel):
    id = PrimaryKeyField(null=False)
    RecipeName = CharField(max_length=200)
    RecipeLink = CharField(max_length=200)
    Subcatname = CharField(max_length=200)
    faves = CharField(max_length=50)
    description = CharField(max_length=300)
    Tags = CharField(max_length=50)
    Allergens = CharField(max_length=50)
    Serving_amount = BigIntegerField()
    Ingredients = CharField(max_length=300)
    items_not_included = CharField(max_length=200)
    utensils = CharField(max_length=200)
    Instructions = CharField(max_length=2000)
    Prep_time = CharField(max_length=200)
    difficulty = CharField(max_length=20)


    @property
    def serialize(self):
        data = {
            'id': self.id,
            'RecipeName': str(self.RecipeName).strip(),
            'RecipeLink': str(self.RecipeLink).strip(),
            'Subcatname': str(self.Subcatname).strip(),
            'faves': str(self.faves).strip(),
            'description': str(self.description).strip(),
            'Tags': str(self.Tags).strip(),
            'Allergens': str(self.Allergens).strip(),
            'Serving_amount': self.Serving_amount,
            'Ingredients': str(self.Ingredients).strip(),
            'items_not_included': str(self.items_not_included).strip(),
            'utensils': str(self.utensils).strip(),
            'Instructions': str(self.Instructions).strip(),
            'Prep_time': str(self.Prep_time).strip(),
            'difficulty': str(self.difficulty).strip(),

        }

        return data



    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(
            self.id,
            self.RecipeName,
            self.RecipeLink,
            self.Subcatname,
            self.faves,
            self.description,
            self.Tags,
            self.Allergens,
            self.Serving_amount,
            self.Ingredients,
            self.items_not_included,
            self.utensils,
            self.Instructions,
            self.Prep_time,
            self.difficulty
        )

        psql_db.connect()
        psql_db.create_tables(Recipes_table, safe=True)