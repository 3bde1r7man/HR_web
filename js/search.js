function search() {
    localStorage.clear();
    for(var i = 0; i < localStorage.length ; i++) {
        var obj = JSON.parse(window.localStorage.getItem(i.toString()));
        if(obj != null) {
            console.log(obj["firstName"]);
        }
    }
}