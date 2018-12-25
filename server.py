#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:51:17 2018

@author: Anastasia
"""

#%%
from flask import Flask, jsonify, request

server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)

@server.route('/degrees-of-separation/<origin>/<destination>', methods=['GET'])
def find_path(origin, destination, graph='', path=[]):
        
    graph = request.get_json()
    
    path = path + [origin]
    
    if origin == destination:
        return jsonify(len(path)-1)
    
    if origin not in graph:
        return jsonify("Origin not in graph")
    
    for node in graph[origin]:
        if node not in path:
            newpath = find_path(node, destination, graph, path)
            if newpath is not None:
                return newpath
  
    return jsonify(None)
                
server.run()