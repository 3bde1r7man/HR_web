//retrive local storage data
const emp_id = localStorage.getItem("current_edit_emp")
const employees = JSON.parse(localStorage.getItem("employees"))
const employee = employees[emp_id]
const form = document.querySelector('form');

for (let index = 0; index < form.children.length; index++) {
    const element = form.children[index].children[1];
    element.value = employee[element.name];
    
}
// end of retrive local storage data
// validating data
const vacationNumberInput = document.querySelector('input[name="vacation number"]');
const approvedVacationsInput = document.querySelector('input[name="approved vacations"]');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', event => {
  event.preventDefault(); // prevent the form from submitting

  const vacationNumber = parseInt(vacationNumberInput.value);
  const approvedVacations = parseInt(approvedVacationsInput.value);

  if (approvedVacations > vacationNumber) {
    errorMessage.textContent = "Can't approve more vacations than available!";
  } else {
    errorMessage.textContent = '';
    for (let index = 0; index < form.children.length; index++) {
      const element = form.children[index].children[1];
      employee[element.name] = element.value;
    }
    form.submit(); // submit the form if everything is valid
  }
});
//end of validating data

//delete data
function del() {
  delete employee;
}
//end of delete data
localStorage.setItem("employees",JSON.stringify(employees));