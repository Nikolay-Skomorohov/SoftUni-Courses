function solve() {
   const sendButtonTarget = document.getElementById('send');
   sendButtonTarget.addEventListener('click', function() {
      const allMessageTagElem = document.getElementById('chat_messages');
      const chatInputElem = document.getElementById('chat_input');
      const chatInputText = chatInputElem.value;
      const newMessageElem = document.createElement('div');
      newMessageElem.className = "message my-message";
      newMessageElem.textContent = chatInputText;
      document.getElementById('chat_messages').appendChild(newMessageElem);
      chatInputElem.value = "";
   })
}


