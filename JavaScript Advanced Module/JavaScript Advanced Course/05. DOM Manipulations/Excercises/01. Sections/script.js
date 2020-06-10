function create(words) {
   const parentDiv = document.getElementById('content');

   for (let item = 0; item < words.length; item++) {
      parentDiv.appendChild(document.createElement('div'));
      const newDiv = document.querySelectorAll('#content > div')[item];
      newDiv.appendChild(document.createElement('p')).textContent = words[item];
      const newP = newDiv.firstChild;
      newP.style.display = 'none';
      newDiv.addEventListener('click', function() {
         newP.style.display = 'block';
      });
   }
}