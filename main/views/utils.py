from rest_framework.views import APIView
from rest_framework import renderers
from main import forms
from rest_framework.response import Response
from django.shortcuts import render, redirect, reverse
from main.filters.filter_handler import FilterHandler
from main.forms import BioPredictionForm
