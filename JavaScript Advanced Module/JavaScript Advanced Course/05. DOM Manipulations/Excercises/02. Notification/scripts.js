function notify(message) {
    const messageDiv = document.getElementById('notification');
    messageDiv.textContent = message;
    messageDiv.style.display = 'block';
    setTimeout(function () {
        messageDiv.style.display = 'none';
    }, 2000);
}