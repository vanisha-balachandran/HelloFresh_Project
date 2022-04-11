from peewee import *

#create a PostgreSQL database
psql_db = PostgresqlDatabase(
    'HelloFreshDB',
    user='postgres',
    password='srisai@2005',
    host='localhost',
)

#create a table class to the database
class BaseModel(Model):

    class Meta:
        database = psql_db
        db_table = 'Recipes_table'
        table_alias = 'c'


#setting fields for the class
class Recipes_table(BaseModel):
    id = PrimaryKeyField(null=False)
    RecipeName = TextField()
    RecipeLink = TextField()
    Subcatname = TextField()
    faves = CharField(max_length=50)
    description = TextField()
    Tags = CharField(max_length=50)
    Allergens = CharField(max_length=50)
    Serving_amount = BigIntegerField()
    Ingredients = TextField()
    items_not_included = TextField()
    utensils = TextField()
    Instructions = TextField()
    Prep_time = TextField()
    difficulty = CharField(max_length=20)


#this function will serialize all the fieldsin the table
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
#connect to the database and create a table
psql_db.connect()
psql_db.create_tables([Recipes_table], safe=True)

#insert data to the database
def insert_data(receipes):

    with psql_db.atomic():
        # insert data
        with psql_db.atomic():
            # insert data
            for recipe in receipes:
                track = dict()
                track["RecipeName"] = recipe[1]
                track["RecipeLink"] = recipe[2]
                track["Subcatname"] = recipe[3]
                track["faves"] = recipe[4]
                track["description"] = recipe[5]
                track["Tags"] = recipe[6]
                track["Allergens"] = recipe[7]
                track["Serving_amount"] = recipe[8]
                track["Ingredients"] = recipe[9]
                track["items_not_included"] = recipe[10]
                track["utensils"] = recipe[11]
                track["Instructions"] = recipe[12]
                track["Prep_time"] = recipe[13]
                track["difficulty"] = recipe[14]

                Recipes_table.create(**track)

if __name__ == '__main__':
    # data
    receipes_data = [
        [1, 'Quick Chicken & Vermicelli Laksa', 'quick-chicken-vermicelli-laksa', 'with Asian Greens, Lime & Coriander',
         'TAKEAWAY FAVES',
         'Colder months are coming, and that means lots of laksa! This version is laced with mild Southeast Asian spices and creamy coconut milk, plus fish sauce and rice vinegar for the perfect ratio of sweet, savoury and salty flavours - which the juicy chicken breast and silky vermicelli soak up beautifully.',
         'Quick', '[Gluten,Soy,Fish]', 2,
         '[2 clove garlic,1 packet vermicelli noodles,1 tin coconut milk,1 bag coriander, 1/2 lime, 1 packet chicken breast, 1 bag asian greens]',
         '[olive oil,3/4 cup water]', 'Large Pan',
         '[* Boil the kettle. Finely chop garlic. Roughly chop Asian greens. Slice lime into wedges. Place vermicelli noodles in a medium heatproof bowl.*In a large saucepan, heat a good drizzle of olive oil over high heat. Cook chicken, tossing occasionally, until browned and cooked through *Return chicken to saucepan. Add Asian greens and the brown sugar *Divide vermicelli noodles between bowls. Pour over chicken laksa. • Tear over coriander. • Serve with any remaining lime wedges.]',
         '25 minutes', 'Easy'],
        [2, 'Quick Chicken & Vermicelli Laksa', 'quick-chicken-vermicelli-laksa', 'with Asian Greens, Lime & Coriander',
         'TAKEAWAY FAVES',
         'Colder months are coming, and that means lots of laksa! This version is laced with mild Southeast Asian spices and creamy coconut milk, plus fish sauce and rice vinegar for the perfect ratio of sweet, savoury and salty flavours - which the juicy chicken breast and silky vermicelli soak up beautifully.',
         'Quick', '[Gluten,Soy,Fish]', 4,
         '[4 clove garlic,1 packet vermicelli noodles,2 tin coconut milk,1 bag coriander, 1 lime, 1 packet chicken breast, 1 bag asian greens]',
         '[olive oil,3/4 cup water]', 'Large Pan',
         '[* Boil the kettle. Finely chop garlic. Roughly chop Asian greens. Slice lime into wedges. Place vermicelli noodles in a medium heatproof bowl.*In a large saucepan, heat a good drizzle of olive oil over high heat. Cook chicken, tossing occasionally, until browned and cooked through *Return chicken to saucepan. Add Asian greens and the brown sugar *Divide vermicelli noodles between bowls. Pour over chicken laksa. • Tear over coriander. • Serve with any remaining lime wedges.]',
         '25 minutes', 'Easy'],
        [3, 'Vietnamese-Style Pork Bowl', 'vietnamese-style-pork-bowl', 'with Corn & Spinach Slaw', 'EXPLORER',
         "We've flavoured juicy pork mince with zingy ginger and lemongrass, nutty sesame oil, plus some sweet and savoury oyster sauce - and swapped rice out for a crunchy and colourful slaw to soak up the saucy deliciousness.",
         'Under 30g carbs', '[Gluten,Sesame,Egg,Soy]', 2,
         '[1/2 onion, 1 tin sweetcorn, 2 clove, 1 bag slaw mix, 1 packet garlic aioli]',
         '[1 olive oil,2tbs water,1/4 rice wine vinegar, 2 egg]', 'Large Nonstick Pan',
         '[*Thinly slice the red onion. In a small bowl, combine the rice wine vinegar and a good pinch of sugar and salt. *Finely chop the garlic. Drain the sweetcorn. Roughly chop the baby spinach leaves. In a second small bowl, combine the sesame oil blend (see ingredients), brown sugar, oyster sauce, soy sauce and the water *Return the frying pan to a high heat with a drizzle of olive oil. When the oil is hot, cook the pork mince, breaking it up with a spoon, until browned, 3-4 minutes *While the pork is cooking, transfer the spinach, slaw mix to the bowl with the charred corn. Top with the garlic aioli and a drizzle of olive oil. Toss to coat. Season to taste..]',
         '30 minutes', 'Easy']]

    insert_data(receipes_data)