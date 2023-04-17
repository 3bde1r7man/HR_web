const usersTmp = document.querySelector("[users-template]");
const table = document.querySelector("[table]");
const searchInput = document.querySelector("[searchInput]");
let employees = [];

searchInput.addEventListener("input", e => {
    const value = e.target.value;
    employees.forEach(employee => {
        if(employee.name.toUpperCase().includes(value.toUpperCase())) {
            employee.element.style.display = "";
        } else {
            employee.element.style.display = "none";
        }
        
    });
    
})

for(var i = 1; i < localStorage.length ; i++) {
    const userRow = usersTmp.content.cloneNode(true).children[0]
    const name = userRow.querySelector("[user-name]")
    const submit = userRow.querySelector("[submit-vac]")
    const edit = userRow.querySelector("[edit-user]")
    var employee = JSON.parse(window.localStorage.getItem(i.toString()));
    if(employee != null) {
        
        var firstName = employee.firstName;
        var lastName = employee.lastName;
        name.textContent = firstName + " " + lastName;
        submit.empID = i;
        edit.empID = i;
        submit.onclick = function() {
            localStorage.setItem("currentEmp", this.empID);
        }
        edit.onclick = function() {
            localStorage.setItem("currentEmp", this.empID);
        }
        table.appendChild(userRow)
        employees.push({name: name.textContent, element: userRow});
    }
}