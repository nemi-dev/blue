const header = document.querySelector("header")
const headerSpace = document.getElementById("HeaderSpace")

const heightStart = 120
const heightEnd = 40

const fontSizeStart = 2.5
const fontSizeEnd = 1.5

headerSpace.style.height = `${heightStart}px`

const scrollRange = heightEnd - heightStart
const fontRange = fontSizeEnd - fontSizeStart

function updateHeight() {
  const scrollY = window.scrollY
  const newHeight = Math.max(heightEnd, heightStart - scrollY)
  const newFontSize = Math.max(fontSizeEnd, fontSizeStart - scrollY * fontRange / scrollRange)

  header.style.height = `${newHeight}px`
  header.style.fontSize = `${newFontSize}rem`
}


let lastScrollY = window.scrollY
function updateShowup() {
  const delta = window.scrollY - lastScrollY
  if (delta < 0) {
    // pop up info section
  } else {
    // hide info section
  }
  lastScrollY = window.scrollY
}

window.addEventListener("scroll", () => {
  updateHeight()
  updateShowup()
})
