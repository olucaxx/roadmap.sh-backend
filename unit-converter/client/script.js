const tabs = document.querySelectorAll('li')
const dropdowns = document.querySelectorAll('.dropdown')
const forms = document.querySelectorAll('form')
const ICON_CLOSED = 'ʌ'
const ICON_OPEN = 'v'

function changeTab() {
    document.querySelectorAll('.current-tab').forEach(element => {
        element.classList.remove('current-tab')
    })

    this.classList.add('current-tab')
    document.querySelector(`.${this.id}`).classList.add('current-tab')
}

function setupDropdown(dropdown) {
    const dropdownBtn = dropdown.querySelector('.button')
    const dropdownContent = dropdown.querySelector('.content')
    const icon = dropdown.querySelector('.icon')
    const dropdownText = dropdown.querySelector('.text')
    const dropdownOptions = dropdown.querySelectorAll('.option')
    const input = dropdown.querySelector('input')

    dropdownBtn.addEventListener('click', (event) => {
        event.stopPropagation()
        dropdownContent.classList.toggle('visible')
        dropdownBtn.classList.toggle('selecting')
        icon.innerHTML = icon.innerHTML == ICON_OPEN ? ICON_CLOSED : ICON_OPEN
    })

    dropdownOptions.forEach((option) => {
        option.addEventListener('click', (event) => {
            selectDropdownOption(event, input, event.currentTarget, dropdownContent, dropdownText, icon, dropdownOptions, dropdownBtn)
        })
    })
}

function selectDropdownOption(event, input, clickedOpt, dropdownContent, dropdownText, icon, options, dropdownBtn) {
    event.stopPropagation()

    options.forEach(opt => opt.classList.remove('selected'))

    clickedOpt.classList.add('selected')

    dropdownText.innerHTML = clickedOpt.textContent
    input.value = clickedOpt.id
    dropdownContent.classList.remove('visible')
    dropdownBtn.classList.toggle('selecting')
    icon.innerHTML = ICON_OPEN
}

function validateFormData(form) {
    return Boolean(form.value.value && form.from.value && form.to.value)
}

function resetForm(event) {
    const form = event.currentTarget
    
    form.value.value = ""
    form.querySelectorAll('.dropdown').forEach(dropdown => {
        dropdown.querySelector('input').value = ""
        dropdown.querySelector('.button .text').innerHTML = "Select unit"
        dropdown.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'))
    })
    form.querySelector(".calculation-result").classList.remove('active')
    form.querySelector(".form-inputs").classList.add('active')
}

function animateErrorMessage(errorMessage) {
    errorMessage.addEventListener('animationend', () => {
        errorMessage.classList.remove('shake-animation');
    }, {once: true});

    if (getComputedStyle(errorMessage).opacity === '1') {
        errorMessage.classList.add('shake-animation')
        return
    }
    setTimeout(() => {
        errorMessage.classList.add('shake-animation')
    }, 120) 
}

function handleFormSubmit(event) {
    event.preventDefault()
    const form = event.currentTarget
    const errorMessage = form.querySelector(".error-message")

    if (validateFormData(form)) {
        errorMessage.classList.remove('visible')
        const data = {
            type: form.id,
            value: form.value.value,    
            from: form.from.value,
            to: form.to.value
        }
        form.querySelector(".calculation-result").classList.add('active')
        form.querySelector(".form-inputs").classList.remove('active')
        return
    }
    errorMessage.classList.add('visible')
    animateErrorMessage(errorMessage)
}

function closeAllDropdowns() {
    dropdowns.forEach(dropdown => {
        dropdown.querySelector('.content').classList.remove('visible')
        dropdown.querySelector('.icon').innerHTML = ICON_OPEN
        dropdown.querySelector('.button').classList.remove('selecting')
    })
}

tabs.forEach(tab => {
    tab.addEventListener('click', changeTab)
})

dropdowns.forEach(setupDropdown)
document.addEventListener('click', closeAllDropdowns)

forms.forEach(form => { 
    form.addEventListener('submit', handleFormSubmit)
    form.addEventListener('reset', resetForm)
})
