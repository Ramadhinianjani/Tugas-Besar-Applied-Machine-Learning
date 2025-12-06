import numpy as np
import pickle
import gradio as gr

model = pickle.load(open("model_siswa.pkl", "rb"))

def prediksi_siswa(ln, ls, pn, ps):
    data = np.array([[ln, ls, pn, ps]])
    hasil = model.predict(data)[0]
    return round(hasil)

with gr.Blocks() as app:
    gr.Markdown("# Prediksi Jumlah Siswa SD")
    ln = gr.Number(label="Laki-laki Negeri")
    ls = gr.Number(label="Laki-laki Swasta")
    pn = gr.Number(label="Perempuan Negeri")
    ps = gr.Number(label="Perempuan Swasta")
    output = gr.Number(label="Total Siswa")

    tombol = gr.Button("Prediksi")
    tombol.click(prediksi_siswa, [ln, ls, pn, ps], output)

app.launch()
