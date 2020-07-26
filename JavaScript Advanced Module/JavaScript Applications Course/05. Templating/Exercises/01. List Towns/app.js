window.addEventListener('load', async function () {
    const rootDivElem = document.getElementById('root');
    const inputElem = document.getElementById('towns');
    const buttonElem = document.getElementById('btnLoadTowns');
    const town_template = await (await fetch('./templates/town_template.hbs')).text();
    Handlebars.registerPartial('town', town_template)
    const templateString = await (await fetch('./templates/main_template.hbs')).text();
    const templateFunction = Handlebars.compile(templateString);


    buttonElem.addEventListener('click', function(e) {
        e.preventDefault();

        const inputString = inputElem.value.split(", ");

        rootDivElem.innerHTML = templateFunction({ input: inputString });
    })
})