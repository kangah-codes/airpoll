from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.module.models import Data
import requests

web = Blueprint('app', __name__)

@web.route('/', methods=['GET', 'POST'])
def index():
	url = "https://api.openaq.org/v1/measurements/coordinates=40.23,34.17"
	#url = "https://api.airvisual.com/v2/countries?key=5dbfdc43-7b14-4534-acc2-d5dbb0054b78"

	payload = {}
	files = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload, files = files)

	print(response.text.encode('utf8'))


	return "Welcome"