function solve() {
    const mainWrapper = document.querySelector('.wrapper');
    const taskNameInput = document.getElementById('task');
    const taskDescInput = document.getElementById('description');
    const taskDateInput = document.getElementById('date');
    const openDiv = mainWrapper.querySelectorAll('section')[1].querySelector('div:last-child');
    const inProgressDiv = mainWrapper.querySelectorAll('section')[2].querySelector('div:last-child');
    const taskCompletedDiv = mainWrapper.querySelectorAll('section')[3].querySelector('div:last-child');

    document.querySelector('#add').addEventListener('click', addFunction);

    function addFunction(event) {
        event.preventDefault();

        const startButton = '<button class="green">Start<\/button>';
        const deleteButton = '<button class="red">Delete<\/button>';
        const finishButton = '<button class="orange">Finish<\/button>';

        function addArticle(taskName, taskDesc, taskDate, first, second) {
            let articleHTML = '<h3>' + taskName;
            articleHTML += '<\/h3><p>Description: ';
            articleHTML += taskDesc;
            articleHTML += '<\/p><p>Due Date: ';
            articleHTML += taskDate;
            articleHTML += '<\/p>';
            articleHTML += addButtons(first, second);
            return articleHTML;
        };

        function addButtons(firstBtn, secondBtn) {
            let result = '<div class="flex">';
            result += firstBtn;
            result += secondBtn;
            return result + '<\/div>';
        };

        if (taskNameInput.value.length > 0 && taskDescInput.value.length > 0 && taskDateInput.value.length > 0) {
            const newTask = document.createElement('article');
            newTask.innerHTML = addArticle(taskNameInput.value, taskDescInput.value, taskDateInput.value, startButton, deleteButton);
            openDiv.appendChild(newTask);

            document.querySelector('.flex .red').addEventListener('click', deleteFunc);
            document.querySelector('.flex .green').addEventListener('click', startFunc);
            document.querySelector('.flex .orange').addEventListener('click', finishFunc);
        };
    };

    function deleteFunc(event) {
        eventTarget = event.target;
        currentElement = eventTarget.parentElement.parentElement;
        currentElement.remove();
    };
};