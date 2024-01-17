function submitPlan() {
    window.localStorage.setItem('name',  document.getElementById("name").value);
    window.localStorage.setItem('email',  document.getElementById("email").value);
    window.localStorage.setItem('withWho', document.getElementById("withWho").value);
    window.localStorage.setItem('meal',  document.getElementById("meal").value);
    window.localStorage.setItem('inputMax',   document.getElementById("inputMax").value);
    window.localStorage.setItem('time',  document.getElementById("time").value);
    window.localStorage.setItem('date',  document.getElementById("date").value);

    console.log(document.getElementById("email"))
    var email = localStorage.getItem("email");
    var withWho = localStorage.getItem("withWho");
    var meal = localStorage.getItem("meal");
    var inputMax = localStorage.getItem("inputMax");
    var time = localStorage.getItem("time");
    var date = localStorage.getItem("date");

    if (!email.includes("@bowdoin.edu")) {
        alert("Email must be a valid Bowdoin email!")
        return false;
    }
    
    if (email == "" || withWho == null || meal == null || inputMax == "" || time == null || date == "") {
        alert("All fields are required!")
        return false;
    }
    else if (inputMax < 1) {
        alert("Number of other people needs to be at least 1.")
        return false;
    }
    else {
    window.location.replace("review.html");
    }
}

function getMeal() {
    window.location.href = "preference_form.html";
}
