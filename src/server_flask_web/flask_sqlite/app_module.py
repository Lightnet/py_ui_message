#!/usr/bin/env python3
#module

from flask import Flask, jsonify, make_response, render_template, request

app = Flask(__name__,template_folder='../templates')