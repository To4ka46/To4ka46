from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Словарик с записями: ключ — заголовок, значение — текст
notes = {
    "Первая запись": "Сегодня начал изучать Flask и маршрутизацию.",
    "Вторая запись": "Разобрался с наследованием шаблонов в Jinja2.",
}

# Таблица тем на главной странице
topics = [
    "HTML & CSS",
    "Flask",
    "Jinja2 и наследование шаблонов",  # третья тема
]


@app.route("/")
def index():
    return render_template("index.html", topics=topics)


# Новый маршрут — страница "Дневник программиста"
@app.route("/diary", methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        if title and text:
            notes[title] = text
        return redirect(url_for("diary"))
    return render_template("notes.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)
