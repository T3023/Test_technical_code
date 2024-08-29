function generate(operation) {
    const numberInput = document.getElementById('numberInput').value;
    const number = parseInt(numberInput);

    // Frontend validation for a positive integer
    if (isNaN(number) || number < 0) {
        alert('Please enter a valid positive number.');
        return;
    }

    $.ajax({
        url: '/generate',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ number: number, operation: operation }),
        success: function(response) {
            // Display the result under the form
            $('#result').text(response.result.join('\n'));
        },
        error: function(error) {
            alert(error.responseJSON.error);
        }
    });
}
