const BASEURL = '';

<<<<<<< HEAD
=======
function postMethod(token,data) {
    return {
        credentials: 'same-origin',
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: JSON.stringify(data),    
    }
};

>>>>>>> 789cb97... data analyzer for web
class Router {

    getFile(fileName) {
        let directoryUrl = BASEURL + 'url';
        let url = new URL(directoryUrl);
        url.search = new URLSearchParams(fileName);
        return fetch(url)
                .then(response => { 
                    if (response.ok) {
                        return response
                    } else {
                        console.log('Network response was not ok.');
                    }
                })
                .catch((error) => {
                    console.log('There has been a problem with fetch operation: ' + error.message);
                });
    }
}
