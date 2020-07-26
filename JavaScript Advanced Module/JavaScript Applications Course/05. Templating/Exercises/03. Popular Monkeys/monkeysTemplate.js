window.addEventListener('load', async function() {
    const sectionElem = document.getElementsByTagName('section')[0];
    const partialMonkey = await (await fetch('./templates/monkey_template.hbs')).text();
    Handlebars.registerPartial('monkey', partialMonkey);
    const mainTemplate = await (await fetch('./templates/main_template.hbs')).text();
    const mainTemplateFn = Handlebars.compile(mainTemplate);
    sectionElem.innerHTML = mainTemplateFn({ monkeys });

    sectionElem.addEventListener('click', function (e) {
        const eventTarget = e.target;
        if (eventTarget.tagName === 'BUTTON') {
            const eventButtonElem = eventTarget.parentNode.getElementsByTagName('p')[0];
            if (eventButtonElem.style.display === 'none') {
                eventButtonElem.style.display = 'block';
            }
            else {
                eventButtonElem.style.display = 'none'
            }
        }
    })
})