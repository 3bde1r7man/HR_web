const usersTmp = document.querySelector("[users-template]");
const table = document.querySelector("[table]");
const searchInput = document.querySelector("[searchInput]");
const employees = JSON.parse(localStorage.getItem("employees"));
let employeesRows = [];

searchInput.addEventListener("input", e => {
    const value = e.target.value;
    employeesRows.forEach(employee => {
        if(employee.name.toUpperCase().includes(value.toUpperCase())) {
            employee.element.style.display = "";
        } else {
            employee.element.style.display = "none";
        }
        
    });
})


for(let empId in employees) {
    let emp = employees[empId];
    const userRow = usersTmp.content.cloneNode(true).children[0]
    const name = userRow.querySelector("[user-name]")
    const submit = userRow.querySelector("[submit-vac]")
    const edit = userRow.querySelector("[edit-user]")
    const submitCheck = userRow.querySelector("[submitCheck]")
    if(emp != null) {
        var firstName = emp.firstName;
        var lastName = emp.lastName;
        name.textContent = firstName + " " + lastName;
        submit.empID = empId;
        edit.empID = empId;
        submit.onclick = function() {
            if(emp.vacationNum > 0) {
                submitCheck.href = "{% url 'form' %}"
                localStorage.setItem("currentEmp", this.empID);
            } else {
                alert("You can't Submit a vacation");
            }
        }
        edit.onclick = function() {
            localStorage.setItem("currentEmp", this.empID);
        }
        table.appendChild(userRow)
        employeesRows.push({name: name.textContent, element: userRow});
    }
}