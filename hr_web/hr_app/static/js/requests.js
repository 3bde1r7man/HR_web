function SubmittedVacationsTable() {
  const table = document.getElementById('vacations-table');
  fetch('/all_vacations/')
    .then(response => response.json())
    .then(data => {
      data.forEach(vacation => {
        const row = table.insertRow();
        const ID = row.insertCell(0);
        const name = row.insertCell(1);
        const fromDate = row.insertCell(2);
        const toDate = row.insertCell(3);
        const reason = row.insertCell(4);
        const status = row.insertCell(5);
        const action = row.insertCell(6);

        ID.innerHTML = vacation.emp_id;
        name.innerHTML = vacation.emp_name;
        fromDate.innerHTML = vacation.fromDate;
        toDate.innerHTML = vacation.toDate;
        reason.innerHTML = vacation.reason;
        status.innerHTML = vacation.status;
        action.innerHTML = `<button class="button1" onclick="approveVacation('${vacation.emp_id}')">Approve</button><button class="button2" onclick="rejectVacation('${vacation.emp_id}')">Reject</button>`;
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function approveVacation(id) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch(`/approve_vacation/${id}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
  })
    .then(response => response.json())
    .then(data => {
      if(data.message === 'Vacation approved successfully.')
          alert(data.message)
      else if(data.message === 'Invalid number of vacation days.')  
          alert(data.message)  
    })
    .catch(error => {
      console.error('Error:', error);
    });
}


function rejectVacation(id) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
    fetch(`/reject_vacation/${id}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
    })
      .then(response => response.json())
      .then(data => {
       if(data.message === 'Vacation rejected successfully.')
          alert(data.message)
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } 
  

window.onload = function() {
  SubmittedVacationsTable();
};

