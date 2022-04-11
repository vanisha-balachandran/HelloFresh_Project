from flask import Flask, jsonify, request, abort, g
from flask_httpauth import HTTPBasicAuth
import db_insert

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "itismysecretkey"
auth = HTTPBasicAuth()


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


# Authentication callback
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = db_insert.UserData.verify_auth_token(username_or_token)
    if not user:
        # Second try to authenticate by login credentials
        user = db_insert.UserData.get(db_insert.UserData.username == username_or_token)
        if not user or not user.verify_password(password):
            return False
        g.user = user
    return True


# token endpoint
@app.route('/api/v1/token')
@auth.login_required
def get_auth_token():
    duration = 600
    token = g.user.generate_auth_token(duration)
    return jsonify({
        'token': token.decode('ascii'),
        'duration': duration,
        'message': 'After Duration: {duration} secs, request for a new token.'.format(duration=duration)
    })


# User registration
@app.route('/api/v1/users', methods=['POST'])
def add_new_user():
    username = request.json['username']
    password = request.json['password_hash']

    if username is None or password is None:
        abort(400)
    try:
        user = db_insert.UserData.get(db_insert.UserData.username == username)
    except:
        user = None

    if user is not None:
        abort(400)

    user = db_insert.UserData(username=username, password_hash=password)
    user.hash_password()
    user.save()
    res = jsonify({'username': user.username, "meta": {"page_url": request.url}})
    res.status_code = 201
    return res

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


if __name__ == "__main__":
    app.run(debug=True)