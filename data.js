function JS() {
    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const email = document.getElementById("email").value;
    const userid = document.getElementById("userid").value;
    const address = document.getElementById("address").value;
    localStorage.setItem(`firstname ${userid}`, firstname);
    localStorage.setItem(`lastname ${userid}`, lastname);
    localStorage.setItem(`email ${userid}`, email);
    localStorage.setItem(`userid ${userid}`, userid);
    localStorage.setItem(`address ${userid}`, address);
    localStorage.setItem(`id`, userid);
}


function JS2() {
    var total = 0;
    const id = localStorage.getItem("id");
    const gender = document.getElementById("gender").value;
    const materialStatus = document.getElementById("materialStatus").value;
    const phoneNum = document.getElementById("phoneNum").value;
    const vacationNum = document.getElementById("vacationNum").value;
    const ApprovedVactions = document.getElementById("ApprovedVactions").value;
    const date = document.getElementById("date").value;
    const salary = document.getElementById("salary").value;
    localStorage.setItem(`gender ${id}`, gender);
    localStorage.setItem(`materialStatus ${id}`, materialStatus);
    localStorage.setItem(`phoneNum ${id}`, phoneNum);
    localStorage.setItem(`vacationNum ${id}`, vacationNum);
    localStorage.setItem(`ApprovedVactions ${id}`, ApprovedVactions);
    localStorage.setItem(`date ${id}`, date);
    localStorage.setItem(`salary ${id}`, salary);
    localStorage.setItem(`Total employees`, ++total);
}