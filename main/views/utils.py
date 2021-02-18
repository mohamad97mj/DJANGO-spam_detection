from rest_framework.views import APIView
from rest_framework import renderers, status
from rest_framework.response import Response
from django.shortcuts import render, redirect, reverse
from main.filters.filter_handler import FilterHandler
from main.forms import *
from main.serializer import *
from django.http import HttpResponse
from main.filters.utils import FileUtils
import os


filter_handler = FilterHandler()

