from flask import *
import random

app = Flask(__name__)
pet_name = 'None'
hunger = 100
experience = 0
tiredness = 100
happiness = 100


@app.route('/', methods=('GET', 'POST'))
def index():
    global pet_name
    if request.method == 'POST':
        pet_name = request.form['pet_name']
        return redirect(url_for('index_pet'))
    return render_template('creation.html')


@app.route('/pet/')
def index_pet():
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="...",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face="'Y'",
                           redirect_url=url_for('index_update'),
                           redirect_time=5000)


@app.route('/feed/')
def index_feed():
    global hunger
    hunger += 15
    if hunger > 100:
        hunger = 100
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="...",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face="'Y'",
                           redirect_url=url_for('index_pet'),
                           redirect_time=0)


@app.route('/train/')
def index_train():
    global hunger
    global tiredness
    global happiness
    global experience
    flag = False
    if hunger < 7:
        flag = True
    if tiredness < 8:
        flag = True
    if happiness < 15:
        flag = True
    if not flag:
        hunger -= 7
        tiredness -= 8
        happiness -= 15
        experience += (experience // 3) + 2
    if hunger < 0:
        hunger = 0
    if tiredness < 0:
        tiredness = 0
    if happiness < 0:
        happiness = 0
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="...",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face="'Y'",
                           redirect_url=url_for('index_pet'),
                           redirect_time=0)


@app.route('/sleep/')
def index_sleep():
    global tiredness
    tiredness += 15
    if tiredness > 100:
        tiredness = 100
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="Sleeping",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face=">Y<",
                           redirect_url=url_for('index_pet'),
                           redirect_time=3000)


@app.route('/play/')
def index_play():
    global hunger
    global tiredness
    global happiness
    global experience
    flag = False
    if hunger < 3:
        flag = True
    if tiredness < 5:
        flag = True
    if not flag:
        hunger -= 3
        tiredness -= 5
        happiness += 15
    if hunger < 0:
        hunger = 0
    if tiredness < 0:
        tiredness = 0
    if happiness > 100:
        happiness = 100
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="Happy",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face="^Y^",
                           redirect_url=url_for('index_pet'),
                           redirect_time=1000)


@app.route('/update/')
def index_update():
    global hunger
    hunger -= random.randint(0,1)
    global tiredness
    tiredness -= random.randint(0,1)
    global happiness
    happiness -= random.randint(0,1)
    if hunger < 0:
        hunger = 0
    if tiredness < 0:
        tiredness = 0
    if happiness < 0:
        happiness = 0
    return render_template('base.html',
                           pet_name=pet_name,
                           pet_status="...",
                           hunger_display=hunger,
                           experience_display=experience,
                           tiredness_display=tiredness,
                           happiness_display=happiness,
                           cat_face="'Y'",
                           redirect_url=url_for('index_pet'),
                           redirect_time=0)


if __name__ == '__main__':
    app.run(debug=True)
