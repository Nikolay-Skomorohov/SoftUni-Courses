window.addEventListener('load', async function () {
     const mainElem = document.getElementById('allCats');
     Handlebars.registerPartial('cat', await (await fetch('./templates/status_cat.hbs')).text());
     const getMainTemplate = await (await fetch('./templates/main_template.hbs')).text();
     const mainTemplateFn = Handlebars.compile(getMainTemplate);
     mainElem.innerHTML = mainTemplateFn({ cats });

     mainElem.addEventListener('click', function(e) {
          const target = e.target;

          if (target.tagName === 'BUTTON') {
             const eventElemDiv = target.parentNode.querySelector('.status');
             if (eventElemDiv.style.display === 'none') {
                  eventElemDiv.style.display = 'block';
             }
             else {
                 eventElemDiv.style.display = 'none';
             }
          }
     })
})
