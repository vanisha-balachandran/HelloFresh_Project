from model import psql_db, Recipes_table


def insert_data(receipes):
    # create table


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
    '''
    with psql_db.atomic():
        for data_dict in cities:
            City_table.create(**data_dict)
    print("Done")
'''

if __name__ == '__main__':
    # data
    receipes_data = [[1,'Quick Chicken & Vermicelli Laksa', 'quick-chicken-vermicelli-laksa', 'with Asian Greens, Lime & Coriander', 'TAKEAWAY FAVES','Colder months are coming, and that means lots of laksa! This version is laced with mild Southeast Asian spices and creamy coconut milk, plus fish sauce and rice vinegar for the perfect ratio of sweet, savoury and salty flavours - which the juicy chicken breast and silky vermicelli soak up beautifully.','Quick','[Gluten,Soy,Fish]',2,'[2 clove garlic,1 packet vermicelli noodles,1 tin coconut milk,1 bag coriander, 1/2 lime, 1 packet chicken breast, 1 bag asian greens]','[olive oil,3/4 cup water]','Large Pan','[* Boil the kettle. Finely chop garlic. Roughly chop Asian greens. Slice lime into wedges. Place vermicelli noodles in a medium heatproof bowl.*In a large saucepan, heat a good drizzle of olive oil over high heat. Cook chicken, tossing occasionally, until browned and cooked through *Return chicken to saucepan. Add Asian greens and the brown sugar *Divide vermicelli noodles between bowls. Pour over chicken laksa. • Tear over coriander. • Serve with any remaining lime wedges.]','25 minutes','Easy'],
                   [2,'Quick Chicken & Vermicelli Laksa', 'quick-chicken-vermicelli-laksa', 'with Asian Greens, Lime & Coriander', 'TAKEAWAY FAVES','Colder months are coming, and that means lots of laksa! This version is laced with mild Southeast Asian spices and creamy coconut milk, plus fish sauce and rice vinegar for the perfect ratio of sweet, savoury and salty flavours - which the juicy chicken breast and silky vermicelli soak up beautifully.','Quick','[Gluten,Soy,Fish]',4,'[4 clove garlic,1 packet vermicelli noodles,2 tin coconut milk,1 bag coriander, 1 lime, 1 packet chicken breast, 1 bag asian greens]','[olive oil,3/4 cup water]','Large Pan','[* Boil the kettle. Finely chop garlic. Roughly chop Asian greens. Slice lime into wedges. Place vermicelli noodles in a medium heatproof bowl.*In a large saucepan, heat a good drizzle of olive oil over high heat. Cook chicken, tossing occasionally, until browned and cooked through *Return chicken to saucepan. Add Asian greens and the brown sugar *Divide vermicelli noodles between bowls. Pour over chicken laksa. • Tear over coriander. • Serve with any remaining lime wedges.]','25 minutes','Easy'],
                   [3,'Vietnamese-Style Pork Bowl', 'vietnamese-style-pork-bowl', 'with Corn & Spinach Slaw', 'EXPLORER',"We've flavoured juicy pork mince with zingy ginger and lemongrass, nutty sesame oil, plus some sweet and savoury oyster sauce - and swapped rice out for a crunchy and colourful slaw to soak up the saucy deliciousness.",'Under 30g carbs','[Gluten,Sesame,Egg,Soy]',2,'[1/2 onion, 1 tin sweetcorn, 2 clove, 1 bag slaw mix, 1 packet garlic aioli]','[1 olive oil,2tbs water,1/4 rice wine vinegar, 2 egg]','Large Nonstick Pan','[*Thinly slice the red onion. In a small bowl, combine the rice wine vinegar and a good pinch of sugar and salt. *Finely chop the garlic. Drain the sweetcorn. Roughly chop the baby spinach leaves. In a second small bowl, combine the sesame oil blend (see ingredients), brown sugar, oyster sauce, soy sauce and the water *Return the frying pan to a high heat with a drizzle of olive oil. When the oil is hot, cook the pork mince, breaking it up with a spoon, until browned, 3-4 minutes *While the pork is cooking, transfer the spinach, slaw mix to the bowl with the charred corn. Top with the garlic aioli and a drizzle of olive oil. Toss to coat. Season to taste..]','30 minutes','Easy']]

    insert_data(receipes_data)