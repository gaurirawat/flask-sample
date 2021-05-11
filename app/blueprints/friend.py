from flask import Blueprint, jsonify, request

friend_bp = Blueprint('friend', __name__)

friendDB=[
    {
        'id':'129',
        'name':'Vaibhav',
        'sex':'male'
    },
    {
        'id':'036',
        'name':'ekta',
        'sex':'female'
    }
 ]

# http://127.0.0.1:5000/friend/hello/gauri
@friend_bp.route('/hello/<string:name>/', methods = ['GET'])
def hello(name):
    return "Hello " + name + "!"

# http://127.0.0.1:5000/friend/bye
@friend_bp.route('/bye/')
def bye():
    return "Bye friend!"

# http://127.0.0.1:5000/friend/
@friend_bp.route('/',methods=['GET'])
def get():
    return jsonify({'friends':friendDB})

# http://127.0.0.1:5000/friend/036
@friend_bp.route('/<friendId>',methods=['GET'])
def get_friend(friendId):
    usr = [ friend for friend in friendDB if (friend['id'] == friendId) ] 
    return jsonify({'friend': usr})


# url: http://127.0.0.1:5000/friend/036
# body:
#     {
#         "friend":
#             {
#                 "id": "036",
#                 "name": "EKTAAA"
#             }
#      }
@friend_bp.route('/<friendId>',methods=['PUT'])
def update_friend(friendId): 
    print(request.json)
    usr = [ friend for friend in friendDB if (friend['id'] == friendId) ][0]
    print(request.json['friend']['name'])
    if 'name' in request.json['friend'] : 
        usr['name'] = request.json['friend']['name'] 
    if 'title' in request.json['friend']:
        usr['title'] = request.json['friend']['title'] 
    return jsonify({'friend':usr})

# link: http://127.0.0.1:5000/friend/add
# body:
#     {
#     "friend":
#         {
#             "id": "001",
#             "name": "aatif",
#             "sex": "MALE"
#         }
#     }
@friend_bp.route('/add', methods = ['POST'])
def add_friend():
    print(request.json)
    new_friend = {
        'id':   request.json['friend']['id'] ,
        'name': request.json['friend']['name'] ,
        'sex':  request.json['friend']['sex'] 
    }
    friendDB.append(new_friend)
    return new_friend