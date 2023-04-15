// function s(){
//     const id = localStorage.getItem("currentEmp");
//     let data = localStorage.getItem(id);
//     const obj = JSON.parse(data);
//     const firstname = obj["firstName"];
//     const lastname = obj["lastName"];
//     const email = obj["email"];
//     const userid = obj["userid"];
//     const address = obj["address"];
//     const gender = obj["gender"];
//     const materialStatus = obj["materialStatus"];
//     const phoneNum = obj["phoneNum"];
//     const vacationNum = obj["vacationNum"];
//     const ApprovedVactions = obj["ApprovedVactions"];
//     const date = obj["date"];
//     const salary = obj["salary"];
    
//     const fromDate=document.getElementById("from-Date").value;
//     const toDate=document.getElementById("to-Date").value;
//     const reason=document.getElementById("Reason").value;

//     let totaldata = `{"firstName":"${firstname}" , "lastName":"${lastname}" , "email":"${email}","userid":"${userid}","address":"${address}",
//                         "gender":"${gender}","materialStatus":"${materialStatus}","phoneNum":"${phoneNum}","vacationNum":"${vacationNum}",
//                             "ApprovedVactions":"${ApprovedVactions}", "from-Date":"${fromDate}", 
//                                           "to-Date":"${toDate}", "Reason":"${reason}"}`;

//     const emp_name =obj["firstName"]+" "+obj["lastName"];
//     document.getElementById("emp-Name").placeholder = emp_name;

//     document.getElementById("emp-ID").placeholder = obj["userid"];

//     localStorage.setItem(id,totaldata);
// };

// const form = document.querySelector('form');
// form.onsubmit=s();



function s(){
    const id = localStorage.getItem("currentEmp");
    let data = localStorage.getItem(id);
    const obj = JSON.parse(data);
    const firstname = obj["firstName"];
    const lastname = obj["lastName"];
    const email = obj["email"];
    const userid = obj["userid"];
    const address = obj["address"];
    const gender = obj["gender"];
    const materialStatus = obj["materialStatus"];
    const phoneNum = obj["phoneNum"];
    const vacationNum = obj["vacationNum"];
    const ApprovedVactions = obj["ApprovedVactions"];
    const date = obj["date"];
    const salary = obj["salary"];
    
    const fromDate=document.getElementById("from-Date").value;
    const toDate=document.getElementById("to-Date").value;
    const reason=document.getElementById("Reason").value;
    const status="submitted";

    let totaldata = `{"firstName":"${firstname}" , "lastName":"${lastname}" , "email":"${email}","userid":"${userid}","address":"${address}",
                        "gender":"${gender}","materialStatus":"${materialStatus}","phoneNum":"${phoneNum}","vacationNum":"${vacationNum}",
                            "ApprovedVactions":"${ApprovedVactions}", "from-Date":"${fromDate}", 
                                          "to-Date":"${toDate}", "Reason":"${reason}" , status:"${status}" , "date":"${date}" , "salary":"${salary}"}`;

    const emp_name =obj["firstName"]+" "+obj["lastName"];
    document.getElementById("emp-Name").placeholder = emp_name;

    document.getElementById("emp-ID").placeholder = obj["userid"];

    localStorage.setItem(id,totaldata);
};


