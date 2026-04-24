from flask import Flask, render_template, request


user_input = input()
query = "SELECT * FROM users WHERE name = '" + user_input + "'"