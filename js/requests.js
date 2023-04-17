function getAllSubmittedVacations() {
    let submittedVacations = [];
    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      if(key !== "currEmp" && key !== "id"){
        const obj = JSON.parse(localStorage.getItem(key));
        if (obj["status"] === "submitted") {
          obj["userid"] = key;
          submittedVacations.push(obj);
        }
      }
    }
    return submittedVacations;
  }
  
  function SubmittedVacationsTable() {
    const table = document.getElementById('vacations-table');
    const submittedVacations = getAllSubmittedVacations().reverse();
    
    for (let i = 0; i < submittedVacations.length; i++) {
      const row = table.insertRow();
      const id = row.insertCell(0);
      const name = row.insertCell(1);
      const fromDate = row.insertCell(2);
      const toDate = row.insertCell(3);
      const reason = row.insertCell(4);
      const status = row.insertCell(5);
      const action = row.insertCell(6);
      
      id.innerHTML = submittedVacations[i]['userid'];
      name.innerHTML = submittedVacations[i]['firstName'] + ' ' + submittedVacations[i]['lastName'];
      fromDate.innerHTML = submittedVacations[i]['from-Date'];
      toDate.innerHTML = submittedVacations[i]['to-Date'];
      reason.innerHTML = submittedVacations[i]['Reason'];
      status.innerHTML = submittedVacations[i]['status'];
      action.innerHTML = '<button class="button1" onclick="approveVacation(\'' + submittedVacations[i]['userid'] + '\')">Approve</button><button class="button2" onclick="rejectVacation(\'' + submittedVacations[i]['userid'] + '\')">Reject</button>';
    }
  }
  

  function approveVacation(id) {
    let data = localStorage.getItem(id);
    let obj = JSON.parse(data);
    obj["status"] = 'approved';
    obj["vacationNum"]++;
    obj["ApprovedVactions"]--;
    delete obj["from-Date"];
    delete obj["to-Date"];
    delete obj["status"];
    localStorage.setItem(id, JSON.stringify(obj));
    location.reload(); 
  }
  
  function rejectVacation(id) {
    let data = localStorage.getItem(id);
    let obj = JSON.parse(data);
    obj["status"] = 'rejected';
    delete obj["from-Date"];
    delete obj["to-Date"];
    delete obj["status"];
    localStorage.setItem(id, JSON.stringify(obj));
    location.reload(); 
  }
  
  window.onload = function() {
    SubmittedVacationsTable();
    
  };