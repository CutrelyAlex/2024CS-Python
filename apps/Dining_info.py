from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for

from Core.StudentController import StudentController

dining_bp = Blueprint('dining',)