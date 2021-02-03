from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import pickle
# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    p = pickle.loads(r.data)
    p.show()
    # decode image
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size='}
    # response = {'message': 'image received. size={}x{}'.format(p.shape[1], p.shape[0])
    #             }
    # encode response using jsonpickle
    # cv2.imshow('image', img)
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="192.168.0.22", port=5000)


# from flask import Flask, request, Response
# import jsonpickle
# import numpy as np
# import cv2
# import pickle
# # Initialize the Flask application
# app = Flask(__name__)


# # route http posts to this method
# @app.route('/api/test', methods=['POST'])
# def test():
#     r = request
#     # convert string of image data to uint8
#     p = pickle.loads(r.data)
#     p.show()
#     # decode image
#     # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     # do some fancy processing here....

#     # build a response dict to send back to client
#     response = {'message': 'image received. size='}
#     # response = {'message': 'image received. size={}x{}'.format(p.shape[1], p.shape[0])
#     #             }
#     # encode response using jsonpickle
#     # cv2.imshow('image', img)
#     response_pickled = jsonpickle.encode(response)

#     return Response(response=response_pickled, status=200, mimetype="application/json")


# # start flask app
# app.run(host="192.168.0.22", port=5000)
