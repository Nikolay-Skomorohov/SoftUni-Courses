function solve() {
    const mainWrapper = document.querySelector(".wrapper");
    const addTaskDiv = mainWrapper.querySelectorAll('section')[0].getElementsByClassName('div:last-child');
    const taskNameInput = document.getElementById('task');
    const taskDescInput = document.getElementById('description');
    const taskDateInput = document.getElementById('date');
    const openDiv = mainWrapper.querySelectorAll('section')[1].querySelector('div:last-child');
    const inProgressDiv = mainWrapper.querySelectorAll('section')[2].querySelector('div:last-child');
    const taskCompletedDiv  = mainWrapper.querySelectorAll('section')[3].querySelector('div:last-child');

    mainWrapper.addEventListener('click', function(e) {
        const eventTarget = e.target;
        if (eventTarget.id === "add") {
            if (taskNameInput.value && taskDescInput.value && taskDateInput.value) {
                let addResult = `<article><h3>${taskNameInput.value}<\/h3><p>Description: ${taskDescInput.value}<\/p><p>Due Date: ${taskDateInput.value}<\/p><div class="flex"><button class="green">Delete<\/button><button class="red">Finish<\/button><\/div><\/article>`;
                openDiv.innerHTML += addResult;
            };
        };
    });
}