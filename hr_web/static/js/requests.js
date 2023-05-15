let days = 0; 

function SubmittedVacationsTable() {
  const table = document.getElementById('vacations-table');
  let employees = JSON.parse(localStorage.getItem("employees"));

  for (const id in employees) {
    const obj = employees[id];
    const vac = obj['vacations'];
    if (vac && vac['status'] === "submitted") {
      const row = table.insertRow();
      const ID = row.insertCell(0);
      const name = row.insertCell(1);
      const fromDate = row.insertCell(2);
      const toDate = row.insertCell(3);
      const reason = row.insertCell(4);
      const status = row.insertCell(5);
      const action = row.insertCell(6);

      ID.innerHTML = id;
      name.innerHTML = obj['firstName']+ ' ' + obj['lastName'];
      fromDate.innerHTML = vac['From-Date'];
      toDate.innerHTML = vac['to-Date'];
      var fromDateObj = new Date(vac['From-Date']);
      var toDateObj = new Date(vac['to-Date']);
      var diff = toDateObj.getTime() - fromDateObj.getTime();
      days = Math.floor(diff / (1000 * 60 * 60 * 24));
      reason.innerHTML = vac['Reason'];
      status.innerHTML = vac['status'];
      action.innerHTML = '<button class="button1" onclick="approveVacation(\'' + id + '\')">Approve</button><button class="button2" onclick="rejectVacation(\'' + id + '\')">Reject</button>';
    }
  }
}

function approveVacation(id) {
  const employees = JSON.parse(localStorage.getItem("employees"));
  const obj = employees[id];
  if(obj.vacationNum >= days) {
    obj['vacations']['status'] = 'approved';
    obj["vacationNum"]-= days;
    obj["ApprovedVactions"]+= days;
    delete obj['vacations'];
    localStorage.setItem("employees", JSON.stringify(employees));
    location.reload();
  } else {
    alert("invalid number of vacation days");
  }
 
}

function rejectVacation(id) {
  const employees = JSON.parse(localStorage.getItem("employees"));
  const obj = employees[id];
  obj['vacations']['status'] = 'rejected';
  delete obj['vacations'];
  localStorage.setItem("employees", JSON.stringify(employees));
  location.reload();
}

window.onload = function() {
  SubmittedVacationsTable();
};