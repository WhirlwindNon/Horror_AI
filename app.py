from flask import Flask, render_template, request, jsonify
import g4f 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        topic = data.get('topic', 'заброшенная больница')
        
        response = g4f.ChatCompletion.create(
            model="",
            messages=[{"role": "user", "content": f"Ты мастер мистического реализма. Напиши пугающую историю на тему '{topic}'. Избегай клише вроде 'вдруг' или 'он закричал'. Используй тактильные ощущения: холод, шепот, запах сырости, липкую темноту. История должна заканчиваться неожиданным и жутким коротким предложением. Не более 20 предложений. Избегай жестоких сцен, пиши крисиво и литературно. Можно вводить персонажей и развивать их историю."}],
        )
        
        if isinstance(response, str):
            story = response
        else:
            story = "".join(response)    
        return jsonify({"story": story})
    
    except Exception as e:
        print(f"Ошибка на сервере: {e}")
        return jsonify({"story": "Кажется, кто-то перерезал провода... Попробуй еще раз позже!"})

if __name__ == '__main__':
    app.run(debug=True)
