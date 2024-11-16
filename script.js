// JavaScript for form validation

// Add event listener for form submission
document.getElementById("enrollmentForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const name = document.getElementById("name").value.trim();
    const mobile = document.getElementById("mobile").value.trim();
    const companyName = document.getElementById("company_name").value.trim();
    const dateOfJoin = document.getElementById("date_of_join").value.trim();
    const enrollmentType = document.querySelector('input[name="enrollment"]:checked');

    // Validate that all fields are filled
    if (!name || !mobile || !companyName || !dateOfJoin || !enrollmentType) {
        alert("All fields are required.");
        return;
    }

    // Validate mobile number: 10 digits and starts with 6, 7, or 9
    const mobileRegex = /^[679]\d{9}$/;
    if (!mobileRegex.test(mobile)) {
        alert("Please enter a valid 10-digit mobile number that starts with 6, 7, or 9.");
        return;
    }

    // If all validations pass
    alert("Form submitted successfully!");

    // Optionally, submit the form data using AJAX or another method
    // this.submit(); // Uncomment this if you want to submit the form after validation
});

// Function to cancel the form and reset all fields
function cancelForm() {
    document.getElementById("enrollmentForm").reset();
}
