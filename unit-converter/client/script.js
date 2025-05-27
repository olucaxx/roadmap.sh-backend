let dropdowns;
const lenghtForm = document.getElementById('length-form');
const weightForm = document.getElementById('weight-form');
const tempForm = document.getElementById('temp-form');

setupDropdowns();

function changeTab() {
    document.querySelectorAll('.active').forEach(element => {
        element.classList.remove('active');
    });

    this.classList.add('active');
    document.querySelector(`.${this.id}`).classList.add('active');

    setupDropdowns();
}

function dropdownConfig(dropdown) {
    const dropdownBtn = dropdown.querySelector('.dropdown-button');
    const dropdownContent = dropdown.querySelector('.dropdown-content');
    const icon = dropdown.querySelector('.dropdown-icon');
    const dropdownText = dropdown.querySelector('.dropdown-text');
    const dropdownOptions = dropdown.querySelectorAll('.dropdown-option');
    const input = dropdown.querySelector('input')

    dropdownBtn.addEventListener('click', (event) => {
        event.stopPropagation();
        dropdownContent.classList.toggle('visible');
        icon.innerHTML = icon.innerHTML == 'v' ? 'ʌ' : 'v';
    });

    dropdownOptions.forEach((option) => {
        console.log(option.textContent)
        option.addEventListener('click', (event) => {
            selectDropdownOption(event, input, event.currentTarget, dropdownContent, dropdownText, icon, dropdownOptions);
        });
    });
}

function selectDropdownOption(event, input, clickedOpt, dropdownContent, dropdownText, icon, options) {
    event.stopPropagation()

    options.forEach(option => option.style.backgroundColor = "#ffffff")

    clickedOpt.style.backgroundColor = "#e0e0e0";

    dropdownText.innerHTML = clickedOpt.textContent;
    input.value = clickedOpt.id
    dropdownContent.classList.remove('visible');
    icon.innerHTML = 'v';
}

function setupDropdowns() {
    if (dropdowns) {
        dropdowns.forEach(dropdown => {
            // isso basicamente reseta o elemento colocando um clone "zero" no lugar dele
            dropdown.replaceWith(dropdown.cloneNode(true));
        });
    }

    dropdowns = document.querySelectorAll('.active .dropdown-div');

    dropdowns.forEach(dropdown => {
        dropdownConfig(dropdown)
    });
}

document.querySelectorAll('li').forEach(item => {
    item.addEventListener('click', changeTab);
});

document.addEventListener('click', () => {
    dropdowns.forEach(dropdown => {
        dropdown.querySelector('.dropdown-content').classList.remove('visible');
        dropdown.querySelector('.dropdown-icon').innerHTML = 'v';
    })
})