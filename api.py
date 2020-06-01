# Importamos todo lo necesario
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import src.predict as pr

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './src/fotos_test'

# En el navegador localhost:5000
@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('formulario.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # get image from input
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # save image
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    pics = {
        'Atocha': {'photo': "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Estaci%C3%B3n_de_Atocha_-_felipe_gabaldon.jpg/1200px-Estaci%C3%B3n_de_Atocha_-_felipe_gabaldon.jpg",
                   'url': "https://es.wikipedia.org/wiki/Estaci%C3%B3n_de_Atocha"},
        'Monumento Alfonso XII': {'photo': "https://www.esmadrid.com/sites/default/files/styles/content_type_full/public/recursosturisticos/infoturistica/monumento_alfonso_xii_carmen.jpg?itok=CAcpXoA3",
                                  'url': "https://es.wikipedia.org/wiki/Monumento_a_Alfonso_XII_de_Espa%C3%B1a"},
        'Museo Prado': {'photo': "https://aws-tiqets-cdn.imgix.net/images/content/91e400c23f0140abb059eb1958530e84.jpg?auto=format&fit=crop&ixlib=python-1.1.2&q=25&s=5cab2e6922dce4aef05898c67c6b3648&w=400&h=320&dpr=2.625",
                        'url': "https://es.wikipedia.org/wiki/Museo_del_Prado"},
        'Edificio Schweppes': {'photo': "https://madridsecreto.co/wp-content/uploads/2018/11/portada-capitol.jpg",
                               'url': "https://es.wikipedia.org/wiki/Edificio_Carri%C3%B3n"},
        'Plaza Mayor': {'photo': "https://www.esmadrid.com/sites/default/files/styles/content_type_full/public/recursosturisticos/infoturistica/panaderia_1399451332.767.jpg?itok=a_DAF8_a",
                        'url': "https://es.wikipedia.org/wiki/Casa_de_la_Panader%C3%ADa"},
        'Catedral de La Almudena': {'photo': "https://www.esmadrid.com/sites/default/files/styles/content_type_full/public/recursosturisticos/infoturistica/catedralalmudena2ok.jpg?itok=0hv37a5F",
                                    'url': "https://es.wikipedia.org/wiki/Catedral_de_la_Almudena"},
        'Ayuntamiento de Madrid': {'photo': "http://images.telemadrid.es/2019/04/13/noticias/madrid/Ayuntamiento-Madrid-compra-palacete-Carabanchel_2112398742_6930059_1300x731.jpg",
                                   'url': "https://es.wikipedia.org/wiki/Palacio_de_Cibeles"},
        'Templo de Debod': {'photo': "https://live.staticflickr.com/881/40547456784_fcba0cd06d_b.jpg",
                            'url': "https://es.wikipedia.org/wiki/Templo_de_Debod"},
        'Puerta Alcala': {'photo': "https://cheapinmadrid.es/wp-content/uploads/2018/02/puerta-alcala.jpg",
                          'url': "https://es.wikipedia.org/wiki/Puerta_de_Alcal%C3%A1"},
        'Plaza de toros Las Ventas': {'photo': "https://upload.wikimedia.org/wikipedia/commons/1/16/Plaza_de_Toros_de_Las_Ventas_%28Madrid%2C_Espa%C3%B1a%29.jpg",
                                      'url': "https://es.wikipedia.org/wiki/Las_Ventas"},
        'Banco España': {'photo': "https://e00-expansion.uecdn.es/assets/multimedia/imagenes/2017/06/16/14976383172511.jpg",
                         'url': "https://es.wikipedia.org/wiki/Banco_de_Espa%C3%B1a"},
        'Jardin Botanico': {'photo': "https://www.esmadrid.com/sites/default/files/styles/content_type_full/public/recursosturisticos/infoturistica/JARDINBOTANICO_006_alta.jpg?itok=XSqurbMY",
                            'url': "https://es.wikipedia.org/wiki/Real_Jard%C3%ADn_Bot%C3%A1nico_de_Madrid"},
        'Palacio Cristal': {'photo': "https://madridsecreto.co/wp-content/uploads/2018/04/palacio-cristal-retiro-madrid.jpg",
                            'url': "https://es.wikipedia.org/wiki/Palacio_de_Cristal_del_Retiro"}
    }

    # Predicting image saved
    pred = pr.pred(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('form_pred.html', pred=pred, pics=pics)


if __name__ == '__main__':
    # Iniciamos la aplicación
    app.run(debug=True, threaded=False)
