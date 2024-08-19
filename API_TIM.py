from flask import Flask, request
from flask_restful import Api, Resource, reqparse,abort
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="Number of views")
video_put_args.add_argument("likes", type=int, help="Number of likes")

videos = {}

def abort_no(video_id):
    if video_id not in videos:
        abort(404,message = "Not valid")
def abort_exist(video_id):
    if video_id in videos:
        abort(404,message = "video exist")

class Video(Resource):
    def get(self, video_id):
        if video_id in videos: 
            return videos[video_id], 200
        else:
            return {"message": "Video not found"}, 404

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self,video_id):
        abort_no(video_id)
        del videos[video_id]
        return '', 204



api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)