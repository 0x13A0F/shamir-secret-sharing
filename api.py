from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

api_keys = [
 "72e072a4a8f3d664db60cce141e7c733",
 "9ce5ba64e55a8f3f83917e7def3ad640",
 "cbdc7a464f34bd60361a1ed211f005db"
]

class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(400))
    y = db.Column(db.String(400))
    hash = db.Column(db.String(50),unique=True)

    def __init__(self, x, y,hash):
	    self.x = x
	    self.y = y
        self.hash = hash


class ShareSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('x','y','hash')


share_schema = ShareSchema()
shares_schema = ShareSchema(many=True)

#endpoint to show all shares
@app.route("/share", methods=["GET"])
def get_shares():
    all_shares = Share.query.all()
    result = shares_schema.dump(all_shares)
    print(result)
    return jsonify(result)


# endpoint to add new share
@app.route("/share", methods=["POST"])
def add_share():
    if 'api_key' not in request.json:
      return jsonify({"error":"Api key not found"})
    api_key = request.json['api_key']
    if (api_key not in api_keys):
      return jsonify({"error":"Invalid Key"})

    x = request.json['x']
    y = request.json['y']
    hash = request.json['hash']

    new_share = Share(x,y,hash)

    db.session.add(new_share)
    db.session.commit()

    return share_schema.jsonify(new_share)


#endpoint to get share detail by id
@app.route("/share/<hash>", methods=["POST"])
def share_detail(hash):
    if 'api_key' not in request.json:
      return jsonify({"error":"Api key not found"})
    api_key = request.json['api_key']
    if (api_key not in api_keys):
      return jsonify({"error":"Invalid Key"})

    share = Share.query.all()
    result = shares_schema.dump(share)
    for data in result.data:
      if (hash == data["hash"]):
        return jsonify(data)
    return jsonify({"error":"Not Authorized"})


# endpoint to delete all shares
@app.route("/shares",methods=["DELETE"])
def share_delete_all():
    if 'api_key' not in request.json:
      return jsonify({"error":"Api key not found"})
    api_key = request.json['api_key']
    if (api_key not in api_keys):
      return jsonify({"error":"Invalid Key"})
    all_shares = db.session.query(Share).delete()
    db.session.commit()
    return jsonify(all_shares)

if __name__ == '__main__':
    app.run("0.0.0.0",debug=False)