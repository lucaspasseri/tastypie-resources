xhr = new XMLHttpRequest();
xhr.open('POST', url, true);
xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
                //xhr.responseText; this contains the data
        }
    }
};
xhr.send(params);