async function getStory() {
    const topic = document.getElementById('topicInput').value;
    const resultDiv = document.getElementById('result');
    
    if (!topic) {
        alert("Введите тему!");
        return;
    }
    resultDiv.innerText = "Духи шепчутся... Подождите...";

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic })
        });

        const data = await response.json();
        resultDiv.innerText = data.story;
    } catch (error) {
        resultDiv.innerText = "Ошибка связи с сервером.";
        console.error(error);
    }
}
