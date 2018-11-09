# -*- coding: UTF-8 -*-
from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired

import word
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
class myForm(FlaskForm):
	keyword = StringField('检索', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
	keywordToNum,TitleToword,UrlLink=word.main()
	zd=[]
	url=[]
	form = myForm()
	keyword = form.keyword.data
	if form.validate_on_submit():
	#获得词库对应
		for i in keywordToNum:
			if(i == keyword):
				for j in keywordToNum[i]:
					zd.append(TitleToword[j])
					zd.append(UrlLink[j])
	return render_template('index.html', form=form, keyword=keyword,answer=zd)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)