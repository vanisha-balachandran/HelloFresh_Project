from flask import Flask, jsonify, request, abort
import db_insert

app = Flask(__name__)
app.config.from_object(__name__)


# error handling
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

#using POST request to add data to DB
@app.route('/receipeadd', methods=['POST'])
def post_eg():
    row = db_insert.Recipes_table.create(**request.json)
    query = db_insert.Recipes_table.select().where(
        db_insert.Recipes_table.RecipeName == row.RecipeName,
        db_insert.Recipes_table.RecipeLink == row.RecipeLink,
        db_insert.Recipes_table.Subcatname == row.Subcatname,
        db_insert.Recipes_table.faves == row.faves,
        db_insert.Recipes_table.description == row.description,
        db_insert.Recipes_table.Tags == row.Tags,
        db_insert.Recipes_table.Allergens == row.Allergens,
        db_insert.Recipes_table.Serving_amount == row.Serving_amount,
        db_insert.Recipes_table.Ingredients == row.Ingredients,
        db_insert.Recipes_table.items_not_included == row.items_not_included,
        db_insert.Recipes_table.utensils == row.utensils,
        db_insert.Recipes_table.Instructions == row.Instructions,
        db_insert.Recipes_table.Prep_time == row.Prep_time,
        db_insert.Recipes_table.difficulty == row.difficulty
    )
    data = [i.serialize for i in query]
    res = jsonify({
         row.RecipeName: data,
        'meta': {'page_url': request.url}
    })
    res.status_code = 201
    return res

#using GET & PUT Request to get all data from DB
@app.route('/getrecipe/<string:RecipeLink>', methods=['GET'])
def put_eg(RecipeLink):
    if request.method == 'GET':
        query = db_insert.Recipes_table.select().where(
            db_insert.Recipes_table.RecipeLink == RecipeLink
        )

        data = [i.serialize for i in query]

        if data:
            res = jsonify({
                RecipeLink: data,
                'meta': {'page_url': request.url}
            })
            res.status_code = 200
        else:
            output = {
                "error": "No results found. Check url again",
                "url": request.url,
            }
            res = jsonify(output)
            res.status_code = 404
        return res

#using GET & PUT Request to get all data from DB
@app.route('/deleterecipe/<string:RecipeLink>', methods=['DELETE'])
def delete_recipe(RecipeLink):
    try:
        del_recipe = db_insert.Recipes_table.get(
            db_insert.Recipes_table.RecipeLink == RecipeLink
        )
    except:
        del_recipe = None

    if del_recipe:
        del_recipe.delete_instance()
        res = jsonify({'Success': 'Item Deleted'})
        res.status_code = 204
        return res
    else:
        res = jsonify({
            "Error": "The requested resource is no longer available at the "
                     "server and no forwarding address is known.",
            "Status Code": 410,
            "URL": request.url
        })
        res.status_code = 410
        return res


@app.route('/getrecipe/<string:RecipeLink>/<int:Serving_amount>', methods=['GET'])
def serving_func(RecipeLink,Serving_amount):

        query = db_insert.Recipes_table.select().where(
            db_insert.Recipes_table.RecipeLink == RecipeLink,
            db_insert.Recipes_table.Serving_amount == Serving_amount
        )

        data = [i.serialize for i in query]

        if data:
            res = jsonify({
                RecipeLink: data,
                'meta': {'page_url': request.url}
            })
            res.status_code = 200
        else:
            output = {
                "error": "No results found. Check url again",
                "url": request.url,
            }
            res = jsonify(output)
            res.status_code = 404
        return res


@app.route('/weeklymenu',methods=["GET"])
def weeklymenu():
    query = db_insert.Recipes_table.select()
    data = [i.serialize for i in query]
    if data:
        res = jsonify({
            'Recipes of this week': data,
            'meta': {
                'page_url': request.url}
        })
        res.status_code = 200
    else:
        # if no results are found.
        output = {
            "error": "No results found. Check url again",
            "url": request.url,
        }
        res = jsonify(output)
        res.status_code = 404
    return res

@app.route('/updatemenu/<string:RecipeLink>',methods=["PUT"])
def updatemenu(RecipeLink):
    c = db_insert.Recipes_table.get(
        db_insert.Recipes_table.RecipeLink == RecipeLink,
        )

    if not c:
        abort(404)
    if not request.json:
        abort(400)

    if 'RecipeName' in request.json and type(request.json['RecipeName']) != str:
        abort(400)
    else:
        c.district = request.json['RecipeName']
    if 'Subcatname' in request.json and type(request.json['Subcatname']) != str:
            abort(400)
    else:
            c.district = request.json['Subcatname']
    if 'faves' in request.json and type(request.json['faves']) != str:
            abort(400)
    else:
            c.district = request.json['faves']
    if 'description' in request.json and type(request.json['description']) != str:
            abort(400)
    else:
            c.district = request.json['description']
    if 'Tags' in request.json and type(request.json['Tags']) != str:
            abort(400)
    else:
            c.district = request.json['Tags']
    if 'Allergens' in request.json and type(request.json['Allergens']) != str:
            abort(400)
    else:
            c.district = request.json['Allergens']
    if 'Ingredients' in request.json and type(request.json['Ingredients']) != str:
            abort(400)
    else:
            c.district = request.json['Ingredients']
    if 'items_not_included' in request.json and type(request.json['items_not_included']) != str:
            abort(400)
    else:
            c.district = request.json['items_not_included']
    if 'utensils' in request.json and type(request.json['utensils']) != str:
            abort(400)
    else:
            c.district = request.json['utensils']
    if 'Instructions' in request.json and type(request.json['Instructions']) != str:
            abort(400)
    else:
            c.district = request.json['Instructions']
    if 'Prep_time' in request.json and type(request.json['Prep_time']) != str:
            abort(400)
    else:
            c.district = request.json['Prep_time']
    if 'difficulty' in request.json and type(request.json['difficulty']) != str:
            abort(400)
    else:
            c.district = request.json['difficulty']
    if 'Serving_amount' in request.json and type(request.json['Serving_amount']) is not int:
        abort(400)
    else:
        c.population = request.json['Serving_amount']

    c.save()

    query = db_insert.Recipes_table.select().where(
        db_insert.Recipes_table.RecipeLink == c.RecipeLink,
        )
    data = [i.serialize for i in query]
    res = jsonify({
        RecipeLink: data,
        'meta': {'page_url': request.url}
    })
    res.status_code = 200
    return res

if __name__ == "__main__":
    app.run(debug=True)