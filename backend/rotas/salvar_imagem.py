from backend.geral.config import *
from backend.imagens.caminho import caminho_imagens

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        #print("comecando")
        file_val = request.files['foto']
        #print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho_imagens, 'passaro.png')
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    return r