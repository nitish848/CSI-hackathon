from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from Home.models import FIR
from django.contrib.auth import authenticate,login,logout
