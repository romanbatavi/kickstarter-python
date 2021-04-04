from flask import Flask, render_template
from models import ArticleModel

application = Flask(__name__)

content = '''
Flask adalah web framework yang digunakan untuk mempermudah dan mempercepat
proses pengembangan aplikasi web menggunakan bahasa pemrograman Python. 
Dibandingkan dengan web framework lain, Flask memiliki cara kerja yang 
lebih sederhana.
'''

@application.route('/')
def index():
   # membuat objek dari kelas ArticleModel
   model = ArticleModel()
   
   # mengisi nilai ke dalam model
   model.setTitle('Mengenal Flask')
   model.setDate('01/02/2019')
   model.setContent(content)   
   
   # mengirim nilai ke view
   return render_template('article.html',
      judul=model.getTitle(),
      tanggal=model.getDate(),
      isi=model.getContent())

if __name__ == '__main__':
   application.run(debug=True)
