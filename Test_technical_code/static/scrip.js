function generate(action) {
    const number = document.getElementById('number').value;
    if (!number || isNaN(number) || parseInt(number) < 0) {
        alert('Input harus berupa angka positif.');
        return;
    }

    const formData = new FormData();
    formData.append('number', number);
    formData.append('action', action);

    fetch('/generate', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = data.error;
        } else {
            document.getElementById('result').innerText = data.result.join('\n');
        }
    })
    .catch(error => console.error('Error:', error));
}
