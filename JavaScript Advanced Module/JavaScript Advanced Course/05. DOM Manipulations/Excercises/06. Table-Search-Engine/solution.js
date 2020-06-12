function solve() {
   const searchButton = document.getElementById('searchBtn');
   const searchInput = document.getElementById('searchField');
   const tableBody = document.querySelector('tbody');
   const tableRows = Array.from(tableBody.querySelectorAll('td'));
   const tableTRs = Array.from(tableBody.querySelectorAll('tr'));

   searchButton.addEventListener('click', function() {
      tableTRs.forEach(element => {
         element.classList.remove('select');
      });
      for (let elem of tableRows) {
         if (elem.textContent.toLowerCase() === searchInput.value.toLowerCase() || 
            elem.textContent.toLowerCase().includes(searchInput.value.toLowerCase())) {
            elem.parentElement.classList.add('select');
         }
      }
      searchInput.value = "";
   });
}