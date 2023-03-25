from app import exm
from random import randrange
from math import factorial
from flask import render_template
@exm.route("/")
def index():
    list_ = [randrange(1, 200) for x in range(15)]
    list_.sort()
    return list_


@exm.route("/personal")
def personal():
    person = {
        "Ім\'я" : "Dmytro",
        "Вік" : 27,
        "Країна" : "Ukraine",
    }
    person.__getitem__
    return render_template('personal.html', content = person )

def fact_(fact = 1, n = 1):
    for i in range(1, n+1):
        fact = fact * i
    return fact
    
@exm.route("/breake_your_brain")
def breake_your_brain():
    """ Є рандомне число від 0 до 100,\
        якщо воно менше за 50 то помножити \
        на 1.5 і вивести, інакше вивести \
        його факторіал.
    """    
        
    t = randrange(0, 100)
    if t < 50:
        return f"{t*1.5}"
    return f"{fact_(n = t)}"
    