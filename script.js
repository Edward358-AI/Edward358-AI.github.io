let pageLinks = document.getElementById("pagelinks")
let aboutPage = document.getElementById("about")
let projectPage = document.getElementById("projects")
let showContact = document.getElementById("showcontact")
let contactInfo = document.getElementById("contact")
let dimScreen = document.getElementById("cover")

document.documentElement.addEventListener("mouseup", (e) => {
  if (!contactInfo.contains(e.target) && contactInfo.style.display == 'block') {
    contactInfo.style.display = 'none'
    dimScreen.style.display = 'none'
  }
})

showContact.onclick = () => {
  contactInfo.style.display = 'block'
  dimScreen.style.display = 'block'
}

pageLinks.addEventListener("click", (e) => {
  if (e.target.innerHTML === "About") {
    aboutPage.style.display = "inline-block"
    projectPage.style.display = "none"
  } else {
    aboutPage.style.display = "none"
    projectPage.style.display = "inline-block"
  }
})
