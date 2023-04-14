const usersTmp = document.querySelector("[users-template]");
const table = document.querySelector("[table]");
for(var i = 1; i < localStorage.length ; i++) {
    const userRow = usersTmp.content.cloneNode(true).children[0]
    const name = userRow.querySelector("[user-name]")
    const submit = userRow.querySelector("[submit-vac]")
    const edit = userRow.querySelector("[edit-user]")
    var obj = JSON.parse(window.localStorage.getItem(i.toString()));
    if(obj != null) {
        var firstName = obj["firstName"];
        var lastName = obj["lastName"];
        name.textContent = firstName + " " + lastName;
        submit.counter = i;
        edit.counter = i;
        submit.onclick = function() {
            localStorage.setItem("currentEmp", this.counter);
        }
        edit.onclick = function() {
            localStorage.setItem("currentEmp", this.counter);
        }
        table.appendChild(userRow)
    }
}

function search() {
    
}
