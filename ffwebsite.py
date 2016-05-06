from flask import Flask, render_template, redirect, url_for
import os
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import sqlite3

app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'comments.db'),
    SECRET_KEY='iddle idle fiddle flip'
))
Bootstrap(app)

class CommentForm(Form):
    charname = StringField('Character Name:', validators=[DataRequired()])
    server = StringField('Server:')
    gameclass = StringField('Class:', validators=[DataRequired()])
    reason = TextAreaField('Reason:', validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField('Submit')

@app.route('/')
def main():
    return render_template('main.html')
    
@app.route('/classes', methods=['GET', 'POST'])
def view_form():
    form = CommentForm()
    if form.validate_on_submit():
        charname = form.charname.data
        server = form.server.data
        gameclass = form.gameclass.data
        reason = form.reason.data
        with sqlite3.connect(app.config['DATABASE']) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO comments_table (charname, server, gameclass, reason) VALUES (?,?,?,?)", (charname, server, gameclass, reason))
            con.commit()

        return redirect(url_for('classes2'))
    return render_template('classes.html', form=form)
    
@app.route('/classes2')
def classes2():
    return render_template('classes2.html')
    
@app.route('/uldah')
def uldah():
    return render_template('uldah.html')
    
@app.route('/gridania')
def gridania():
    return render_template('gridania.html')
    
@app.route('/limsa')
def limds():
    return render_template('limsa.html')
    
@app.route('/display')
def list_results():
    with sqlite3.connect(app.config['DATABASE']) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM comments_table")
        entries = cur.fetchall()
        return render_template('flask_sqlite.html', entries=entries)
    
    
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)