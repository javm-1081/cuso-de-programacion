const tabs = document.querySelectorAll('[data-target]'),
      tabContent = document.querySelectorAll('[data-content]')

tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        const target = document.querySelector(tab.dataset.target)

        tabContent.forEach(tabContents => {
            tabContents.classList.remove('skills__active')
        })

        target.classList.add('skills__active')

        tabs.forEach(tab => {
            tab.classList.remove('skills__active')
        })

        tab.classList.add('skills__active')
    })
})

const linkWork = document.querySelectorAll('.work__item')

function activeWork() {
    linkWork.forEach(l=> l.classList.remove('active-work'))
    this.classList.add('active-work')
}

linkWork.forEach(l=> l.addEventListener("click", activeWork))

document.addEventListener("click", (e) => {
    if(e.target.classList.contains("work__button")) {
        togglePortfolioPopup();
    }
})

function togglePortfolioPopup() {
    document.querySelector(".portfolio__popup").classList.toggle("open");
}

document.querySelector(".portfolio__popup-close").addEventListener("click", togglePortfolioPopup)