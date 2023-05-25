function s(){
  const fromDate=document.getElementById("from-Date").value;
  const toDate=document.getElementById("to-Date").value;  
  var fromDateObj = new Date(fromDate);
  var toDateObj = new Date(toDate);
  if(fromDateObj >= toDateObj) {
    alert("From date should be less than To date")
  } 
  else{
    alert("Vacation request submitted successfully")
  }
};
