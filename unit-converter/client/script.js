document.querySelectorAll('li').forEach(item => item.addEventListener('click', changeTab))

function changeTab() {
    document.querySelectorAll('.active').forEach(element => {
        element.classList.remove('active')
    });
    this.classList.add('active')
    document.querySelector(`.${this.id}`).classList.add('active')
}
