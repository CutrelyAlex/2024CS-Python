from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from Core.StudentController import StudentController,DiningInfo

dining_bp = Blueprint('dining', __name__ ,url_prefix='/dining')
diningInit = StudentController()