function JS() {
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const email = document.getElementById("email").value;
  const userid = document.getElementById("userid").value;
  const address = document.getElementById("address").value;
  let data = `{ "firstName":"${firstname}" , "lastName":"${lastname}" , "email":"${email}","userid":"${userid}","address":"${address}" }`;
  localStorage.setItem(userid, data);
  localStorage.setItem(`id`, userid);
}
function JS2() {
  const id = localStorage.getItem("id");
  let data = localStorage.getItem(id);
  const obj = JSON.parse(data);
  const firstname = obj["firstName"];
  const lastname = obj["lastName"];
  const email = obj["email"];
  const userid = obj["userid"];
  const address = obj["address"];
  const gender = document.getElementById("gender").value;
  const materialStatus = document.getElementById("materialStatus").value;
  const phoneNum = document.getElementById("phoneNum").value;
  const vacationNum = document.getElementById("vacationNum").value;
  const ApprovedVactions = document.getElementById("ApprovedVactions").value;
  const date = document.getElementById("date").value;
  const salary = document.getElementById("salary").value;
  let totaldata = `{ "firstName":"${firstname}" , "lastName":"${lastname}" , "email":"${email}","userid":"${userid}","address":"${address}",
                                          "gender":"${gender}","materialStatus":"${materialStatus}","phoneNum":"${phoneNum}","vacationNum":"${vacationNum}","ApprovedVactions":"${ApprovedVactions}"}`;
  
  localStorage.setItem(id,totaldata);
  
}