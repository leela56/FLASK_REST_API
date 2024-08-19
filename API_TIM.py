from flask import Flask, request # Importing Flask
from flask_restful import Api, Resource, reqparse,abort # Importing Resource, reqparse,abort
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser() #we create new  object will parse automatically and 
                                          #get the information using parse_args() line 31 PUT method
video_put_args.add_argument("name", type=str, help="Name of the video") # Here name is argument and help is that which 
                                                                        #displays the value given to it  if they didn't sent the required value

video_put_args.add_argument("views", type=int, help="Number of views")
video_put_args.add_argument("likes", type=int, help="Number of likes")

videos = {} # we intialize an empty dictionary

def abort_no(video_id): # We write abort function to not crash if user hits wrong values
    if video_id not in videos:
        abort(404,message = "Not valid")
def abort_exist(video_id): # We write one more function to check if it exists
    if video_id in videos:
        abort(404,message = "video exist")

class Video(Resource):
    def get(self, video_id): # GET method
        if video_id in videos: 
            return videos[video_id], 200
        else:
            return {"message": "Video not found"}, 404

    def put(self, video_id):
        args = video_put_args.parse_args()#Here we use parse_args() to parse the arguments then store them in args
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self,video_id): # DELETE
        abort_no(video_id)
        del videos[video_id]
        return '', 204



api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)