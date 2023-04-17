function s(){
  
  const id = localStorage.getItem("currentEmp");
  const employees = JSON.parse(localStorage.getItem("employees"))
  const obj = employees[id];

  const fromDate=document.getElementById("from-Date").value;
  const toDate=document.getElementById("to-Date").value;
  const reason=document.getElementById("Reason").value;
  const status="submitted";
  var fromDateObj = new Date(fromDate);
  var toDateObj = new Date(toDate);
  if(fromDateObj > toDateObj) {
    alert("Error")
  } else {
    obj.vacations = {"to-Date":toDate, "From-Date":fromDate, "Reason":reason , "status":status};
    localStorage.setItem("employees",JSON.stringify(employees)); 
    alert("Submitted successfully")
  }
  
};

function info(){

  const id = localStorage.getItem("currentEmp");
  const employees = JSON.parse(localStorage.getItem("employees"))
  const obj = employees[id];
  const emp_name =obj["firstName"]+" "+obj["lastName"];
  document.getElementById("emp-Name").placeholder = emp_name;                          
  document.getElementById("emp-ID").placeholder = id;
};

window.onload=info();
