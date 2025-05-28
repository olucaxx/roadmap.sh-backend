const dropdowns = document.querySelectorAll('.dropdown');
const forms = document.querySelectorAll('form');
const tabs = document.querySelectorAll('li')

function changeTab() {
    document.querySelectorAll('.active').forEach(element => {
        element.classList.remove('active');
    });

    this.classList.add('active');
    document.querySelector(`.${this.id}`).classList.add('active');
}

function selectDropdownOption(event, input, clickedOpt, dropdownContent, dropdownText, icon, options, dropdownBtn) {
    event.stopPropagation()

    options.forEach(option => option.style.backgroundColor = "#ffffff")

    clickedOpt.style.backgroundColor = "#e0e0e0";

    dropdownText.innerHTML = clickedOpt.textContent;
    input.value = clickedOpt.id
    dropdownContent.classList.remove('visible');
    dropdownBtn.classList.toggle('selecting');
    icon.innerHTML = 'v';
}

function validateFormData(form) {
    return Boolean(form.value.value && form.from.value && form.to.value)
}

tabs.forEach(tab => tab.addEventListener('click', changeTab));

dropdowns.forEach(dropdown => {
    const dropdownBtn = dropdown.querySelector('.button');
    const dropdownContent = dropdown.querySelector('.content');
    const icon = dropdown.querySelector('.icon');
    const dropdownText = dropdown.querySelector('.text');
    const dropdownOptions = dropdown.querySelectorAll('.option');
    const input = dropdown.querySelector('input')

    dropdownBtn.addEventListener('click', (event) => {
        event.stopPropagation();
        dropdownContent.classList.toggle('visible');
        dropdownBtn.classList.toggle('selecting');
        icon.innerHTML = icon.innerHTML == 'v' ? 'ʌ' : 'v';
    });

    dropdownOptions.forEach((option) => {
        option.addEventListener('click', (event) => {
            selectDropdownOption(event, input, event.currentTarget, dropdownContent, dropdownText, icon, dropdownOptions, dropdownBtn);
        });
    });
});


document.addEventListener('click', () => {
    dropdowns.forEach(dropdown => {
        dropdown.querySelector('.content').classList.remove('visible');
        dropdown.querySelector('.icon').innerHTML = 'v';
        dropdown.querySelector('.button').classList.remove('selecting');
    })
})

forms.forEach(form => { 
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        if (validateFormData(form)) {
            form.querySelector(".error-message").classList.remove('visible')
            const data = {
                type: form.id,
                value: form.value.value,
                from: form.from.value,
                to: form.to.value
            };
            return
        }
        form.querySelector(".error-message").classList.add('visible')
    });
});
