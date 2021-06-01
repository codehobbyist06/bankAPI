from coreAPI import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify,redirect
from coreAPI.queries import query

type_defs = load_schema_from_path("coreAPI/schema.graphql")
schema = make_executable_schema(
    type_defs, query
)

@app.route("/")
def redirect_to_gql_server():
    print(request.url)
    return redirect(request.url + "gql")

@app.route("/gql", methods=["GET"])
def graphql_playground():
    """
    This routes to the Graphql playground webpage
    provided by the ariadne library
    """
    return PLAYGROUND_HTML, 200

@app.route("/gql", methods=["POST"])
def graphql_server():
    """
    This routes to the '/gql' endpoint to which all the 
    queries can be made
    """
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        # debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code