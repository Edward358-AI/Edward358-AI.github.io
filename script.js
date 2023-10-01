let pageLinks = document.getElementById("pagelinks")
let aboutPage = document.getElementById("about")
let projectPage = document.getElementById("projects")
let showContact = document.getElementById("showcontact")
let contactInfo = document.getElementById("contact")

document.documentElement.addEventListener("mouseup", (e) => {
  if (!contactInfo.contains(e.target) && contactInfo.style.display == 'block') {
    contactInfo.style.display = 'none'
  }
})

showContact.onclick = () => {
  contactInfo.style.display = 'block'
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