function addItem() {
    const textInputField = document.getElementById('newItemText').value;
    const valueInputField = document.getElementById('newItemValue').value;
    const selectMenu = document.getElementById('menu');
    const newOptionCreate = document.createElement('option')
    newOptionCreate.textContent = textInputField;
    newOptionCreate.value = valueInputField;
    selectMenu.appendChild(newOptionCreate);
    document.getElementById('newItemText').value = "";
    document.getElementById('newItemValue').value = "";
}