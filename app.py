# app.py

from flask import Flask, request, jsonify
from bst import BinarySearchTree
from flask_cors import CORS, cross_origin

app = Flask(__name__)
bst = BinarySearchTree()


# Generates a new BST
@app.route("/generate", methods=["GET"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def generate_bst():
    bst = BinarySearchTree()
    return jsonify({"result": str(bst)})


# Route to insert a key into the BST
@app.route("/insert/<int:key>", methods=["POST"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def insert(key):
    bst.insert(key)
    return jsonify({"result": str(bst)})


# Route to delete a key from the BST
@app.route("/remove/<int:key>", methods=["DELETE"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def remove(key):
    bst.delete(key)
    return jsonify({"result": str(bst)})


# Route to perform inorder traversal of the BST
@app.route("/inorder", methods=["GET"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def inorder_traversal():
    result = bst.inorder_traversal()
    return jsonify({"result": result})


# Route to perform inorder traversal of the BST
@app.route("/preorder", methods=["GET"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def preorder_traversal():
    result = bst.preorder_traversal()
    return jsonify({"result": result})


# Route to perform inorder traversal of the BST
@app.route("/postorder", methods=["GET"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def postorder_traversal():
    result = bst.postorder_traversal()
    return jsonify({"result": result})


# Clear BST
@app.route("/clear", methods=["DELETE"])
@cross_origin(origin="*", headers=["Content- Type", "Authorization"])
def clear():
    bst.clearAll()
    return jsonify({"result": ""})


if __name__ == "__main__":
    app.run(debug=True)
