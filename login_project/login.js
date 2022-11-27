
// linking data from HTML code and implement it to variables
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// loading data from HTML code and implement it to variables by button click event
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // if all user credential OK - SUCCESS
    if (username === "lukasz" && password === "1234") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        // if all user credential NOK - information logon & password NOK
        if(username != "lukasz" && password != "1234")
        {
            alert("User name and possword not valid");
            loginErrorMsg.style.opacity = 1;
            location.reload();
        }
        // if user login NOK but user password OK - information that login is not valid
        if(username != "lukasz" && password === "1234")
        {
            alert("Login not valid");
            loginErrorMsg.style.opacity = 1;
            location.reload();
        }
        // if user login OK but user password NOK - information that passowrd is not valid
        if(username === "lukasz" && password != "1234")
        {
            alert("Password not valid");
            loginErrorMsg.style.opacity = 1;
            location.reload();
        }

    }
})