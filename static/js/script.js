// Close messages after 3 seconds
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);