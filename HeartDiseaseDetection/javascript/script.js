// Scripting for Carousel
const carousel = document.querySelector('.carousel');
const images = carousel.querySelectorAll('img');
let counter = 0;

setInterval(() => {
  images[counter].classList.remove('active');
  counter++;
  if (counter >= images.length) {
    counter = 0;
  }
  images[counter].classList.add('active');
}, 3000);

// Scripting for Login Page

document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get form values
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Perform login validation
  if (email === "example@example.com" && password === "password") {
    // Successful login, redirect to home page
    window.location.href = "index.html";
  } else {
    // Invalid login credentials, display error message
    alert("Invalid email or password. Please try again.");
  }
});

//Scripting for SignUp page

document.getElementById("signup").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get form values
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Perform signup validation
  if (validateEmail(email)) {
    // Successful signup, display success message
    alert("Thank you for signing up, " + name + "!");

    // Reset form fields
    document.getElementById("signup").reset();
  } else {
    // Invalid email format, display error message
    alert("Invalid email format. Please enter a valid email address.");
  }
});

// Email validation helper function
function validateEmail(email) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}