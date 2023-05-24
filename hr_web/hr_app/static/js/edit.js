// retrieve local storage data
const emp_id = localStorage.getItem("currentEmp");
const employees = JSON.parse(localStorage.getItem("employees"));
const employee = employees[emp_id];
localStorage.removeItem("currentEmp");
const form = document.querySelector('form');

for (let index = 0; index < form.elements.length; index++) {
    const element = form.elements[index];
    element.value = employee[element.name];
}
// end of retrieve local storage data

form.addEventListener('submit', event => {
    if (confirm(`Are you sure you want to save`)) {
      for (let index = 0; index < form.elements.length; index++) {
        const element = form.elements[index];
        employee[element.name] = element.value;
      }
      localStorage.setItem("employees", JSON.stringify(employees));
    }
});

// delete data
function del() {
  if (confirm(`Are you sure you want to delete ${employee.firstName}?`)) {
    // remove the employee from the array
    delete employees[employee.userid]
    localStorage.setItem("employees", JSON.stringify(employees));
  }
}
// end of delete data

function del(delete_url) {
  var confirmed = confirm("Are you sure you want to delete the employee?");

  if (confirmed) {
    fetch(delete_url, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": csrf_token,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({})
    })
      .then(function (response) {
        if (response.ok) {
          console.log("Success");
        } else {
          console.log("Error");
          throw new Error("Error: " + response.status);
        }
      });
  } else {
    console.log("Deletion canceled by user.");
  }
}