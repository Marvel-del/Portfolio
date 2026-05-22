// ── MOBILE NAVBAR ──

// Force desktop viewport on Chrome Desktop mode


const menuIcon = document.querySelector(".menu-icon");
const navLinks = document.querySelector(".nav-links");

menuIcon.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


// ── AUTO PROJECT SLIDER ──
const slider = document.querySelector(".project-slider");
if(slider){
  let scrollAmount = 0;
  setInterval(() => {
    scrollAmount += 320;
    if (scrollAmount >= slider.scrollWidth - slider.clientWidth) {
      scrollAmount = 0;
    }
    slider.scrollTo({ left: scrollAmount, behavior: "smooth" });
  }, 5000);
}


// ── CHROME DESKTOP MODE DETECTOR ──
function applyDesktopIfNeeded() {
  const ua = navigator.userAgent;

  // Desktop mode UA: "Mozilla/5.0 (X11; Linux x86_64)..."
  // Normal portrait UA: "Mozilla/5.0 (Linux; Android 10; K)..."
  // Key difference: Desktop mode has "x86_64", normal has "Android"

  const isDesktopMode = ua.indexOf("x86_64") !== -1;

  
  if (isDesktopMode) {
    document.body.classList.add("desktop-mode");
  } else {
    document.body.classList.remove("desktop-mode");
  }
}

applyDesktopIfNeeded();
