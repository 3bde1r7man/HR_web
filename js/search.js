const usersTmp = document.querySelector("[users-template]");
const employees = JSON.parse(localStorage.getItem("employees"));
const table = document.querySelector("table")
const searchField = document.querySelector(".place")



function expandItems(employees) {
    const usersTmp = document.querySelector("[users-template]");
    const table = document.querySelector("table");

    for (let empid in employees) {
        const userRow = usersTmp.content.cloneNode(true).children[0];
        const name = userRow.querySelector("[user-name]");
        const submit = userRow.querySelector("[submit-vac]");
        const edit = userRow.querySelector("[edit-user]");
        let emp = employees[empid];
        let firstName = emp.firstName;
        let lastName = emp.lastName;
        name.textContent = firstName + " " + lastName;
        submit.empid = empid;
        edit.empid = empid;
        submit.onclick = function() {
            localStorage.setItem("currentEmp", this.empid);
        }
        edit.onclick = function() {
            localStorage.setItem("currentEmp", this.empid);
        }
        table.appendChild(userRow);
    }
}
expandItems(employees)
function search() {
    let employees = {};
    for (let userid in employees) {
        let employee = employees[userid];
        if (userid.toLowerCase().includes(searchField.value.toLowerCase()) || employee.firstname.toLowerCase().includes(searchField.value.toLowerCase())) {
            employees[userid] = employee;
        }
    }
    if (!employees) {
        alert("NO DATA FOUNDED");
    }
    else {
        for (let i = 1; i < table.rows.length; i++) {
            table.rows[i].remove();
        }
        expandItems(employees)
    }
}