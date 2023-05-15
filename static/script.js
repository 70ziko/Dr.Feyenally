document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#chat-form');
  const messagesList = document.querySelector('#messages');
  const inputField = document.querySelector('#message-input');
  const button = document.getElementById("send-btn");

  console.log(massagesList);

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const message = inputField.value;
    inputField.value = '';

    const messageElement = document.createElement('li');
    messageElement.innerHTML = `<div class="user-message">${message}</div>`;
    messagesList.appendChild(messageElement);

    fetch('/get_response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        const botMessage = data.message;
        const botMessageElement = document.createElement('li');
        botMessageElement.innerHTML = `<div class="bot-message">${botMessage}</div>`;
        messagesList.appendChild(botMessageElement);
      });
  });

  button.addEventListener("click", function(e) {
    let input = inputField.value;
    inputField.value = "";
    output("You: " + input);
    fetch('/send_message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({message: input})
    })
    .then(response => response.json())
    .then(data => {
      output("Bot: " + data.message);
    });
  });

  function output(response) {
    const div = document.createElement("div");
    div.innerHTML = response;
    document.getElementById("chatbot").appendChild(div);
  }
});
