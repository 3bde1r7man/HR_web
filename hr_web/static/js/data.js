// local storage will be like
// employees: {
//   "id": {
//     "firstName","value",
//     "lastName","value",
//     "email","value",
//     "address","value",
//     "userid","value",
//     "gender","value",
//     "matialStatus","value",
//     "phoneNum","value",
//      ... etc
//   }
//    "id": {
//     "firstName","value",
//     "lastName","value",
//     "email","value",
//     "address","value",
//     "userid","value",
//     "gender","value",
//     "matialStatus","value",
//     "phoneNum","value",
//      ... etc
//   },
// "id": {
//     "firstName","value",
//     "lastName","value",
//     "email","value",
//     "address","value",
//     "userid","value",
//     "gender","value",
//     "matialStatus","value",
//     "phoneNum","value",
//      ... etc
//   }  
// }


function JS() {
  let employees = JSON.parse(localStorage.getItem("employees"))
  if (employees == null) {
    employees = {};
  }
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const email = document.getElementById("email").value;
  const userid = document.getElementById("userid").value;
  const address = document.getElementById("address").value;
  let data = {
    "firstName": firstname,
    "lastName": lastname,
    "email": email,
    "address": address,
    "userid":userid
  };
  employees[userid] = data;
  localStorage.setItem("employees",JSON.stringify(employees));
  localStorage.setItem("currentEmp",userid);
}

function JS2() {
  let employees = JSON.parse(localStorage.getItem("employees"))
  const employee = employees[localStorage.getItem("currentEmp")];
  employee.gender = document.getElementById("gender").value;
  employee.materialStatus = document.getElementById("materialStatus").value;
  employee.phoneNum = document.getElementById("phoneNum").value;
  employee.vacationNum = document.getElementById("vacationNum").value;
  employee.ApprovedVactions = document.getElementById("ApprovedVactions").value;
  employee.salary = document.getElementById("salary").value;
  employee.date = document.getElementById("date").value;
  localStorage.setItem("employees",JSON.stringify(employees));
  alert("Employee added Successfully");
}