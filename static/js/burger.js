document.addEventListener("DOMContentLoaded", () => {
    const burger = document.querySelector(".burger"); // Select the burger button
    const navbar = document.querySelector(".navbar ul"); // Select the navbar list

    burger.addEventListener("click", () => {
        // Toggle the 'active' class on the navbar
        navbar.classList.toggle("active");

        // Optional: Change the appearance of the burger menu when toggled
        burger.classList.toggle("open");
    });
});
