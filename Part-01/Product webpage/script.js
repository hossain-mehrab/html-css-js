// Function to handle navigation highlighting
function handleNavigation() {
    var navBar = document.getElementById("nav-bar");
    var navLinks = navBar.getElementsByTagName("a");

    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].addEventListener("click", function () {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
        });
    }
}

// Call the function on page load
window.onload = function () {
    handleNavigation();
};
